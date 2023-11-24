inteiro = int(input("Digite um numero inteiro:"))

div = inteiro % 5
div2 = inteiro % 3

if div == 0 and div2 == 0:
    print("FizzBuzz")
else:
    print(inteiro)