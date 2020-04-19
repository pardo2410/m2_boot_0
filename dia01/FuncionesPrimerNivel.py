def normal(x):
    return x
def cuadrado(x):
    return x * x

def Sumatodo(limit,f):
    resultado=0
    for i in range (limit+1):
        resultado += f(i)
    return resultado


print('Funciones de nivel superior prueba')
num=int(input('ingrese un numero '))
print(Sumatodo(num,normal))
print(Sumatodo(num,cuadrado))