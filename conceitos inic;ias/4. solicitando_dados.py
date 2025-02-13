import os

# Limpa o terminal.
os.system("clear")

print("olá mundo")

# Solicitar dados para o usúario.
nome=input ("Digite seu nome:")
idade=int(input("Digite sua idade:"))
altura=float(input("Digite sua altura:"))


#Exibindo dados.
print()
print(f"nome:{nome}")
print(f"idade:{idade}")
print(f"altura:{altura}")
