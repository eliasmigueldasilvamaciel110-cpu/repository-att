def calcular_fatorial_iterativo(numero):
  resultado = 1
  if numero == 0 or numero == 1:
    return 1
  else:
    for i in range(1, numero + 1):
      resultado *= i
    return resultado
num = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {num} é {calcular_fatorial_iterativo(num)}")
