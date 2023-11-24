def remove_repetidos(lista):
    lista.sort()
    sem_repetidos = []
    for x in lista:
        if x not in sem_repetidos:
            sem_repetidos.append(x)
    return sem_repetidos