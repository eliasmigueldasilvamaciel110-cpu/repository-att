a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a + b > c and a + c > b and b + c > a:#Verifica se os lados podem formar um triângulo usando a regra a soma de dois lados deve ser maior que o terceiro para todos os lados
    if a == b == c:
        print("Triângulo Equilátero")#todos os lados iguais
    elif a == b or b == c or a == c:
        print("Triângulo Isósceles")#dois lados iguais
    else:
        print("Triângulo Escaleno")#todos os lados diferentes
else:
    print("Não formam triângulo")
