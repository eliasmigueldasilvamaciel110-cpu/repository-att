# Função para converter um horário em segundos
def horario_para_segundos(hora, minuto, segundo):
    return hora * 3600 + minuto * 60 + segundo

# Leitura dos dois horários
hora1, minuto1, segundo1 = map(int, input("Digite o primeiro horário (hora minuto segundo): ").split())
hora2, minuto2, segundo2 = map(int, input("Digite o segundo horário (hora minuto segundo): ").split())

# Cálculo do tempo em segundos
tempo1 = horario_para_segundos(hora1, minuto1, segundo1)
tempo2 = horario_para_segundos(hora2, minuto2, segundo2)

# Comparação e exibição do maior tempo
if tempo1 > tempo2:
    print(f"O primeiro horário é maior com {tempo1} segundos.")
else:
    print(f"O segundo horário é maior com {tempo2} segundos.")
