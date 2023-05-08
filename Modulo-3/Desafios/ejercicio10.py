
# Escribir un programa que pida al usuario dos números y muestre por pantalla 
# su división. Si el divisor es cero el programa debe mostrar un error.

numerador = float(input("Ingresa el numerador de la división: "))
denominador = float(input("Ingresa el denominador de la división: "))

if denominador == 0:
    print("No es posible dividir por 0")
else:
    resultado = numerador / denominador
    print(f'El resultado de la división es {round(resultado,2)}')

