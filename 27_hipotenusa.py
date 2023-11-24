import math

def é_hipotenusa(i, j):
    hip = math.sqrt(i**2 + j**2)
    return hip

def soma_hipotenusas(h):
    x = 1
    soma = 0
    while x <= h:
        i = 1
        j = 1
        while i < h:
            while j < h:
                if x == é_hipotenusa(i, j):
                    soma = soma + x
                    i = h
                j = j + 1
            i = i + 1
            j = i
        x = x + 1
    return soma                  
    