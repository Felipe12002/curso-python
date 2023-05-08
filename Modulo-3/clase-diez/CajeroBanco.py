
# Automatización de un cajero automático

class Cuenta:
    total_abiertas = 0
    existentes = dict()
    
    def __init__(self, cliente):
        Cuenta.total_abiertas += 1
        self.cliente = cliente
        self.saldo = 0
        self.numero = f'UCR{Cuenta.total_abiertas: 04d }'
        self.fecha_apertura = datetime.now()
        Cuenta.existentes[self.numero] = self
        print(f"Se ha abierto la cuenta {self.numero} a nombre de {self.cliente} con fecha {self.fecha_apertura}")
    
    def __repr__(self):
        return print(f"Cuenta {self.numero}, cliente {self.cliente}, saldo = {self.saldo}")
    
    def depositar(self, monto):
        if monto < 0:
            print("Error: monto no puede ser negativo")
        else:
            self.saldo += monto
            print(f"Se depositó {monto} en la cuenta {self.numero}. Nuevo saldo es ")
    
    def retirar(self, monto):
        if monto < 0:
            print("Error: Monto no puede ser negativo")
        elif monto > self.saldo:
            print("error:fondos insuficientes")
        else:
            self.saldo -= monto
            print(f"Se retiró {monto} en la cuenta {self.numero}. Nuevo saldo es {self.saldo}")
    
    def transferir(self, monto, otra_cuenta):
        if monto < 0:
            print("Error: Monto no puede ser negativo")
        elif monto > self.saldo:
            print("error:fondos insuficientes")
        if otra_cuenta not in cuenta.existente:
            print("Error: Cuenta destino no exiate")
        else:
            self.saldo -= monto
            Cuenta.existente[otra_cuenta].saldo += monto
            print(f"Se transfirió {monto} en la cuenta {self.numero} a la cuenta {otra_cuenta}")
        
    
 
    cta1 = Cuenta("Felipe")
 