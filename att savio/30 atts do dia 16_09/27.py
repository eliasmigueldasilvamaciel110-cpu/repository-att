# Leitura dos lados
a = float(input("Digite o comprimento do lado a: "))
b = float(input("Digite o comprimento do lado b: "))
c = float(input("Digite o comprimento do lado c: "))

# Verificando se os lados formam um triângulo
if a + b > c and a + c > b and b + c > a:
    # Classificação do triângulo
    if a == b == c:
        print("O triângulo é Equilátero.")
    elif a == b or a == c or b == c:
        print("O triângulo é Isósceles.")
    else:
        print("O triângulo é Escaleno.")
    
    # Verificando se é um triângulo retângulo
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("O triângulo é Retângulo.")
else:
    print("Os valores não formam um triângulo.")
