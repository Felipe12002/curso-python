# Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra 
# asociada con esa calificación. con al siguiente tabla
# 0 - 2 D
#2.1 - 5 C
# 5.1 - 6 B
#6.1 -7 A

print('\n')
print("********** Promedio de Notas ***********")
nota1 = float(input(("Ingrese nota 1: ")))
while nota1 < 0 or nota1 > 7:
    print("Debes ingresar una nota correcta")
    nota1 = float(input(("Ingrese nota 1:")))
                  
nota2 = float(input(("Ingrese nota 2: ")))
while nota2 < 0 or nota2 > 7:
    print("Debes ingresar una nota correcta")
    nota1 = float(input(("Ingrese nota 1:")))

nota3 = float(input(("Ingrese nota 3: ")))
while nota3 < 0 or nota3 > 7:
    print("Debes ingresar una nota correcta")
    nota1 = float(input(("Ingrese nota 1:")))

promedio = (nota1 + nota2 + nota3)/3
print('\n')

if 0 < promedio <= 2:
    print("*** Su calificación corresponde a la letra D ***")
elif 2.1 < promedio <= 5:
    print("*** Su calificación corresponde a la letra C ***")
elif 5.1 < promedio <= 6:
    print("*** Su calificación corresponde a la letra B ***")
elif 6.1 < promedio <= 7:
    print("*** Su calificación corresponde a la letra A ***")
print('\n')









