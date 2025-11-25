print("Números primos de 1 a 100:")
for num in range(2, 101):
    cont = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        print(num)
