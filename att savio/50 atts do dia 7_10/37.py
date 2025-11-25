total = 0
while True:
    preco = float(input("Digite o preço do produto (ou 0 para encerrar): "))
    if preco == 0:
        break
    total += preco

print(f"\nTotal da compra: R$ {total:.2f}")
