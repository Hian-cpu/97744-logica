import os

os.system("clear")  #Limpa o terminal.

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

login_cadastrado = "Hian"
senha_cadastrada = "021983"

if login_cadastrado == login and senha_cadastrada == senha:
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos!")
