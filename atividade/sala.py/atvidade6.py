import os

os.system("clear")
Desejo = int(input("Quantidades de maçãs Desejadas?"))



if Desejo < 12:
   preco_maca = 1.30
else:
    preco_maca = 1.00

valor_total = Desejo * preco_maca


print()
print(f"valor total da compra R${valor_total:.2f}")


