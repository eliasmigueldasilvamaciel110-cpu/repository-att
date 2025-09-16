n = int(input("Digite um número inteiro (maior q um): "))

if n <= 1:
    print("Não é primo")
else:
    raiz = int(n**0.5)
    if raiz < 2:
        print("É primo")  # 2 ou 3
    elif n % 2 == 0:
        print("Não é primo")
    elif raiz == 2 and n % 3 == 0:
        print("Não é primo")
    else:
        print("É primo")
