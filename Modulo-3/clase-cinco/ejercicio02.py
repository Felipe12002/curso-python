# utilizando dos while anidados, construya la tablas de mutiplicacion, ejemplo
# Ejemplo while anidados:
#    while codicion1
#        while codicion2
#            .....

def es_numerico(tabla):
    try:
        int(tabla)
        return True
    except ValueError:
        return False



print('\n')
print("********** Tablas de Multiplicar ***********")
n = 1
i = 's'
tabla = input("Ingrese la tabla de multiplicar que desea: ")
print('\n')

while es_numerico(tabla) == False:
    print("Debes ingresar un número entero")
    tabla = input("Ingrese la tabla de multiplicar que desea: ")
    print('\n')


while i == 's':
    while n <= 10:
        print(tabla + " x " + str(n) + " = " + str(n * int(tabla)))
        n = n +1
    
    i = input("Desea obtener otra tabla de multiplicar: S/N : ").lower()
    while i != 's' and i != 'n':
        print("Debes ingresar S/N: ")
        i = input("Desea obtener otra tabla de multiplicar: S/N : ").lower()
    print('\n')
    
    if i == 's':
        n = 1
        tabla = input("Ingrese la nueva tabla de multiplicar que desea: ")
        while es_numerico(tabla) != True:
            print("Debes ingresar un número entero")
            tabla = input("Ingrese la tabla de multiplicar que desea: ")
            print('\n')
    while n <= 10:
        print(tabla + " x " + str(n) + " = " + str(n * int(tabla)))
        n = n +1

print('\n')