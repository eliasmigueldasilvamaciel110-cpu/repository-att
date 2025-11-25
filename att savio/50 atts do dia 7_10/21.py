alunos = 0
notad = 0
while alunos <= 10:
    nota = float(input("Digite a nota do aluno (entre 0 e 10): "))
    if 0 <= nota <= 10:
        alunos += 1
        notad += nota
    else:
        print("Nota inválida. Tente novamente.")
media = notad / 10
print(f"A média da turma é: {media}")