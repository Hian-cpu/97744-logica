import os
os.system("clear")
          
primeiro_numero = float(input("Digite o primeiro Número:"))
segundo_numero = float(input("Digite o Segundo Número:"))
terceiro_numero = float(input("Digite o Terceiro Número:"))


maior_numero = max(primeiro_numero, segundo_numero, terceiro_numero)
menor_numero = min(primeiro_numero, segundo_numero, terceiro_numero)


print(f"Primeiro Número:{primeiro_numero:}")
print(f"Segundo Número: {segundo_numero:}")
print(f"Terceiro Número:{terceiro_numero:}")
print()
print(f"menor_numero:{menor_numero}")
print(f"maior_numero:{maior_numero}")
