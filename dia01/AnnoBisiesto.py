def Negativo(numero):
    if int(numero)<1:
        return True
    else:
        return False
def excepcion(anno):
    try:
        Num=int(anno)
        return True
    except:
        print('Ocurrio un error')
        return False  
def Bisiesto(anno):

    num=int(anno)
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        return True
    else:
        return False



print('El programa determina si el anno ingresado es bisiesto')
ano = (input('Ingrese un ano: '))


while excepcion(ano)==False:
    print(ano,' no es un numero o es un decimal')
    ano = (input('Ingrese un ano: '))

while Negativo(ano)==True:
    print(ano,' debe ser un numero positivo')
    ano = (input('Ingrese un ano: '))    

if Bisiesto(ano)==True:
    print(Bisiesto(ano),' el anno ',ano,' es bisiesto')
else:
    print(Bisiesto(ano),' el anno ',ano,' no es bisiesto')