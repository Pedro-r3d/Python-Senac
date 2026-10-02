import json
from constants import NOME_ARQUIVO, ENCONDING_ARQUIVO

def salvar_caso():
        with open(NOME_ARQUIVO, "w", encoding=ENCONDING_ARQUIVO) as arquivo:
            json.dump(arquivo, indent=4, ensure_ascii=False)    

def carregar_caso():
    try:
        with open(NOME_ARQUIVO, "r", encoding=ENCONDING_ARQUIVO) as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []