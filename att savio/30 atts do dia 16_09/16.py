a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

# Verifica se os lados formam um triângulo
if a + b > c and a + c > b and b + c > a:
    # Verifica se é retângulo (usando Teorema de Pitágoras)
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Formam triângulo retângulo")
    else:
        print("Formam triângulo, mas não retângulo")
else:
    print("Não formam triângulo")
