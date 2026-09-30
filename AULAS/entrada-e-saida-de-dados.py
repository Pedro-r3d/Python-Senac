
nome = input("Digite seu nome: ")
try:
    idade = int(input("Digite sua idade: "))
    print(f"Olá {nome}, Você tem {idade} anos.")
    if idade <= 12:
        print("É criança")
    elif idade <= 18:
        print("é adolescente")
    else:
        print("É adulto")
except Exception:
    print("O valor da idade não é valido.")


#print(f"tipo do nome {type(nome)}")
#print(f"tipo da idade {type(idade)}")