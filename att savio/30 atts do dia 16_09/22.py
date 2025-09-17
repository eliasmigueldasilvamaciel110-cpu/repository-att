# Leitura dos pontos
x1, y1 = map(int, input("Digite as coordenadas do ponto 1 (x1 y1): ").split())
x2, y2 = map(int, input("Digite as coordenadas do ponto 2 (x2 y2): ").split())
x3, y3 = map(int, input("Digite as coordenadas do ponto 3 (x3 y3): ").split())

# Fórmula para calcular a área do triângulo
area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

# Verificar se os pontos estão alinhados
if area == 0:
    print("Os pontos estão alinhados.")
else:
    print("Os pontos não estão alinhados.")
