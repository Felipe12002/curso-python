# Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
# Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), 
# forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.

def es_numerico(m):
    try:
        int(m)
        return True
    except ValueError:
        return False

print('\n')
print("********** Trimestre ***********")

m = input(("Ingrese el número del mes buscado : "))
while es_numerico(m) == False or int(m) < 0 or int(m) > 12:
    print("Debes ingresar un número entero positivo entre 1 y 12")
    m = input(("Ingrese el primer valor : "))
    print('\n')


if 1 <= int(m) <= 3:
    print("El mes corresponde al Primer Semestre!!") 
elif 4 <= int(m) <= 6:
    print("El mes corresponde al Segundo Semestre!!") 
elif 7 <= int(m) <= 9:
    print("El mes corresponde al Tercer Semestre!!")
elif 10 <= int(m) <= 12:
    print("El mes corresponde al Cuarto Semestre!!")

print('\n')