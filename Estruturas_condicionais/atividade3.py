import os

os.system("clear") 

#solicitando dados (entrada)
#Tipagem dinamica.
#Quando a linguagem identifica tipos de dados.

primeira_nota=float(input("Digite a sua Primeira Nota:"))
segunda_nota=float(input("Digite a sua Segunda Nota:"))

media = (primeira_nota + segunda_nota) /2

  #Verificando (processamento)
if media >=7:
    print("APROVADO!")
else:
    print("REPROVADO!")

    
    #EXIBINDO DADOS (SAIDA)
    print()
    print(f"media: {media}")
    print("==FIM==")


