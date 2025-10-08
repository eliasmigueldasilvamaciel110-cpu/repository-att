pares = impares = 0
for i in range(10):
    n=int(input("digite um número: "))
    impares += n % 2 != 0
    pares += n % 2 == 0
print(f"Você digitou {pares} números pares e {impares} números ímpares.")