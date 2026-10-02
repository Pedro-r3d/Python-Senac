class Usuario():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"O nome do objeto usuário é {self.nome}"

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

usuario = Usuario("Guilherme", 27)
usuario2 = Usuario("Douglas", 32)
print(usuario)
print(usuario.nome, usuario.idade)

usuario.idade = 28

print(f"nova idade {usuario.idade}")
usuario.apresentar()
usuario2.apresentar