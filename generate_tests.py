import ast
import inspect
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import pipeline
from dataset.funcoes_ramificadas import min_in_list
from prompts import UNIT_TEST_PROMPT_TEMPLATE
from utils import get_test_file_header, get_function_info_header, get_test_function_template

from path_extractor import PathVisitor

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

def write_test_file(function_name, tests, func):
    """Escreve os testes em um arquivo seguindo padrão pytest/unittest"""
    
    test_filename = f"test_{function_name}.py"
    
    header = get_test_file_header(function_name)
    
    context = get_function_context(func)
    function_info = get_function_info_header(context)
    
    test_content = ""
    for i, test in enumerate(tests):
        test_name = f"test_{function_name}_path_{i+1}"
        test_content += get_test_function_template(test_name, test, i+1)
    
    with open(test_filename, 'w', encoding='utf-8') as f:
        f.write(header + function_info + test_content)
    
    print(f"✅ Arquivo de teste criado: {test_filename}")
    print(f"📊 Total de testes gerados: {len(tests)}")
    
    return test_filename

def clean_test_output(raw_output):
    """Limpa a saída do LLM para extrair apenas o código do teste"""
    # Remove o prompt se estiver presente
    if "**Código do teste:**" in raw_output:
        raw_output = raw_output.split("**Código do teste:**")[-1]
    
    # Remove explicações no início
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
            
        # Remove linhas vazias no início
        if not in_code and line.strip() == '':
            continue
            
        # Marca que estamos no código
        if line.strip() and not line.startswith('#'):
            in_code = True
            
        if in_code:
            code_lines.append(line)
    
    return '\n'.join(code_lines).strip()

# Etapa 3: Geração do código de teste
def generate_tests_with_langchain(func, llm, prompt):
    function_name = func.__name__
    paths = extract_paths_from_function(func)
    context = get_function_context(func)
    tests = []

    print(f" Analisando função: {function_name}")
    print(f"📈 Caminhos encontrados: {len(paths)}")

    for i, path in enumerate(paths):
        print(f"  Gerando teste para caminho {i+1}/{len(paths)}...")
        path_description = "\n".join(f"- {step}" for step in path)
        
        # Formata o prompt diretamente
        formatted_prompt = prompt.format(
            function_name=function_name,
            path_description=path_description,
            signature=context["signature"],
            parameters=context["parameters"],
            docstring=context["docstring"],
            return_type=context["return_type"]
        )
        
        # Chama o LLM diretamente
        raw_result = llm(formatted_prompt)
        
        # Limpa a saída
        clean_result = clean_test_output(raw_result)
        tests.append(clean_result)

    return tests

if __name__ == "__main__":
    generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", max_new_tokens=150, device="cpu")
    llm = HuggingFacePipeline(pipeline=generator)

    # 2. Prompt template    
    prompt = PromptTemplate(
        input_variables=["function_name", "path_description", "signature", "parameters", "docstring", "return_type"],
        template=UNIT_TEST_PROMPT_TEMPLATE
    )

    # 4. Gerar testes
    tests = generate_tests_with_langchain(min_in_list, llm, prompt)
    
    # 5. Escrever arquivo de teste
    test_file = write_test_file(min_in_list.__name__, tests, min_in_list)
    
    print(f"\n Processo concluído!")
    print(f"📁 Arquivo criado: {test_file}")
    print(f"🧪 Para executar os testes: pytest {test_file}")
