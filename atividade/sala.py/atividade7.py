import os

os.system("clear")

primeiro_numero = float(input("Digite o Primeiro Número:"))
operacao = input("Digite a operaçao:")
segundo_numero =float(input("Digite o segundo_numero:"))

# 3 - verificando dados.
match operacao:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero
    case"_":
        print("opção inválida.")




print()
print(f"Primeiro número : {primeiro_numero}")
print(f"segundo número : {segundo_numero}")
print(f"resultado: {resultado}")


