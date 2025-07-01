# lllm-test
project of TAES

Geração de Casos de Teste para Caminhos de Execução Específicos em um Módulo Pequeno:
Ideia: O SymPrompt propõe a "Path Constraint Prompting" para guiar LLMs na geração de testes para caminhos de execução específicos. Este projeto aplicaria essa técnica a uma função ou classe pequena e bem definida.
Objetivo: Implementar um protótipo que, dada uma função Python, identifica seus caminhos de execução (simplificado, talvez apenas condições if/else) e gera prompts para um LLM para criar casos de teste que cubram cada um desses caminhos.
Passos Chave:
Escolher uma função Python com 2-4 caminhos de execução distintos.
Realizar uma análise estática rudimentar (manual ou com uma biblioteca simples como ast) para identificar condições de ramificação e seus caminhos correspondentes.
Formular prompts para um LLM (ex: gpt-3.5-turbo ou um modelo local menor) que incluem o código da função e uma descrição do caminho de execução desejado.
Gerar testes e verificar (manualmente ou com ferramentas de cobertura de código simples) se os testes realmente cobrem os caminhos pretendidos.
Relevância dos Artigos: Reproduz o conceito central do SymPrompt da "Path Constraint Prompting" e a abordagem de decomposição multi-estágio do processo de geração de testes.
