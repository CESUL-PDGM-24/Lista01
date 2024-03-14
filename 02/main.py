from functions import *

height = 0
elevation = 0

points = []
while height != -1:
    height = float(input("Informe a altitude do ponto (-1 para encerrar): "))

    if height != -1:
        points.append(height)

elevation = calculate_elevation(points)

print(f"O ganho de elevação no percurso foi de {elevation:.1f} metros")
