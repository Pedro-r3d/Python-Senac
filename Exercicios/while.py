contador_numeros = 0
soma = 0
try:
    while contador_numeros != 5:
        numeros = int(input(f"Digite um número({contador_numeros + 1}): "))
        soma += numeros
        contador_numeros += 1
        print(soma)
except Exception as ex:
    print("Apenas números")
    print(ex)