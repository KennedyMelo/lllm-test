UNIT_TEST_PROMPT_TEMPLATE = """
Você é um especialista em Python e testes automatizados.
Sua tarefa é gerar exclusivamente o código Python de um teste unitário para a função abaixo que cobre o caminho de execução especificado.

**Detalhes da Função**:
- Assinatura: `{signature}`
- Parâmetros: {parameters}
- Tipo de retorno: {return_type}
- Documentação: {docstring}

**Caminho de execução a ser testado**:
{path_description}

**Instruções obrigatórias**:
- Gere apenas o código do teste unitário em Python
- Utilize apenas `assert` com mensagens claras e descritivas
- Não inclua explicações, comentários, o prompt ou a definição da função original
- Seja explícito nos valores de entrada e saída esperados
- O teste deve ser direto, objetivo e completo para o caminho informado

**Código do teste unitário:**
"""