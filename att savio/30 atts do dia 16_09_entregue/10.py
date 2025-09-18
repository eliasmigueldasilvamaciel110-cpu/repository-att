altura = float(input("Digite a altura (m): "))
peso = float(input("Digite o peso (kg): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
