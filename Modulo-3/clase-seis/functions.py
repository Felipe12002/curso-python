# definicion de funciones
def saludar(name):
    print(f'Hola {name}!!!')

saludar('rodrigo')


def saludar_dos(first_name, last_name):
    print(f'Hola {first_name}, {last_name}')

saludar_dos('Felipe', 'Arias')

# usando valores posicionales, puedo cambiar el orden de ingresar los parametros
saludar_dos(last_name='Arias', first_name='Felipe')

print('\n')
# puedo prederminar un valor, para que quede por defecto pero se puede cambiar al llamar la funcion
def multiplicar_text(texto, multipler=1):
    print(texto * multipler)

multiplicar_text("v",5)
multiplicar_text("x")


# si coloco arterisco, indico que pueden venir infinitos parametros
# todo lo que este despues del * se presentara en una tupla
def varietal(paran1, param2, *others):
    print(paran1)
    print(param2)
    print(others)

varietal("1A", "2B", 0)
print('\n')
varietal("1A", "2B", 0, "xx", [0, 1])


print('\n')
# al ocupar doble **, voy a producir un diccionarie en vez de una tupla
def varietal_dos(paran1, **others):
    print(paran1)
    print(others)


varietal_dos("1A", id = 0, name = 'Carlos')




print('\n')