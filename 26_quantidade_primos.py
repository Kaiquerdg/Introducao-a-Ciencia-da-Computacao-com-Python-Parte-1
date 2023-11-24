def éPrimo(k):
    naturais = 2
    primo = True

    while naturais < k and primo:
        primo = ((k % naturais) != 0)
        naturais = naturais + 1
    
    if k > 1 and primo:
        return True
    elif k < 1:
        print("O menor número primo é o 2. Digite um número maior ou igual a ele")
    else:
        return False

def n_primos(x):
    p = 0
    while x > 0:
        if éPrimo(x) == True:
            p = p + 1
            x = x - 1
        else:
            x = x - 1
    return(p)
    