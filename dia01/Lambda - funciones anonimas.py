#landas - importar funciones desde otro fichero
from SumaTodoLambda import sumaTodos2 

valor=int(input('Ingrese el valor: '))
print('Suma todos los cubos hasta el numero ',valor,' el resultado es: ' ,sumaTodos2(valor,lambda x: x**3))
print('Suma todos los valores por 3 hasta el numero ',valor,' el resultado es: ' ,sumaTodos2(valor,lambda x: x*3))
print('Suma todos los valores por 2 hasta el numero ',valor,' el resultado es: ' ,sumaTodos2(valor,lambda x: x*2))
