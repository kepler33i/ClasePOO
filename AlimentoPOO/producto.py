class Producto:
    #Estructura para los productos de una tienda (ejemplo sin herencia)
    def __init__(self, referencia, tipo, nombre, sku, descripcion, productor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.sku = sku
        self.descripcion = descripcion
        self.productor = productor
        self.isbn = isbn
        self.autor = autor


    def __str__(self):
        return '''
        REFERENCIA\t{}
        NOMBRE\t\t{}
        TIPO\t\t{}
        SKU\t\t{}
        DESCRIPCION\t{}
        '''.format(self.referencia, self.tipo, self.nombre, self.sku, self.descripcion)
    
#Subclase Alimento
class Alimento(Producto):
    productores = ''
    distribuidor = ''

    def __str__(self):
        return '''
        REFERENCIA\t{}
        NOMBRE\t\t{}
        TIPO\t\t{}
        SKU\t\t{}
        DESCRIPCION\t{}
        PRODUCTOR\t{}
        DESTRIBUIDOR\t{}
        '''.format(self.referencia, self.tipo, self.nombre, self.sku, self.descripcion, self.productores, self.distribuidor)

#Subclase Libro    
class Libro(Producto):
    isbn = ''
    autor = ''


    
    def __str__(self):
        return '''
        REFERENCIA\t{}
        NOMBRE\t\t{}
        SKU\t\t{}
        DESCRIPCION\t{}
        ISBN\t\t{}
        AUTOR\t\t{}
        '''.format(self.referencia, self.nombre, self.sku, self.descripcion, self.isbn, self.autor)

class Adorno(Producto):
    pass

a = Producto('A-001', 'Adorno', 'Vaso', '15', 'SKU 1010', 'Vaso de vidrio')
print(a)

food = Alimento('A-002', 'Perecible', 'Leche cultivada', 'SKU-2020', 'Leche cultivada chirimoya', 'asd')
food.productores = 'Vaquita Feliz'
food.distribuidor = 'Inacap Eats'
print(food)

book = Libro('A-003', 'Programacion', 'Master Crack POO', 'SKU-0101', 'Codigos Piolas', 'Pepe Objeto OLA', 'LALALA')
book.isbn = '1999-20293-202028'
book.autor = 'Petete Oiga OIGA'
print(book)

productos = [a, food]
productos.append(book)
print(productos)

for p in productos:
    print(p)