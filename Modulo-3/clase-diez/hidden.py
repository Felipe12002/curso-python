
# para ocultar variables __variable automaticamente dr oculta 
# no se accede desde la instancia u objeto
# class Droid:,
#     def __init__(self,name):
#         self.__name = name
    
#     @property
#     def name(self) -> str:
#         return self.__name
    
#     @name.setter
#     def name(self, name:str) -> None:
#         self.__name= name

# arturo = Droid("Arturo")
# print((arturo.__name))




# Cree una clase llamada artefacto, agreguele tres atributos y 
# utilice los getter and setter para acdeder a ellos

class Artefeacto:
    def __init__(self, marca, tamaño, precio):
        self.__marca = marca
        self.__tamaño = tamaño
        self.__precio = precio
    
    @property
    def marca(self) -> str:
        return self.__marca
    
    @marca.setter
    def marca(self, marca:str) -> None:
        self.__marca= marca


radio = Artefeacto("Casio", "30 cm", 20.000)
print(radio.marca)


print('\n')



#Métodos de instancia
# def nombre_metodo(self, parametros)

# Métodos de la clase
# modifica los atributos de la clase no de la instancia

# @classmethod
# def nombre_method(cls)









