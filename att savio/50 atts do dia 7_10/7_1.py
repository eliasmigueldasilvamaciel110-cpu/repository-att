numeros = []
i = 0

while i < 5:
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)
    i += 1  # aumenta o contador

media = sum(numeros) / 5
print("A média dos números é:", media)
