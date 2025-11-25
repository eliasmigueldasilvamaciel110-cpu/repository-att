soma_notas = 0
soma_pesos = 0

for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    peso = float(input(f"Digite o peso {i+1}: "))
    soma_notas += nota * peso
    soma_pesos += peso

media_ponderada = soma_notas / soma_pesos

print(f"\nA média ponderada é: {media_ponderada:.2f}")
