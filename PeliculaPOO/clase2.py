class Pelicula:
    def __init__(self, titulo, categoria, año) -> None:
        self.titulo = titulo
        self.categoria = categoria
        self.a = año
        print('Se ha creado la pelicula', titulo, self.a)

    def __str__(self) -> str:
        return '´{} ({})'.format(self.titulo, self.a)
    
p = Pelicula('El Exorcista', 'Terror', 1973)


class Catalogo:
    
    peliculas = []  #Lista que contiene las peliculas del catalogo

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  #p será un objeto pelicula
        self.peliculas.append(p) 

    def mostrar(self):
        for p in self.peliculas:
            print(p)  #print toma por defecto str(p)

p = Pelicula('-> El Exorcista', 'Terror', 1973)
c = Catalogo([p])


c.mostrar()
c.agregar(Pelicula('El exorcista - Parte 2', 'Terror', 2022))
c.mostrar()