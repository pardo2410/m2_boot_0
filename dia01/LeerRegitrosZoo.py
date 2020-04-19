fEntradas = open('transacciones.txt','r')
todas=fEntradas.readlines()
for transaccion in todas:
    print(transaccion)