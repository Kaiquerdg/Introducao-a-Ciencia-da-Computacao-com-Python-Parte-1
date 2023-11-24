x1 = float(input("Digite o primeiro numero:"))
y1 = float(input("Digite o segundo numero:"))
x2 = float(input("Digite o terceiro numero:"))
y2 = float(input("Digite o quarto numero:"))

import math

distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")