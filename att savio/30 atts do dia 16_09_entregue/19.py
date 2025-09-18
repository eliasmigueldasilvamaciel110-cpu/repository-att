h = int(input("Hora: "))
m = int(input("Minuto: "))

if 8 <= h < 18:
    print("Está no horário comercial")
elif h == 18 and m == 0:
    print("Está no horário comercial")
else:
    print("Não está no horário comercial")
