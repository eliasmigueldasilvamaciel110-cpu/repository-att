mes = int(input("Digite um número de 1 a 12: "))
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= mes <= 12:
    print(f"Mês: {meses[mes - 1]}")#[mes - 1]pq aparentemente a lista começa do 0 no py
else:
    print("Mês inválido")
