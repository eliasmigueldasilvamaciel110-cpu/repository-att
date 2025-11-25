palavra = input("Digite uma palavra: ").lower()  # converte pra minúsculas(anotando pois sei que vou esquecer)
vogais = "aeiou"
cont = 0

for letra in palavra:
    if letra in vogais:
        cont += 1

print(f"A palavra '{palavra}' tem {cont} vogais.")
