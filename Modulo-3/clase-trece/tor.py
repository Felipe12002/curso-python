class Torniquete:    
    pasaje = 730
    print('\n*******************************************************************************************************************')
    def __init__(self):
        self.patente_micro = []
        self.pasajero = []
        self.registro = []
        self.balance = []
    
    def abordar_micro(self, patente_micro, tipo_pasajero, fecha):
        if patente_micro not in self.patente_micro:            
            self.patente_micro.append({
            'patente_micro': patente_micro,
            'correlativo_abordaje': 1,
            #'Pago_pasaje': pago_pasaje,
            'balance': 0
        })
        
    def registro_torniquete_for(self, patente_micro, tipo_pasajero, fecha, balance):
        
           
        if elemento['tipo_pasajero'] == 'mujer' or elemento['tipo_pasajero'] == 'hombre':
            self.registro.append({
                'patente_micro': elemento['patente_micro'],
                'tipo_pasajero': elemento['tipo_pasajero'],
                'fecha_abordaje': elemento['fecha_abordaje'],
                'correlativo_abordaje': elemento['correlativo_abordaje'],
                'pago_pasaje': pasaje,
                'balance': balance
            })
            elemento['balance'] += 730
            elemento['correlativo_abordaje'] += 1
        elif elemento['tipo_pasajero'] == 'niño':
            self.registro.append({
                'patente_micro': patente_micro,
                'tipo_pasajero': tipo_pasajero,
                'fecha_abordaje': fecha,
                'correlativo_abordaje': elemento['correlativo_abordaje'],
                'pago_pasaje': 0,
                'balance': balance
            })
            elemento['balance'] += 0
            elemento['correlativo_abordaje'] += 1
        else: #tipo_pasajero == 'adulto_mayor':
            self.registro.append({
                'patente_micro': patente_micro,
                'tipo_pasajero': tipo_pasajero,
                'fecha_abordaje': fecha,
                'correlativo_abordaje': elemento['correlativo_abordaje'],
                'pago_pasaje': pasaje/2,
                'balance': balance
            })
            elemento['balance'] += 365
            elemento['correlativo_abordaje'] += 1
                #break
    
    def estado(self, patente_micro):
        movimientos = list(filter(lambda elementos: elementos['patente_micro'] == patente_micro, self.registro))
        print("{:<20}".format(" N° Viaje"),  "{:<20}".format("Fecha"),   "{:<20}".format("Tipo_pasajero"),   "{:<20}".format("Valor_pasaje"),  "{:<20}".format("Balance"))
        for elemento in movimientos:
            print("{:<20}".format(elemento['correlativo_abordaje']),  "{:<20}".format(elemento['fecha_abordaje']), "{:<20}".format(elemento['tipo_pasajero']),   "{:<20}".format(elemento['pago_pasaje']),  "{:<20}".format(elemento['balance']))


bus_intercomunal = Torniquete()

bus_intercomunal.abordar_micro("FGDS12", "mujer", "21/01/2023")
bus_intercomunal.abordar_micro("FGDS12", 'hombre', "22/01/2023")
bus_intercomunal.abordar_micro("FGDS12", 'mujer', "22/01/2023")
bus_intercomunal.abordar_micro("FGDS12", 'mujer', "23/01/2023")


bus_intercomunal.abordar_micro("FGDS13", 'niño', "24/01/2023")
bus_intercomunal.abordar_micro("FGDS13", 'adulto_mayor', "24/01/2023")
bus_intercomunal.abordar_micro("FGDS13", 'mujer', "25/01/2023")
bus_intercomunal.abordar_micro("FGDS13", 'niño', "25/01/2023")



bus_intercomunal.estado("FGDS12")





print('\n*******************************************************************************************************************\n')
