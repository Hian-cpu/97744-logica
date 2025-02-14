import os

os.system("clear") #limpa de terminal.

#solicitando dados (entrada)
#Tipagem dinamica.
#Quando a linguagem identifica tipos de dados.
primeira_nota=float(input("Digite a sua primeira nota:"))
print()
segunda_nota=float(input("Digite a sua segunda nota:"))
print()
terceira_nota=float(input("Digite a sua terceira nota"))
print()


media = (primeira_nota + segunda_nota + terceira_nota) /3 


 #verificando (processamento)

if media >7:
    print("APROVADO!")
else:
    print("REPROVADO!")

#EXIBINDO DADOS (SAIDA)
print()
print(f"media: {media}")
print('==FIM==')