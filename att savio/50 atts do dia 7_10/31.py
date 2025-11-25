preco = 1.50
total = 0

while True:
    qtd = int(input("Quantos doces você quer comprar? "))
    total += qtd * preco
    continuar = input("Deseja continuar comprando? (sim/não): ").lower()

    if continuar == "não":
        break

print(f"\nTotal final da compra: R$ {total:.2f}") #nota o n/ serve para descer pra linha de baixo a resposta
