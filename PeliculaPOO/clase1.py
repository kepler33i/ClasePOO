class Pelicula:
    def __init__(self, titulo, categoria, año) -> None:
        self.titulo = titulo
        self.categoria = categoria
        self.a = año
        print('Se ha creado la pelicula', titulo, self.a)

    def __init__(self, titulo=None, categoria=None, año=None):
        self.titulo = titulo
        self.categoria = categoria
        self.a = año
        print('Se ha creado la pelicula', titulo, self.a)

    def __del__(self):
        print('Se destruye la pelicula', self.titulo)

    def __len__(self):
        return self.a
    
p = Pelicula('Ready player one', 'Ciencia Ficcion', 2018)
pp = Pelicula()
print(len(p))
#print(len(pp))