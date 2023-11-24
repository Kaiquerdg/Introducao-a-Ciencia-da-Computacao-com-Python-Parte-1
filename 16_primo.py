numero = int(input("Digite um numero natural positivo:"))

naturais = 2
primo = True

while naturais < numero and primo:
    primo = ((numero % naturais) != 0)
    naturais = naturais + 1
    
if numero > 1 and primo:
    print("primo")
else:
    print("não primo")