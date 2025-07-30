import ast
import inspect
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import pipeline
import dataset.funcoes_ramificadas
from prompts import UNIT_TEST_PROMPT_TEMPLATE
from utils import get_test_file_header, get_function_info_header, get_test_function_template
import subprocess
import re
from path_extractor import PathVisitor

def get_functions_from_module(module):
    functions = []
    for _, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            functions.append(obj)
    return functions

def extract_paths_from_function(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)
    visitor = PathVisitor()
    visitor.visit(tree)
    return visitor.paths

def get_function_context(func):
    """Extrai contexto completo da função: assinatura, tipos e docstring"""
    sig = inspect.signature(func)
    signature_str = f"{func.__name__}{sig}"
    
    type_info = []
    for param_name, param in sig.parameters.items():
        if param.annotation != inspect.Parameter.empty:
            type_info.append(f"{param_name}: {param.annotation}")
        else:
            type_info.append(f"{param_name}: Any")
    
    docstring = func.__doc__ or "Sem documentação disponível"
    
    return_type = sig.return_annotation
    if return_type == inspect.Signature.empty:
        return_type_str = "Any"
    else:
        return_type_str = str(return_type)
    
    return {
        "signature": signature_str,
        "parameters": ", ".join(type_info),
        "docstring": docstring.strip(),
        "return_type": return_type_str
    }

def run_tests_and_get_coverage(test_file, module_to_cover):
    print(f"\nExecutando testes em: {test_file}")

    command = [
        "pytest", 
        test_file, 
        f"--cov={module_to_cover.__name__}", 
        "--cov-report=term-missing", 
        "-s",
        "-v"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        
        match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", result.stdout)
        if match:
            coverage_percentage = int(match.group(1))
            return coverage_percentage
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar pytest para {test_file}:")
        print(e.stdout)
        print(e.stderr)
    
    return 0

def write_test_file(function_name, tests, func):
    """Escreve os testes em um arquivo seguindo padrão pytest/unittest"""
    
    test_filename = f"tests/test_{function_name}.py"
    
    header = get_test_file_header(function_name)
    
    context = get_function_context(func)
    function_info = get_function_info_header(context)
    
    test_content = ""
    for i, test in enumerate(tests):
        test_name = f"test_{function_name}_path_{i+1}"
        test_content += get_test_function_template(test_name, test, i+1)
    
    with open(test_filename, 'w', encoding='utf-8') as f:
        f.write(header + function_info + test_content)
    
    print(f"Arquivo de teste criado: {test_filename}")
    print(f"Total de testes gerados: {len(tests)}")
    
    return test_filename

def clean_test_output(raw_output):
    """Limpa a saída do LLM para extrair apenas o código do teste"""
    if "**Código do teste:**" in raw_output:
        raw_output = raw_output.split("**Código do teste:**")[-1]
    
    lines = raw_output.strip().split('\n')
    code_lines = []
    in_code = False
    
    for line in lines:
        # Pula linhas que são parte do prompt
        if any(skip in line.lower() for skip in [
            "você é um especialista", "informações da função", "objetivo", 
            "requisitos", "exemplo", "importante", "gere o teste"
        ]):
            continue
        
        # Remove linhas que começam com ** (formatação markdown)
        if line.strip().startswith('**'):
            continue
            
        if not in_code and line.strip() == '':
            continue
            
        if line.strip() and not line.startswith('#'):
            in_code = True
            
        if in_code:
            code_lines.append(line)
    
    return '\n'.join(code_lines).strip()

def generate_tests_with_langchain(func, llm, prompt):
    function_name = func.__name__
    paths = extract_paths_from_function(func)
    context = get_function_context(func)
    tests = []

    print(f" Analisando função: {function_name}")
    print(f" Caminhos encontrados: {len(paths)}")

    for i, path in enumerate(paths):
        print(f"  Gerando teste para caminho {i+1}/{len(paths)}...")
        path_description = "\n".join(f"- {step}" for step in path)
        
        formatted_prompt = prompt.format(
            function_name=function_name,
            path_description=path_description,
            signature=context["signature"],
            parameters=context["parameters"],
            docstring=context["docstring"],
            return_type=context["return_type"]
        )
        
        raw_result = llm(formatted_prompt)
        
        clean_result = clean_test_output(raw_result)
        tests.append(clean_result)
    return tests

if __name__ == "__main__":
    # 1. Configuração do LLM
    generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", max_new_tokens=150, device="cpu")
    llm = HuggingFacePipeline(pipeline=generator)
    llm = []
    # 2. Prompt template    
    prompt = PromptTemplate(
        input_variables=["function_name", "path_description", "signature", "parameters", "docstring", "return_type"],
        template=UNIT_TEST_PROMPT_TEMPLATE
    )

    all_functions_coverage = {}

    for function in get_functions_from_module(dataset.funcoes_ramificadas):
        # 4. Gerar testes
        tests = generate_tests_with_langchain(function, llm, prompt)
        
        # 5. Escrever arquivo de teste
        test_file = write_test_file(function.__name__, tests, function)

        # 6. Executar os testes e obter a cobertura
        coverage = run_tests_and_get_coverage(test_file, dataset.funcoes_ramificadas)
        all_functions_coverage[function.__name__] = coverage
        print(f"Cobertura para {function.__name__}: {coverage}%")
        
    print(f"\n Processo concluído!")
    
    print("\n--- Relatório Final de Cobertura ---")
    for func_name, cov_percentage in all_functions_coverage.items():
        print(f"  {func_name}: {cov_percentage}% de Cobertura")

    print(f"Para executar todos os testes gerados: pytest test_*.py")
