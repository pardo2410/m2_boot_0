def sumaTodos(limit):
    
    resultado=0
    for i in range(0,limit + 1):
        resultado += i
    return resultado

def sumaTodosLosCuadrados(limit):
    resultado=0
    for i in range(limit+1):
        resultado += i*i
    return resultado

def sumaTodosLosCubos(limit):
    resultado=0
    for i in range(limit+1):
        resultado += i**3
    return resultado

def sumaTodos2(limit,f):
    resultado=0
    for i in range(limit+1):
        resultado+=f(i)
    return resultado