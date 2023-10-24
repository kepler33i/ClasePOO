class VehiculoGrande:
    pass

class VehiculoMediano(VehiculoGrande):
    pass

class VehiculoChico(VehiculoMediano):
    pass

objetoVG = VehiculoGrande()
objetoVM = VehiculoMediano()
objetoVC = VehiculoChico()


for obj in [objetoVG, objetoVM, objetoVC]:
    for cls in [VehiculoGrande, VehiculoMediano, VehiculoChico]:
        print(isinstance(obj, cls), end='\t')
    print()

#Operador is es operador de igualdad (==) que compara los valores de ambos operandos


