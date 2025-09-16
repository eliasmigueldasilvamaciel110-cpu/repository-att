ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = 2025  # Atualize conforme necessário
idade = ano_atual - ano_nasc
if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")
