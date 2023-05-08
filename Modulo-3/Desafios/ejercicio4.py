
# Escribir un programa que pregunte al usuario por el número de horas trabajadas
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde



print('---------- Cálculo de Suelo -----------')
horas_trabajadas = float(input("Cuantas horas haz trabajado?: "))
costo_hora = float(input("Cuanto es el costo por hora?: "))

sueldo = horas_trabajadas * costo_hora
print(f'El pago que le corresponde es {sueldo} pesos')
print('\n')






