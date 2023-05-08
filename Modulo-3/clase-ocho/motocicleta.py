# class Motocicleta():
#     # Atributos de clase
#     estado = "nueva"
#     motor = False
    
#     # Métodos
#     def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
#         self.color = color
#         self.matricula = matricula
#         self.combustible_litros = combustible_litros
#         self.numero_ruedas = numero_ruedas
#         self.marca = marca
#         self.modelo = modelo
#         self.fecha_fabricacion = fecha_fabricacion
#         self.velocidad_punta = velocidad_punta
#         self.peso = peso
    
#     def arrancar(self):
#         if self.motor:
#             print("Se escucha un molesto sonido al girar la llave. El motor ya estaba arrancado.")
#         else:
#             print("Se ha arrancado el motor. Ruge como un león.")
            
#     def detener(self):
#         if self.motor:
#             print("Se detiene el motor.")
#         else:
#             print("No puedes parar el motor, porque ya está apagado. ¿No lo oyes?")
    



class Motocicleta():
    # Atributos de clase
    estado = "nueva"
    motor = False

    # Métodos
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, combustible_maximo):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.combustible_maximo = combustible_maximo

    def arrancar(self):
        if self.motor:
            print("Se escucha un molesto sonido al girar la llave. El motor ya estaba arrancado.")
        else:
            print("Se ha arrancado el motor. Ruge como un león.")
    
    def detener(self):
        if self.motor:
            print("Se detiene el motor.")
        else:
            print("No puedes parar el motor, porque ya está apagado. ¿No lo oyes?")

    def consulta_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} $.")

    def comprobar_deposito(self):
        print(f"--->REPORTE DE DEPÓSITO DE {self.marca} {self.modelo}<---")
        print(f"El depósito tiene {self.combustible_litros} litros.")
        print(f"La capacidad máxima del tanque de combustible es de {self.combustible_maximo}.")
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
                print("No cabe tanto combustible. ¿Quieres encharcar el concesionario?")

# Instancias de la clase Motocicleta
motocicleta_yamaha_1 = Motocicleta("Roja y blanca", "45663-FHDY", 10, 2, "Yamaha", "YZF-R1", "20/02/2020", 288, 199, 17)

motocicleta_harley_1 = Motocicleta(
    matricula="48659-FHEZ", 
    combustible_litros=0, 
    color="Negra", 
    marca="Harley Davidson", 
    modelo="Fat Boy", 
    numero_ruedas=2, 
    peso=304, 
    fecha_fabricacion="29/09/2020", 
    velocidad_punta=160,
    combustible_maximo=20
    )

motocicleta_harley_1.precio = 27000










# EJERCICIO
# https://programacionfacil.org/blog/ejercicios-de-programacion-orientada-a-objetos-en-python-100-dias-de-python-11/


# Respuesta
# https://programacionfacil.org/blog/soluciones-de-ejercicios-de-programacion-orientada-a-objetos-100-dias-de-python-11/




