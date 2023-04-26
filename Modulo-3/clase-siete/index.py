# defino  mi primera calse
# pass nes para definir una clase vacia sin que indique un error
class Transporte:
    pass

# instanciar la clase y crear un objeto
# aqui se guardara en las variables transporte1 y transporte2 lo que resulte de la clase Transporte
transporte1 = Transporte()
transporte2 = Transporte()
transporte = Transporte()


class BuzzeLigthYear:
    pass

bozz1 = BuzzeLigthYear()
bozz2 = BuzzeLigthYear()


print(type(transporte1))
print(type(bozz1))

# las clases son un molde
# self debe ser incluido dentro de la definion. no es especificamente un parametro
class Droid:
    def __init__(self):  # esto es un metodo que esta por defecto (metodo constructor de la clase)
        self.power_on = False
    
    def switch_on(self):
        print("Hola soy un Droid, y estoy a tu orden")
        self.power_on = True          # esto es un atributo y siempre debe ser llamado con self
    
    def switch_off(self):
        print("Adios, enciendeme cuando me necesites")
        self.power_on = False          # esto es un atributo y siempre debe ser llamado con self


k8_arthur = Droid()
k8_citripio = Droid()

print('\n')
# de esta forma puedo utilizar el metodo de la clase
k8_arthur.switch_on()
print("power om Arthur: ", k8_arthur.power_on)
k8_citripio.switch_off()
print("power on citripio: ", k8_citripio.power_on)
k8_arthur.switch_off()
print(k8_arthur.power_on)



















print('\n')