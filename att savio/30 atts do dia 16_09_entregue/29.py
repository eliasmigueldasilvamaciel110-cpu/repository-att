# Leitura da nota e faltas
nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite a quantidade de faltas: "))

# Classificação
if nota >= 7 and faltas <= 10:
    print("Aprovado")
elif nota >= 5 and faltas <= 10:
    print("Recuperação")
else:
    print("Reprovado")
