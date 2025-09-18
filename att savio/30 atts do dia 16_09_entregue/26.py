n = float(input("Digite um número real: "))
parte_decimal = n -int(n)
parte_decimal_int = int(parte_decimal *10**len(str(parte_decimal).split('.')[1]))
if parte_decimal_int > n:
    print("A parte decimal é maior que a parte inteira.")
else:
    print("A parte decimal não é maior que a parte inteira.")