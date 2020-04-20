# Valor Maximo
def maxi(l): #*l es una lista
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1,len(l)):
        if l[ix] > m:
            m = l[ix]
    return m
# Valor Minimo
def mini(l): #*l es una lista
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1,len(l)):
        if l[ix] < m:
            m = l[ix]
    return m
# Calculo de la media
def media(l): #*l es una lista
    if len(l) == 0:
        return 0
    suma = 0
    for valor in l:
        suma += valor
    return suma/len(l)

lista = []
num=1
while num != 0:
   num=int(input('ingrese un valor y para finalizar ponga cero: '))
   lista.append(num)

lista.remove(0)

print('-----------Resultados-----------')
print('La lista de valores es la siguiente: ',lista)
print('El numero de elementos ingresados es de: ',len(lista))
print('El valor Maximo es: ',maxi(lista))   
print('El valor minimo es: ',mini(lista))
print('La media de los valores es: ',media(lista))