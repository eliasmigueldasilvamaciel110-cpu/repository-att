notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]

notas.remove(max(notas))
notas.remove(min(notas))

media = sum(notas) / 2 #soma = sum #soma as notas restantes e divide por 2

if media >= 7:
    print(f"Aprovado com média {media:.2f}")
elif media >= 5:
    print(f"Recuperação com média {media:.2f}")
else:
    print(f"Reprovado com média {media:.2f}")
#.2f serve para mostrar so 2 casas decimais