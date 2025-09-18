# Leitura de idade e tempo de contribuição
idade = int(input("Digite sua idade: "))
tempo_contribuicao = int(input("Digite seu tempo de contribuição (em anos): "))

# Verificação da possibilidade de aposentadoria
if idade >= 65 or tempo_contribuicao >= 35:
    print("Você pode se aposentar!")
else:
    print("Você não pode se aposentar ainda.")
