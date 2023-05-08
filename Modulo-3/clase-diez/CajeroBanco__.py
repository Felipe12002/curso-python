class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Cuenta_Bancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.movimientos = []
        self.cantidad_movimientos = 0

    def abonar(self):
        abono = float(input("Ingrese el monto a abonar: "))
        self.saldo += abono
        self.movimientos.append(('Abono', abono, self.saldo))
        self.cantidad_movimientos += 1
        print(f'Se ha abonado exitosamente {abono}')

    def cargar(self):
        cargo = float(input("Ingrese el monto a cargar: "))
        if cargo > self.saldo:
            raise ValueError(f'No se puede hacer un cargo mayor a {self.saldo}')
        else:
            self.saldo -= cargo
            self.movimientos.append(('Cargo', cargo, self.saldo))
            self.cantidad_movimientos += 1
            print(f'Se ha cargado exitosamente {cargo}')
    
    def estado_cuenta(self):
        print(f'\n *******Estado de cuenta******** \n')
        print(f'La cuenta tiene un saldo de {self.saldo}')
        print(f'Cantidad de movimientos {self.cantidad_movimientos}')

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
persona = Persona(nombre, edad)

saldo_inicial = float(input("Ingrese el saldo inicial de su cuenta: "))
cuenta = Cuenta_Bancaria(saldo_inicial)

cuenta.abonar()
cuenta.cargar()
cuenta.estado_cuenta()
