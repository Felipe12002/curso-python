class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.app = []
        self.status = False
        
    def switch_on(self):
        print('Iniciado')
        self.switch_on = True
    
    def switch_off(self):
        print('Apagado')
        self.switch_off = False
    
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
    

celular = MobilePhone('China', '8"','9')


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


