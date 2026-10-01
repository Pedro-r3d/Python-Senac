import json

from Exercicios.gerenciamento_visitantes.constants import NOME_ARQUIVO, ENCONDING_ARQUIVO
def carregar_usuarios():
    try:
        with open(NOME_ARQUIVO, "r", encoding=ENCONDING_ARQUIVO) as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_usuarios(usuarios):
    with open(NOME_ARQUIVO, "w", encoding=ENCONDING_ARQUIVO) as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)      
