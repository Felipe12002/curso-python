

# Escribir un programa que le pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión.


print('---------- Cálculo de inversión ----------')
cantidad_invertir = float(input("Cuál es tu cantidad a invertir?: "))
interes_anual = float(input("Cuál es el interés anual?: "))
num_anios = int(input("Cuántos años vas a invertir?: "))

capital_obtenido = cantidad_invertir * (1 + (interes_anual/100))**num_anios


print(f'El capital obtenido es de {round(capital_obtenido,2)} pesos')


