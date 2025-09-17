# Leitura do número real
numero = float(input("Digite um número real: "))

# Separando parte inteira e decimal
parte_inteira = int(numero)
parte_decimal = numero - parte_inteira

# Verificando se a parte decimal é maior que a parte inteira
if parte_decimal > parte_inteira:
    print("A parte decimal é maior que a parte inteira.")
else:
    print("A parte decimal não é maior que a parte inteira.")
