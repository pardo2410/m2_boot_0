def sumaTodos(limit):
    i=0
    resultado=0
    for i in range(0,limit + 1):
        resultado += 1
    return resultado

print(sumaTodos(100))