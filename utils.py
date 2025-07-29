def get_test_file_header(function_name):
    """Retorna o cabeçalho do arquivo de teste"""
    return f'''"""
Testes unitários para a função {function_name}
Gerados automaticamente por LLM baseado em análise de caminhos de execução
"""

import pytest
import sys
import os

# Adiciona o diretório pai ao path para importar a função
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa a função a ser testada
from dataset.funcoes_ramificadas import {function_name}

'''

def get_function_info_header(context):
    """Retorna o cabeçalho com informações da função"""
    return f'''
# Informações da função:
# Assinatura: {context['signature']}
# Parâmetros: {context['parameters']}
# Tipo de retorno: {context['return_type']}
# Documentação: {context['docstring']}

'''

def get_test_function_template(test_name, test_content, path_number):
    """Retorna o template para uma função de teste"""
    return f'''
def {test_name}():
    """
    Teste para caminho de execução {path_number}
    """
    {test_content.strip()}
'''