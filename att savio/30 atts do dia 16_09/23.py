numero = input("Digite um número de 5 dígitos: ")

if numero == numero[::-1]:
    print(f"O número {numero} é um palíndromo.")
else:
    print(f"O número {numero} não é um palíndromo.")
