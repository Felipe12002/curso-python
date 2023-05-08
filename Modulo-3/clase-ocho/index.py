# Acceso directo a objetos
# objeto.atriburto  # obtengo valor
# objeto.atributo = valor  # cambio el valor, modifica

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

gato = Animal("Angora", "Persa")
print(gato.type)
gato.type = "Peludo"
print(gato.type)
print('\n*************************************\n')

# @property es para declarar cuando una funcion es una propiedad (getters)
# .setter


class Droid:
    def __init__(self,name):
        self.hidden_name = name
    
    @property
    def name(self) -> str:
        return self.hidden_name
    
    @name.setter
    def name(self, name:str) -> None:
        self.hidden_name= name

android = Droid("Arthur")
print(android.name)
android.name = 'Citripio'
print(android.name)



android.hidden_name = "Rojo"
# print(android.hidden_name)
# print(android.name)


# REALIZAR UN EJERCICIO CON PROPERTY Y SETTER




# Hidden hace referencia a un valor ue no puedo mostarr u ocupar libremente como una variable
# @property me permite obtener el valor de la variable hidden
# @setter me permite cambiar el valor de esta variable






print('\n*************************************\n')
# VALORES CALCULADOS
# valor que se devuelde un valor calculado o computado  partir de alguna operacion, etc


class CalculateValue:
    def __init__(self, _name, _height):
        self.name = _name
        self.height = _height
    
    @property
    def get_Calculate_Value(self) -> float:
        return 0.35 * self.height

valuex = CalculateValue("ratio", 10)

print((f'El {valuex.name} es: {valuex.get_Calculate_Value}'))


print('\n*************************************\n')
class Dog:
    obeys_owner = True # Esto es una variable global
    
    def __init__(self, _name):
        self.name = _name

dog_one = Dog("Robbin")
dog_two = Dog("Malta")
dog_three = Dog("Luz")


dog_one.obeys_owner = False
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')


print('\n*************************************\n')
dog_one.obeys_owner = False
dog_two.obeys_owner = False

print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')


print('\n*************************************\n')
Dog.obeys_owner = False # aqui la modificacion se aplicac a todos los elemnetos al mismo tiempo
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')






 


print('\n')