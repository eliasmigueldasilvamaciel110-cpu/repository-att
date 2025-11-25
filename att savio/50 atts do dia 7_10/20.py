
num = int(input("Digite um número: "))

print(f"Os divisores de {num} são:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
