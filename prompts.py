UNIT_TEST_PROMPT_TEMPLATE = """
Você é um especialista em Python e testes automatizados. Sua tarefa é gerar APENAS o código Python de um teste unitário.

**Informações da Função**:
- Assinatura: `{signature}`
- Parâmetros: {parameters}
- Tipo de retorno: {return_type}
- Documentação: {docstring}

**Caminho de execução a ser testado**:
{path_description}

**IMPORTANTE**: 
- Gere APENAS o código Python do teste
- NÃO inclua explicações, comentários extras ou o prompt
- NÃO inclua a definição da função original
- Use apenas `assert` com mensagens descritivas
- Seja explícito com valores de entrada e saída esperada

**Código do teste:**
"""