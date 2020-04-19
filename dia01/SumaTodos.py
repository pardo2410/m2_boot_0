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


Num=int(input('ingrese un numero '))
print('Suma Todo ',sumaTodos(Num))
print('SumaTodos los Cuadrados ',sumaTodosLosCuadrados(Num))