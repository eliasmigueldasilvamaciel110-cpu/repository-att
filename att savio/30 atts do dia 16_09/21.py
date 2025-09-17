import math
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
n1,n2,n3,n4  = (n1**0.5,n2**0.5,n3**0.5,n4**0.5)
if n1.is_integer():
    print(f"ah um quadrado perfeito e ele é {n1*n1} e sua raiz {n1}")
elif n2.is_integer():
    print(f"ah um quadrado perfeito e ele é {n2*n2} e sua raiz {n2}")
elif n3.is_integer():
    print(f"ah um quadrado perfeito e ele é {n3*n3} e sua raiz {n3}")
elif n4.is_integer():
    print(f"ah um quadrado perfeito e ele é {n4*n4} e sua raiz {n4}")
else:
    print("n há número quadrado")
    print(f"porem essas são suas raízes: {n1:.2f}, {n2:.2f}, {n3:.2f}, {n4:.2f}")