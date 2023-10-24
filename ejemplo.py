class Ejemplo:
    __atributo_privado = print('Soy un atributo privado, solo puedo ser visto desde esta clase ')

    def __metodo_privado(self):
        print('Soy un metodo privado, solo puedo ser visto aca')

    def atributo_publico(self):
        return self.__atributo_privado
    
    def metodo_publico(self):
        return self.__metodo_privado
    
e = Ejemplo()
e.atributo_publico()
e.metodo_publico()