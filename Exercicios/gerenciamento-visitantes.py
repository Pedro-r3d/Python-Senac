import uuid
import json
import os
from datetime import datetime

ARQUIVO = "./pasta/usuarios.json"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)      

usuario = {}
usuarios = carregar_usuarios()
        
while True:
    clear_console()
    try:

        print(f"========================================\nPARQUE AVENTURA\n========================================\n1 - Cadastrar visitante\n2 - Remover visitante\n3 - Listar visitantes\n4 - Ordenar visitantes\n5 - Filtrar visitantes\n6 - Consultar visitante\n7 - Consultar por data de visita\n8 - Estatícas do parque\n0 - Encerrar programa\nEscolha uma opção:")
        opcao = int(input(""))
        if opcao == 0:
            break
        #CRIAR USUARIOS
        if opcao == 1:
            clear_console()

            print("===== CRIAÇÃO DE VISITANTE =====")
            while True:
                nome = input("nome do visitante: ")
                if nome == "":
                    print("Digite algo.")
                else:
                    break
                
            while True:
                data_nascimento = input("Data de nascimento(DD/MM/AAAA): ")
                try:
                    data_nascimento_dt = datetime.strptime( 
                    data_nascimento,
                    "%d/%m/%Y"
                    ).date()
                    hoje = datetime.today().date()
                    if data_nascimento_dt > hoje:
                        print("Não pode ser do futuro.")
                    else:
                        break
                except ValueError:
                    print("Data inválida.")

            while True:
                cpf = input("CPF: ")
                if len(cpf) != 11:
                    print("CPF inválido. CPF precisa de 11 digitos.")
                elif any(u["cpf"] == cpf for u in usuarios):
                    print("CPF ja cadastrado. ")
                else:
                    break
            while True:
                try:
                    tipo_ingresso_opcao = int(input("Tipo de ingresso:\n1-VIP\n2-Normal\n3-Premium\n "))
                    if tipo_ingresso_opcao == 1:
                        tipo_ingresso = "VIP"
                        break
                    elif tipo_ingresso_opcao == 2:
                        tipo_ingresso = "Normal"
                        break
                    elif tipo_ingresso_opcao == 3:
                        tipo_ingresso = "Premium"
                        break
                    else:
                        print("Opção inválida.")
                except Exception:
                    print("Opção inválida.")
            while True:
                data_visita = input("Data da visita(DD/MM/AAAA): ")
                try:
                    data_visita_dt = datetime.strptime(
                        data_visita,
                        "%d/%m/%Y"
                    ).date()
                    hoje = datetime.today().date()
                    if data_visita_dt < hoje:
                        print("Data da visita inválida.\nInforme uma data igual ou posterior à data atual.")
                    else:
                        break
                except ValueError:
                    print("Data inválida.")
            numero_ingresso = str(uuid.uuid4())

            usuario = {
                "nome" : nome,
                "data_nascimento" : data_nascimento,
                "idade" : hoje.year - data_nascimento_dt.year,
                "cpf" : cpf,
                "tipo_ingresso" : tipo_ingresso,
                "data_visita" : data_visita,
                "numero_ingresso" : numero_ingresso
            }
            
            usuarios.append(usuario)
            salvar_usuarios(usuarios)
            
            quantidade_visitantes = len(usuarios)
            #LISTAR USUARIOS
        elif opcao == 3:
            clear_console()

            print("========= VISITANTES =========")
            for usuario in usuarios:
                print(f"Nome: {usuario["nome"]}\nIdade: {usuario["idade"]}\nIngresso: {usuario["tipo_ingresso"]}\n")
            input("")

        #APAGAR USUARIOS
        elif opcao == 2:
            clear_console()

            try:
                deletar = input("Qual usuario deletar(digite o cpf): ")
                usuario_encontrado = False
                for indice, usuario in enumerate(usuarios):
                    if usuario["cpf"] == deletar:
                        usuario_encontrado = True
                        usuarios.pop(indice)
                        salvar_usuarios(usuarios)
                        print(f"Visitante {usuario["nome"]} removido.")
                        input("-Voltar-")
                if not usuario_encontrado:
                    print("Visitante com esse CPF não foi encontrado.")
                    input("-Voltar-")
            except Exception:
                print("Valor inválido")
                input("-Voltar-")

        #ORDENADO POR IDADE OU NOME
        elif opcao == 4:
            clear_console()
            print("====== ORDENAR VISITANTES ======")
            print("1- Ordenar por nome\n2- Ordenar por idade")
            ordenado = input("")
            
            visitantes_ordenados = usuarios.copy()
            
            if ordenado == "1":
                 for i in range(len(visitantes_ordenados)):
                    for j in range(i + 1, len(visitantes_ordenados)):

                        if visitantes_ordenados[i]["nome"].lower() > visitantes_ordenados[j]["nome"].lower():

                            visitantes_ordenados[i], visitantes_ordenados[j] = (
                                visitantes_ordenados[j],
                                visitantes_ordenados[i]
                            )
                    print("\n===== VISITANTES ORDENADOS POR NOME =====")

                    for usuario in visitantes_ordenados:
                        print(
                        f'Nome: {usuario["nome"]}\n'
                        f'Idade: {usuario["idade"]}\n'
                        f'Tipo de ingresso: {usuario["tipo_ingresso"]}\n'
                     )
                    input("-Voltar-")
            elif ordenado == "2":
                 for i in range(len(visitantes_ordenados)):
                    for j in range(i + 1, len(visitantes_ordenados)):

                        if visitantes_ordenados[i]["idade"] > visitantes_ordenados[j]["idade"]:

                            visitantes_ordenados[i], visitantes_ordenados[j] = (
                                visitantes_ordenados[j],
                                visitantes_ordenados[i]
                            )

                    print("\n===== VISITANTES ORDENADOS POR IDADE =====")

                    for usuario in visitantes_ordenados:
                        print(
                        f'Nome: {usuario["nome"]}\n'
                        f'Idade: {usuario["idade"]}\n'
                        f'Tipo de ingresso: {usuario["tipo_ingresso"]}\n'
                     )
                    input("-Voltar-")
            
        elif opcao == 5:
            clear_console()

            print("====== FILTRAR POR INGRESSO ======")
            print("1 - Normal\n2 - VIP\n3 - Premium")
            tipo = int(input(""))
            tipo_existe = False
            for usuario in usuarios:
                if tipo == 2:
                    if usuario["tipo_ingresso"] == "VIP":
                        tipo_existe = True
                        print(usuario)
                
                elif tipo == 1:
                    if usuario["tipo_ingresso"] == "Normal":
                        tipo_existe = True
                        print(usuario)
                
                elif tipo == 3:
                    if usuario["tipo_ingresso"] == "Premium":
                        tipo_existe = True
                        print(usuario)
            if not tipo_existe:
                print("Usuario não encontrado\n-Voltar-")
            input("")

    # BUSCAR POR CPF
        elif opcao == 6:
            clear_console()

            print("====== BUSCAR POR CPF =====")
            cpf_buscar = input("Digite o cpf: ")
            cpf_existe = False
            for usuario in usuarios:
                if usuario["cpf"] == cpf_buscar:
                    cpf_existe = True
                    print("======= INGRESSO ENCONTRADO =======")
                    print(f"Nome: {usuario["nome"]}\nIdade: {usuario["idade"]}\nCPF: {usuario["cpf"]}\nData de nascimento: {usuario["data_nascimento"]}\nIngresso: {usuario["tipo_ingresso"]}\nData da visita: {usuario["data_visita"]}\n\nNúmero do ingresso: {usuario["numero_ingresso"]}")
                    input("- Voltar -")
            if not cpf_existe:
                input("CPF não encontrado.\n -Voltar-")

        elif opcao == 7:
            clear_console()

            print("====== BUSCAR POR DATA ======")
            try:
                data_buscada = input("Data da visita: ")

                data_buscada = datetime.strptime(
                    data_buscada,
                    "%d/%m/%Y"
                ).date()

                data_encontrada = False
                for usuario in usuarios:
                    data_expecifica = datetime.strptime(
                        usuario["data_visita"],
                        "%d/%m/%Y"
                    ).date()
                    if data_expecifica == data_buscada:
                        data_encontrada = True
                        print(f"{usuario["nome"]} - {usuario["idade"]} - {usuario["tipo_ingresso"]}")
                if not data_encontrada:
                    print("Visitantes com essa data não encontrado")
                input("- VOLTAR -")
            except Exception:
                print("Data inválida")
                input("-Voltar-")
        elif opcao == 8:
            print("====== ESTATISTICAS DO PARQUE ======")
            total_vip = 0
            total_normal = 0
            total_premium = 0
            idades = [usuario.get("idade") for usuario in usuarios if "idade" in usuario]
            total_usuarios = len(usuarios)
            media_idade = sum(idades) / total_usuarios
            
            for usuario in usuarios:
        
                if usuario.get("tipo_ingresso") == "VIP":
                    total_vip += 1

                if usuario.get("tipo_ingresso") == "Normal":
                    total_normal += 1

                if usuario.get("tipo_ingresso") == "Premium":
                    total_premium += 1

            print(f"Total de visitantes tipo VIP: {total_vip}")
            print(f"Total de visitantes tipo Normal: {total_normal}")
            print(f"Total de visitantes tipo Premium: {total_premium}")
            print(f"Média de idade dos visitantes: {media_idade}")
            input("- Voltar -")

    except Exception as erro:
        print("Valor inválido")
        print(erro)
        input("-Voltar-")