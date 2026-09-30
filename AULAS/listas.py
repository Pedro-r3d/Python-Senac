frutas = ["Maça", "Banana", "Mamão", "Uva"]

numeros = [1, 3, 5, 10]

booleanos = [True, False, True]

dados = ["Guilherme", 27, True, "Programdor"]

for dado in dados:
    print(f"{dado}")

alunos = []

alunos.append("Guilherme")
alunos.append("Vitor")
alunos.append("Pedro")

print(f"alunos[0] {alunos[0]}")
print(f"alunos[1] {alunos[1]}")
print(f"alunos[2] {alunos[-1]}")

alunos[1] = "Anna"

print(alunos)

alunos.insert(1, "Gabriela")

print(alunos)

print(alunos[1])

alunos.remove("Guilherme")

print(alunos)

alunos.pop()

print(alunos)

tamanho_lista = len(alunos)

print(tamanho_lista)