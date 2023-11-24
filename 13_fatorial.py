numero = int(input("Digite um numero natural positivo:"))

produto = 1

while numero > 1:
    produto = produto * numero
    numero = numero - 1

print(produto)