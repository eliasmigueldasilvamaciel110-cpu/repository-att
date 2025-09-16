n = int(input("Digite um número inteiro: "))
if n == 0:
    print("Zero (nem positivo nem negativo)")
else:
    if n % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"
    if n > 0:
        sinal = "positivo"
    else:
        sinal = "negativo"
    print(f"O número é {paridade} e {sinal}.")
