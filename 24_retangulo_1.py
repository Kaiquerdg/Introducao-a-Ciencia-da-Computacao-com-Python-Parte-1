x = int(input("Digite a largura do retângulo: "))
y = int(input("Digite a altura do retângulo: "))

i = 1
j = 1
while i <= y:
    while j <= x:
        print("#", end = "")
        j = j + 1
    print("")
    i = i + 1
    j = 1