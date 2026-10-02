def saudacao():
    print("Olá, mundo")

saudacao()

def saudacao_com_nome(nome="Aluno"): ## (nome="aluno") Valor default, caso não coloque parametros.
    print(f"Olá, meu nome é {nome}")

saudacao_com_nome("Douglas")
saudacao_com_nome()

def somar(a, b):
    soma = a + b
    return soma

print(somar(5,2))

def cadastrar_usuario(nome: str, idade: int = 18):
    print(f"Cadastrando nome {nome}")
    print(f"Cadastrando idade {idade}")

idade = 27

cadastrar_usuario("Guilherme",idade)
cadastrar_usuario("João")
cadastrar_usuario(idade=32,nome="Guilherme")