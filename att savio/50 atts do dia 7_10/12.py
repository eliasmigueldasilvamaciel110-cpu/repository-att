soma = 0
numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    print(f"Você digitou {numero}")
    soma += numero
    numero = int(input("Digite outro número (0 para parar): "))
    
print(f"A soma de numeros{soma}.")
