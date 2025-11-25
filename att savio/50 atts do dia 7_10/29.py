print("Números perfeitos entre 1 e 1000:")

for num in range(1, 1001):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if soma == num:
        print(num)
