import json

from constants import NOME_ARQUIVO, ENCONDING_ARQUIVO

def carregar_usuarios():
    try:
        with open(NOME_ARQUIVO, "r", encoding=ENCONDING_ARQUIVO) as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_usuarios(usuarios):
    dados = []
    for usuario in usuarios:
        dados.append({
            "nome": usuario.nome,
            "data_nascimento": usuario.data_nascimento,
            "idade": usuario.idade,
            "cpf": usuario.cpf,
            "tipo_ingresso": usuario.tipo_ingresso,
            "data_visita": usuario.data_visita,
            "numero_ingresso": usuario.numero_ingresso
    })


    with open(NOME_ARQUIVO, "w", encoding=ENCONDING_ARQUIVO) as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)      
