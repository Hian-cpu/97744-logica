import os

os.system("clear") 

primeiro_numero = float(input("Digite o Primeiro Número:"))
segundo_numero = float(input("Digite o Segundo Número:"))


soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) / 2


maior_numero = max(primeiro_numero, segundo_numero)
menor_numero = min(primeiro_numero, segundo_numero)

print()
print(f"soma: {soma}")
print(f"produto:{produto}")
print(f"media:{media}")

if primeiro_numero == segundo_numero:
    print(f"os números são iguais")
else:
    print(f"maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")