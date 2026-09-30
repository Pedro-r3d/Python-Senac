email = "admin@email.com"
senha = "123456"

email_login = input("Email: ")
senha_login = input("Senha: ")

if email_login == email and senha_login == senha:
    print("Login realizado")
else:
    print("Informações incorretas")