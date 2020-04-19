def imprimeCosas(*listadecosas):
    for item in listadecosas:
        print(item)
def imprimecondiccionario(**diccionariodeparametros):
    if 'line' in diccionariodeparametros:
        print('Posicionar en linea',diccionariodeparametros['line'])
    else:
        print('No hay line')


imprimeCosas('cosa2','cosa1','cosa3','cosa4')
imprimecondiccionario(contenido='la cosa',column=5)