

class Motocicleta:
    is_new = True
    motor = False
    
    def __init__(self, _color, _matricula, _combustible_litros, _numero_ruedas, 
                 _marca, _modelo, _fecha_fabricacion, _velocidad_punta, _peso, _combustible_maximo):
        self.color = _color
        self.matricula = _matricula
        self.combustible_litros = _combustible_litros
        self.numero_ruedas = _numero_ruedas
        self.marca = _marca
        self.modelo = _modelo
        self.fecha_fabricacion = _fecha_fabricacion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso
        self.combustible_maximo = _combustible_maximo
    
    
    # if self.variable == False:  === if not self.variable:
    # if self.variable == true:  === if self.variable:
    
    
    # aqui coloco las condiciones para ser evaluadas 
    # por el atributo de le linea 5
    def arrancar(self):
        if self.motor == True:
            print("El Motor ya estaba en marcha")
        else:
            print("El motor ha arrancado")
    
    def detener(self):
        if self.motor == True:
            print("El motor se ha detenido")
        else:
            print("El motor ya estába detenido")
    
    def consulta_precio(self):
	    print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} $.")
    
    
    # Pregunta 14
    def comprobar_deposito(self):
        print(f"**** REPORTE DE {self.marca} {self.modelo} ****")
        print(f"El depósito tiene {self.combustible_litros} litros.")
        print(f"La capacidad máxima del tanque de combustible es de {self.combustible_maximo} litros.")
        print(f"Faltan {self.combustible_maximo - self.combustible_litros} litros para llenar el depósito.")
        print(f"--->FIN DEL REPORTE<---\n")
    
    def repostar(self):
        while True:
            self.repostar_litros = float(input("Por favor, introduzca la cantidad de litros que desea repostar:\n"))
            
            if self.combustible_litros + self.repostar_litros <= self.combustible_maximo:
                print("Repostaje exitoso.")
                print(f"Se han repostado {self.repostar_litros} litros.")
                self.combustible_litros += self.repostar_litros 
                print(f"El depósito tiene {self.combustible_litros} litros de combustible.")
                break
            else:
                print("La cantidad de combustible a colocar, supera el máximo, \n intente con una cifra menor")




print('\n*******************************\n')
motocicleta_Suzuki = Motocicleta("Azul", "THD-254", 10, 2, "Suzuki", "Gsxr 1000", "2022/05/10", "290 km/hr", "200 kg", 17)
print(f'La motocicleta {motocicleta_Suzuki.marca} fue fabricada con fecha: {motocicleta_Suzuki.fecha_fabricacion}')
print(f'La motocicleta {motocicleta_Suzuki.marca} tiene un estaque de : {motocicleta_Suzuki.combustible_litros} litos de capacidad')
print('\n*******************************\n')

# Orden no posicionales
motocicleta_ducati = Motocicleta(_peso= "220 kg",_velocidad_punta="308 km/hr", _fecha_fabricacion= "2022/10/05", _modelo= "V4 R 2023",
                                 _marca= "Ducati", _numero_ruedas= 2, _combustible_litros= 0, _matricula= "THD-254", _color= "Roja", _combustible_maximo= 20)
print(f'La motocicleta {motocicleta_ducati.marca} fue fabricada con fecha: {motocicleta_ducati.fecha_fabricacion}')
print(f'La motocicleta {motocicleta_ducati.marca} tiene un estaque de : {motocicleta_ducati.combustible_litros} litos de capacidad')
print('\n*******************************\n')



# llamar un método de un objeto
motocicleta_ducati.arrancar()
motocicleta_ducati.detener()

print('\n*******************************\n')
# Asignar un valor
motocicleta_Suzuki.precio = "$18.000.000"
print(f'La precio de  la motocicleta {motocicleta_Suzuki.marca} modelo {motocicleta_Suzuki.modelo} tiene un valor de : {motocicleta_Suzuki.precio}')

print('\n*******************************\n')

# Consultar el precio desde un metodo
motocicleta_Suzuki.consulta_precio()

print('\n*******************************\n')
# Consultar el precio desde un metodo, pero la motocicleta ducati no tiene
# motocicleta_ducati.consulta_precio()

print('\n*******************************\n')
# Pregunta 14
motocicleta_ducati.comprobar_deposito()
print('\n')
motocicleta_Suzuki.comprobar_deposito()
print('\n')
motocicleta_ducati.repostar()
print('\n')
motocicleta_Suzuki.repostar()

print('\n*******************************\n')












