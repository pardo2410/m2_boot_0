def retrocontador(e):
    print('{},'.format(e),end='')
    if e>0:
        retrocontador(e-1)
def sumatoria(e):
    if e > 0:
        return e + sumatoria(e-1)
    else:
        return 0
def factorial(e):
    if e > 0:
        return e * factorial(e-1)
    else:
        return 1

entrada=int(input('ingrese valor  de retrocontador: '))
retrocontador(entrada)
print(sumatoria(entrada))