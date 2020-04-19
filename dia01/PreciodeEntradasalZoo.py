def esNegativo(numero):
    if int(numero)<0:
        return True
    else:
        return False
    
def esEntero(numero):
    try:
        num=int(numero)
        return True
    except:
        return False

def precioZoo(edad):
    
    baby=0
    menores=0
    resto=0
    jubilados=0
    
    while edad != 0:
        if edad <= 2:
            baby+=1
        elif edad >2 and edad <= 12:
            menores+=1
        elif edad>12 and edad<65:
            resto+=1
        else:
            jubilados+=1
        edad=(input('Ingrese su edad: '))
        

        while not esEntero(edad):
            print(edad," debe ser un numero entero")
            edad=input('Ingrese su edad: ')
        
        while esNegativo(edad)==True:
            print(edad," debe ser un numero positivo")
            edad=input('Ingrese su edad: ')
        
        edad=int(edad)


       
    
    Totbaby=baby*0
    Totmenores=menores*14
    Totresto=resto*23
    Totjubilados=jubilados*18
    TotGeneral=baby+menores+resto+jubilados
    PrecioTot=Totbaby+Totmenores+Totresto+Totjubilados
    
    print('-------------------- Total a Pagar Zoo ----------------------\n {} entradas de baby ($0): ${:.2f}\n {} entradas de menores ($14): ${:.2f}\n {} entradas normales ($23): ${:.2f}\n {} entradas de jubilados ($18): ${:.2f}\n -------------------------------------------------------------\n {} Total entradas: ${:.2f}\n '.format(baby,Totbaby,menores,Totmenores,resto,Totresto,jubilados,Totjubilados,TotGeneral,PrecioTot))            
   
#Las siguientes tres lineas del programa guarda la informacion impresa en consola en el fichero txt (transacciones.txt) 
    fEntradas = open('transacciones.txt','a+')
    transaccion = ('-------------------- Total a Pagar Zoo ----------------------\n {} entradas de baby ($0): ${:.2f}\n {} entradas de menores ($14): ${:.2f}\n {} entradas normales ($23): ${:.2f}\n {} entradas de jubilados ($18): ${:.2f}\n -------------------------------------------------------------\n {} Total entradas: ${:.2f}\n'.format(baby,Totbaby,menores,Totmenores,resto,Totresto,jubilados,Totjubilados,TotGeneral,PrecioTot))            
    fEntradas.write(transaccion)
    fEntradas.close()
    
print(' Bienvenido al Zoo\n Ingrese su edad y la de sus acompañantes, para conocer el total a pagar por su visita.\n para finalizar ingrese 0 y Enter.')
Edad=input('Ingrese su edad: ')
    
while not esEntero(Edad):
    print(Edad," debe ser un numero entero")
    Edad=input('Ingrese su edad: ')

while esNegativo(Edad)==True:
    print(Edad," debe ser un numero positivo")
    Edad=input('Ingrese su edad: ')

precioZoo(int(Edad))

