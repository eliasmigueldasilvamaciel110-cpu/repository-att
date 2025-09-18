n1 = float(input("Nota 1 (peso 2): "))
n2 = float(input("Nota 2 (peso 3): "))
n3 = float(input("Nota 3 (peso 5): "))

media = (n1*2 + n2*3 + n3*5) / 10

if media >= 7:
    print(f"Aprovado com média {media:.2f}")
elif media >= 5:
    print(f"Recuperação com média {media:.2f}")
else:
    print(f"Reprovado com média {media:.2f}")
