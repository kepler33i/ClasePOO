from AlimentoPOO.producto import *

class Cosa(Producto):
    precio = ''

    def __str__(self):
        return '''
        Nombre \t{}
        Precio \t{}
        '''.format(self.nombre, self.precio)
    
stuff = Cosa('A-004', 'Cualquiera', 'Cosa', 'SKU-asd', 'Una cosa lala')
stuff.precio = 100

#Para crear una copia 100% nueva debemos utilizar el modulo copy
import copy
copia_cosa =copy.copy(stuff)
print(copia_cosa)

copia_cosa.precio = 200
print(copia_cosa)
print(stuff)



def rebaja_productos(p, rebaja):
    #Rebaja del precio de un producto segun porcentaje
    p.precio = p.precio - (p.precio/100 * rebaja)


rebaja_productos(stuff, 10)
print(stuff)
rebaja_productos(stuff, 10)
print(stuff)

print('Creacion de una copia '
      )

copia_de_objeto = food
copia_de_objeto.referencia = 'A-002'
print('\nObjeto copiado\n', copia_de_objeto)
print('\nObjeto original\n', food)


def rebajar_producto(p, rebaja):
    p.precio = p.precio -(p.precio/100 * rebaja)
    print(p.precio)

