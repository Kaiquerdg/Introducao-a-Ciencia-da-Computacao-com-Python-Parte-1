numero = int(input("Digite um numero natural positivo:"))

adjacente = True

while adjacente:
    resto = numero % 10
    inteiro = numero //10
    resto2 = inteiro % 10
    if numero <= 10:
        print("não")
        adjacente = False
    else:
        if numero > 10 and resto == resto2:
            print("sim")
            adjacente = False
        else:
            numero = numero // 10