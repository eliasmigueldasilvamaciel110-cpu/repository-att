ch = input("Digite um caractere: ")
if ch.isalpha():
    if ch.lower() in 'aeiou':#if ch.lower() in 'aeiou'Converte o caractere para minúsculo e verifica se está entre as vogais
        print("Vogal")
    else:
        print("Consoante")
elif ch.isdigit():#Se não for letra, verifica se é um número.
    print("Número")
else:
    print("Símbolo")
