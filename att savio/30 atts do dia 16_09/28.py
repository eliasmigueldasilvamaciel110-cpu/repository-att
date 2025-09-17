# Leitura do caractere
caractere = input("Digite um caractere: ")

# Verificando o tipo do caractere
if 'A' <= caractere <= 'Z':
    print("É uma letra maiúscula.")
elif 'a' <= caractere <= 'z':
    print("É uma letra minúscula.")
elif '0' <= caractere <= '9':
    print("É um número.")
else:
    print("É um outro símbolo.")
