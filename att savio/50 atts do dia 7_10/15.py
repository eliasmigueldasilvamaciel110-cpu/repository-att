contador = 0
numero = int(input("Digite um número (negativo para parar): "))

while numero >= 0:
    print(f"Você digitou {numero}")
    contador += 1
    numero = int(input("Digite outro número (negativo para parar): "))
    
print(f"A quantidade de numeros q vc digitou { contador}")


