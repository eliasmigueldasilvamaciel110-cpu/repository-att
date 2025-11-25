import random
num_secreto = random.randint(1, 10)

for i in range(3):
    palpite = int(input("Adivinhe o número (1 a 10): "))
    if palpite == num_secreto:
        print("Acertou!")
        break
    else:
        print("Errou!")
else:
    print("Você perdeu! O número era", num_secreto)
