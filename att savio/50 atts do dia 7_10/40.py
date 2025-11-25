while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    print("Binário:", bin(num)[2:])
    print("Octal:", oct(num)[2:])
    print("Hexadecimal:", hex(num)[2:])
