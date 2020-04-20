#Prueba con atributos vacios y None
class Dog():
    def __init__(self):
        self.nombre =''
        self.edad = None
        self.peso = None
    def ladrar(self):
        if self.peso==None:
            print('No hay perro')
        if self.peso >= 8:
            print(' Guau, Guau ')
        else:
            print(' guau, guau ')    

class Perro():
#asignacion de atributos de la clase
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    def ladrar(self):
        if self.peso >= 8:
            print(' Guau, Guau ')
        else:
            print(' guau, guau ')
#Con esta linea se traduce los codigos a texto
    def __str__(self):
        return 'Soy el perro {}'.format(self.nombre,self.edad,self.peso)
#creacion de una sub clase
class PerroAsistencia(Perro): 
    def __init__(self, nombre, edad, peso,amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo=amo
        self.trabajando = False
    def __str__(self):
        return 'Soy el perro {} de asistencia'.format(self.nombre,self.edad,self.peso,self.amo)
    def pasear(self):
        return '{}, ayudo a mi propietario, {} a pasear'.format(self.nombre,self.amo)
    def ladrar(self):
        if self.trabajando:
            print('shhh, no puedo ladrar')
        else:
            Perro.ladrar(self)
    def trabajando(self,valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor