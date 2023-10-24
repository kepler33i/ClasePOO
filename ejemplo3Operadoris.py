class Ejemplo:
    def __init__(self, var) -> None:
        self.var= var

objeto1 = Ejemplo(0)
objeto2 = Ejemplo(2)
objeto3 = objeto1
objeto3.var +=1

print(objeto1 is objeto2)
print(objeto2 is objeto3)
print(objeto3 is objeto1)
print(objeto1.var, objeto2.var, objeto3.var)

string1 = 'Juanito have '
string2 = 'Juanito have one cookie'
string1 += 'one cookie'

print(string1==string2, string1 is string2)

