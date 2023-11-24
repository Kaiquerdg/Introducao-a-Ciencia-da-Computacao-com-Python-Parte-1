x = int(input("Digite a largura do retângulo: "))
y = int(input("Digite a altura do retângulo: "))


i = 1
j = 1
while i <= y:
    while j <= x:
        if i == 1 or i == y or j == 1 or j == x:
            print("#", end = "")
        else:
            print(" ", end = "")
        j = j + 1
    print("")
    i = i + 1
    j = 1