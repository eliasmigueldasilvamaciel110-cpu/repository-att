a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if b == 0:
    print("Divisão por zero não é permitida.")
else:
    if a % b == 0:
        print(f"{a} é múltiplo de {b}")
    else:
        print(f"{a} não é múltiplo de {b}")
