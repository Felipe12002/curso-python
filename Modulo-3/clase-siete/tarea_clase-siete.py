class MobilePhone:
    def __init__(self, manufacturer ='China', screen_size = '8.5', num_cores = '9', app = 'si', status = 'Apagado'):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.app = app
        self.status = status
        
    def Manufacturer(self):
        return self.manufacturer
    
    def Screen_size(self):
        return self.screen_size
    
    def Num_cores(self):
        return self.num_cores
    
    def App(self):
        return self.app
    
    def Status(self):
        return self.status
    

celular = MobilePhone()

celular.Manufacturer()
print("Manufactura: ", celular.manufacturer)
celular.Screen_size()
print("Tamaño de pantalla(pulgadas): ", celular.screen_size)
celular.Num_cores()
print("Números de Procesadores: ", celular.num_cores)
celular.App()
print("Tiene aplicaciones instaladas: ", celular.app)
celular.Status()
print("El estado del telefono es: ", celular.status)

print('\n')


