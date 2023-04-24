# Escriba un programa que eliminar un signo de exclamación del final de una cadena. 
# puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.


print('\n')
print("********** Eliminar Signo de Exclamación ***********")

texto = input("Ingrese una frase con signo de exclamación al final: ")
print("El texto original es: " + texto)
texto = texto.rstrip(texto[-1])
print("El texto modificado es: " + texto)







