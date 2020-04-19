import sys #libreria de consola

def area(base,altura):
    
    return base*altura/2

print (len(sys.argv)) # mensaje en consola

if __name__=='__main__':
    b=float(input('Base: '))
    h=float(input('Altura: '))
    print(area(b,h))

for item in sys.argv:
    print(item)