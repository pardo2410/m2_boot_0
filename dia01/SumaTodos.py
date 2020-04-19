def sumaTodos(limit):
    
    resultado=0
    for i in range(0,limit + 1):
        resultado += i
    return resultado

Num=int(input('ingrese un numero '))
print(sumaTodos(Num))