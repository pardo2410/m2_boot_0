lista = [1,3,-1,15,9,4]

#map permite que una funcion actue sobre cada uno de los valores simplificando el proceso
listaDobles = map(lambda x: x*2, lista)
print(list(listaDobles))

#filter se usa para filtrar segun la condicion definida, en este caso solo se imprimira los valores pares 

#utilizando una funcion anonima lambda
listaPares = filter(lambda x: x % 2 == 0,lista)
print(list(listaPares))

#escrita utilizando una funcion general
def esImpar(x):
    return x % 2 != 0

listaImpares=filter(esImpar,lista)
print(list(listaImpares))

#reduce suma todos los valores de una lista o vector y da como resultado un unico valor
from functools import reduce

sumatoria = reduce(lambda x, y: x + y , lista)
print(sumatoria)
print('media ',sumatoria/len(lista))

suma100 = reduce(lambda x,y: x + y,range(101))
print(suma100)



def productoTotal(x):
    resultado = 1
    for valor in x:
        resultado *= valor
    return resultado
prodTotal = productoTotal(lista)
print(prodTotal)