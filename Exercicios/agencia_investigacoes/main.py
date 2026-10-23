import casosrepository
from datetime import datetime
import uuid


class Casos():
    def __init__(self, titulo,local,suspeitos=None,resolvido =False,):
        self.id_caso = str(uuid.uuid4()) # ver como fazer
        self.titulo = titulo
        self.local = local 
        self.suspeitos = suspeitos if suspeitos is not None else []  # outra classe
        self.resolvido = resolvido # booleano
        self.data_criado = datetime.now().isoformat()
        self.data_resolvido = None

    def to_dict(self):
        return {
            "id_caso": self.id_caso,
            "titulo": self.titulo,
            "local": self.local,
            "suspeitos": [s.to_dict() if hasattr(s, "to_dict") else s.__dict__ for s in self.suspeitos],
            "resolvido": self.resolvido,
            "data_criado": self.data_criado,
            "data_resolvido": self.data_resolvido
        }
dados = casosrepository.carregar_caso()

try:
    def menu():
        while True:
            print("======= AGENCIA DE INVESTIGAÇÕES =======")
            print("1- Criar novo caso")
            print("2- Adicionar suspeito")
            print("3- Registrar evidência")
            print("4- Analisar caso")
            print("5- Resolver caso")
            print("6- Listar casos")
            print("7- Sair")
            opcao = input("Escolha: ")
            if opcao == "1":
                titulo = input("Titulo do caso: ")
                local = input("Local do caso: ")

                novo_caso = Casos(titulo=titulo, local=local)
                casosrepository.salvar_caso(novo_caso)
                print("Caso cadastrado.")

            elif opcao == "2":
                dados = casosrepository.carregar_caso()
                if not dados:
                    print("Nenhum caso criado.")

                else:
                    print(dados)
                input("")

            elif opcao == "7":
                break


    if __name__ == "__main__":
        menu()
except Exception as erro:
    print(erro)
