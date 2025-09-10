#slb = salario bruto dh = dinheiro hr ht = hrs trabalhadas no mes imp = imposto de renda inss = inss sin = sindicato #sll = salario liquido
#mostrar o salario bruto o inss o sindicato e o liquido
dh = float(input("quanto você ganha por hrs? "))
ht = float(input("quantas hrs por mes você trabalha? "))
ht * dh
slb = dh * ht
imp = slb * 0.11
inss = slb * 0.08
sin = slb * 0.05
sll = slb - sin - inss - imp
sll = int(sll)
print(f"salario bruto:{slb},valor pago de sindicato:{sin},valor pago de inss:{inss},salario liquido:{sll}")
