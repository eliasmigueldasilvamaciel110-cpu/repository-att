n = 10  
a, b = 0, 1

print("Sequência de Fibonacci até o 10º termo:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
