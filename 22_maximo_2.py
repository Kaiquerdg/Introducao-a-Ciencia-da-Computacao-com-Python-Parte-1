def maximo(x,y,z):
    if x > y > z:
        return x
    elif x > z > y:
        return x
    elif y > x > z:
        return y
    elif y > z > x:
        return y
    elif z > x > y:
        return z
    else:
        return z