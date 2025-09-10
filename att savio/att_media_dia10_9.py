a = int(input("digite a primeira nota: "))
b = int(input("digite a primeira nota: "))
c = int(input("digite a primeira nota: "))
media = (a + b + c) / 3
print(f"A média é: {media}")
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")