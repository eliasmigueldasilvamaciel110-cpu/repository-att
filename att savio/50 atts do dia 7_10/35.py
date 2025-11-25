votosA = 0
votosB = 0
votosC = 0

while True:
    voto = input("Vote em A, B ou C (ou 'fim' para encerrar): ").lower()

    if voto == "fim":
        break
    elif voto == "a":
        votosA += 1
    elif voto == "b":
        votosB += 1
    elif voto == "c":
        votosC += 1
    else:
        print("Voto inválido!")
print("\nResultado da votação:")# Mostra o total de votos
print(f"A: {votosA} votos")
print(f"B: {votosB} votos")
print(f"C: {votosC} votos")
if votosA > votosB and votosA > votosC:# Determina o vencedor
    print("Vencedor: Candidato A")
elif votosB > votosA and votosB > votosC:
    print("Vencedor: Candidato B")
elif votosC > votosA and votosC > votosB:
    print("Vencedor: Candidato C")
else:
    print("Empate!")
