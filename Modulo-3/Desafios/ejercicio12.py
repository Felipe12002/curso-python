

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al 
# sexo y el Nombre. El grupo A esta formado por las mujeres con un nombre 
# anterior a la M Y a los hombres con un nombre posterior a la N y el grupo B 
# por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde



nombre = str(input("Cual es tu nombre: "))
sexo = str(input("Cual es tu sexo (M/H): "))

print(nombre)
print(sexo)


if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

if sexo == "m":
    sexo = "Mujer"
else:
    sexo = "Hombre"
        
print(f'Tu nombre es {nombre}, tu sexo es {sexo}, entonces perteneces al grupo {grupo}')






