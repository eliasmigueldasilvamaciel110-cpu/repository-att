import random

num_secreto = random.randint(1, 50)

palpite = 0
while palpite != num_secreto:
    palpite = int(input("Adivinhe o número (1 a 50): "))

    if palpite < num_secreto:
        print("O número é maior.")
    elif palpite > num_secreto:
        print("O número é menor.")

print("Acertou!")
