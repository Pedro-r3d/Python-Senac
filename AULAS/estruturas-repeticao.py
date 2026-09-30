contador = 1

while contador <= 10:

    if contador == 3:
        contador += 1
        continue

    if contador == 5:
        break
        
    print(f"contador {contador}")
    contador += 1

for numero in range(1, 5):
    print(f"Número {numero}")
 
for numero in range(0, 11, 2):
    print(f"Número 2 em 2: {numero}")

for numero in range(10, -1, -1):
    print(f"Número negativo: {numero}")

for letra in "Pedro":
    print(f"letra {letra}")

frutas = ["Maça", "Banana", "Mamão"]

for fruta in frutas:
    print(f"Frutas {fruta}")

print("Usando enumerate")

for indice, fruta in enumerate(frutas, start=1):
    print(f"Indice {indice}: {fruta}")