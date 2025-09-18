h1 = int(input("Hora do 1 horário: "))
m1 = int(input("Minuto do 1 horário: "))
h2 = int(input("Hora do 2 horário: "))
m2 = int(input("Minuto do 2 horário: "))

if h1 < h2 or (h1 == h2 and m1 < m2):
    print("O 1 horário acontece primeiro")
elif h1 == h2 and m1 == m2:
    print("Os horários são iguais")
else:
    print("O 2 horário acontece primeiro")
