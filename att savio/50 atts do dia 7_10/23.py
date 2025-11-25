valor = int(input("Digite o valor para saque: "))

n100 = valor // 100
valor %= 100

n50 = valor // 50
valor %= 50

n20 = valor // 20
valor %= 20

n10 = valor // 10
valor %= 10

n5 = valor // 5
valor %= 5

print("\nNotas necessárias:")
print(f"100: {n100}")
print(f"50: {n50}")
print(f"20: {n20}")
print(f"10: {n10}")
print(f"5: {n5}")
