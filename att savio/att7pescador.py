#pm = peso max 50kg ml = multa de 4 por kg a mais ex = excesso qtp = quantia a pagar 
pm = 50
ml = 4
px = int(input("quanto pesa seu peixe? "))
if px > pm:
    ex = px - pm
    qtp = ex * ml
    print(f"voce excedeu o peso maximo do peixe em {ex} kg sua multa e de {qtp} reais")