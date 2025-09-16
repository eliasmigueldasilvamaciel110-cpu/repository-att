dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
if mes < 1 or mes > 12:
    valido = False
elif dia < 1:
    valido = False
else:
    if mes in [1,3,5,7,8,10,12]:
        valido = dia <= 31
    elif mes in [4,6,9,11]:
        valido = dia <= 30
print("Data válida" if valido else "Data inválida")
