def isAnagramEle(p1,p2):
   
    
    if len(p1)==len(p2):
        listaComparacionLetras=[]    
        for caracter1 in p1:
            haPasadoPorAqui=False
            for caracter2 in p2:
                if caracter1==caracter2:
                    haPasadoPorAqui=True
                    listaComparacionLetras.append(True)
                    
            if not haPasadoPorAqui: 
                listaComparacionLetras.append(False)
        
        if False in listaComparacionLetras:
            print('No es un anagrama')
            return False
        else:
            print('Es un anagrama')
            return True
    else:
            print('Las palabras no tienen las misma longitud')
def isAnagram(p1,p2):
    return isAnagramEle(p1,p2) and isAnagramEle(p2,p1)
    

print('El programa solicita dos palabras y valida si es un anagrama')
a=input('ingrese primera palabra: ')
b=input('ingrese segunda palabra: ')
isAnagramEle(a,b)


