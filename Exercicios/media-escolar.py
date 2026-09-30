from decimal import Decimal


try:
    nome = input("Qual o nome do aluno? ")
    nota1 = Decimal(input("Nota do primeiro trimestre: "))
    nota2 = Decimal(input("Nota do segundo trimestre: "))
    nota3 = Decimal(input("Nota do terceiro trimestre: "))

    nota_final = (nota1 + nota2 + nota3) / 3

    print(f"Aluno: {nome} ")
    print(f"1º tri: {nota1}; 2º tri: {nota2}; 3º tri {nota3}")
    print(f"Média final: {nota_final:.2f}")

    if nota_final >= 7:
        print("Aprovado")
    elif nota_final > 5 and nota_final <= 6.9:
        print("Recuperação")
    else:
        print("Reprovado")

except Exception:
    print("Informação inválida")
