import json
from constants import NOME_ARQUIVO, ENCONDING_ARQUIVO

def salvar_caso(novo_caso_objeto):
        lista_caso = carregar_caso()
        from main import Casos  

        if isinstance(lista_caso, dict):
            lista_caso = [lista_caso]

        lista_caso.append(novo_caso_objeto.to_dict())

        with open(NOME_ARQUIVO, "w", encoding=ENCONDING_ARQUIVO) as arquivo:
            json.dump(lista_caso,arquivo, indent=4, ensure_ascii=False)    

def carregar_caso():
    try:
        with open(NOME_ARQUIVO, "r", encoding=ENCONDING_ARQUIVO) as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []