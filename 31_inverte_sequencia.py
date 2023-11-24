lista = []
x = int(input("Digite um número: "))

while x != 0:
    lista.append(x)
    y = int(input("Digite um número: "))
    x = y

lista_invertida = []

for n in range(len(lista), 0, -1):
    lista_invertida.append(lista[n - 1])

for w in lista_invertida:
    print(w)