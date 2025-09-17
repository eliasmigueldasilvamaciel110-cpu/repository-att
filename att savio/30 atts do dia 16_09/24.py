h=int(input("me de um horario(em horas) "))
m=int(input("me de um horario em minutos "))
s=int(input("me de um horario em segundos "))
h=h*60*60
m=m*60
maior = max(h,m,s)
h=h/60/60
m=m/60
print(f"o maior valor em segudos é{maior}")