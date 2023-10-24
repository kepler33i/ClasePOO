class Animal:
    def __init__(self, NombreAnimal):
        print(NombreAnimal, 'es un animal')

class Mamifero(Animal):
    def __init__(self, NombreMamifero):
        print(NombreMamifero, 'es un animal de sangre caliente')
        super().__init__(NombreMamifero)

class MamiferoNoAlado(Mamifero):
    def __init__(self, NombreMamiferoNoAlado):
        print(NombreMamiferoNoAlado, 'No puede volar')
        super().__init__(NombreMamiferoNoAlado)

class MamiferoNoMarino(Mamifero):
    def __init__(self, NombreMamiferoNoMarino):
        print(NombreMamiferoNoMarino, 'no puede nadar')
        super().__init__(NombreMamiferoNoMarino)        



class Perro(Mamifero):
    def __init__(self):
        print('El perro tiene 4 patas')
        super().__init__('Perro')

d1 = Perro()
print('')
murcielago = MamiferoNoMarino('Murcielago')
