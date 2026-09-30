usuario = {
    "nome": "João",
    "email": "joao@email.com",
    "idade": 20,
    "ativo": True,
    "pets": ["Junior", "Drago"]
}
print(f"Nome: {usuario["nome"]}")
print(f"idade: {usuario["idade"]}")

usuario["idade"] = 21
usuario["cidade"] = "Santa Cruz do Sul"

print(f"idade: {usuario["idade"]}")
print(f"Cidade: {usuario["cidade"]}")

del usuario["idade"]
usuario.pop("pets")
print(usuario)

for chave, valor in usuario.items():
    print(f"chave: {chave} | valor: {valor}")