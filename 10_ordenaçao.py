inteiro1 = int(input("Digite o primeiro numero inteiro:"))
inteiro2 = int(input("Digite o segundo numero inteiro:"))
inteiro3 = int(input("Digite o terceiro numero inteiro:"))

if inteiro1 < inteiro2 and inteiro2 < inteiro3:
    print("crescente")
else:
    print("nao está em ordem crescente")