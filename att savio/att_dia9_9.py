#receber 2 valores inteiros a,b printar a e b , trocar os valores e printar novamente
a = int(input("fala ai um valor "))
b = int(input("fala ai outro valor batola "))
print(f"antes de trocar os valores:A={a} e B={b}")
a, b = b, a
print(f"depois de trocar los valores A={a}e B={b}")
