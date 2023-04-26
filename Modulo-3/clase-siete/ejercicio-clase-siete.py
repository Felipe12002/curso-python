class MobilePhone:
    def __init__(self, manufacturer ='China', screen_size = '8"', num_cores = '9', app = 'si', status = 'Apagado'):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.app = app
        self.status = status
        
    def getManufacturer(self):
        return self.manufacturer
    
    def getScreen_size(self):
        return self.screen_size
    
    def getNum_cores(self):
        return self.num_cores
    
    def getApp(self):
        return self.app
    
    def getStatus(self):
        return self.status
    
    # def mostrarMobilePhone(self):
    #     print("\nManufacturer: " + self.getManufacturer() + 
    #           "\nScreen_size: " + self.getScreen_size() + 
    #           "\nNum_cores: " + self.getNum_cores() + 
    #           "\nApp: " + self.getApp() + 
    #           "\nStatus: " + self.getStatus())
    

# manufacturer = input("Favor ingresa lugar de manufacturer: ")
# screen_size = input("Favor ingresa el tamaño de la pantalla: ")
# num_cores = input("Favor ingresa cuantos procesadores tiene: ")
# app = input("Favor ingresa si tiene aplicaciones: ")
# status = input("Favor ingresa el estado del equipo: ")
# e = MobilePhone(manufacturer, screen_size, num_cores, app, status)
# e.mostrarMobilePhone()

celular = MobilePhone()

celular.getManufacturer()
print("Manufactura: ", celular.manufacturer)
celular.getScreen_size()
print("Tamaño de pantalla: ")
celular.getNum_cores()
print("Números de Procesadores: ")
celular.getApp()
print("Tiene aplicaciones instaladas: ")
celular.getStatus
print("El estado del telefono es: ")

print('\n')





