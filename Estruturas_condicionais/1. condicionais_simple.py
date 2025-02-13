import os 

os.system("clear") #limpa o terminal.

#solicitando dados (Entrada)
idade=int(input("Digite sua idade: ")) 
#verificando(Processamento)

if idade <18:
    print("Acesso negado!")
else:
    print("Acesso permitido!")
    #Exibindo dados (saida)


    print("==fim==")
