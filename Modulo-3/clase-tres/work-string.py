# Concatenación
first_name = "Felipe"
last_name = "Arias"
print(first_name +" "+ last_name)

# Multiplicacion de String
mensaje1 = "Hola " * 3
print(mensaje1)

# añadir
mensaje3 = "Sebastian"
print(mensaje3)
mensaje3 += ","
print(mensaje3)
mensaje3 += "Arias"
print(mensaje3)

# Funcion [built in]: len (longitud) obtiene el total de caracteres
print(len(mensaje3))

# Funcion [own function]
# si el valor es -1 significa que no hay coicidencia. no existe
cadena = "esto es una oracion por ucrania"
posicion = cadena.find("pelo")
print("pelo se encuentra en ", posicion)
posicion = cadena.find("ucrania")
print("ucrania se encuentra en:",posicion)


# Funcion lower
texto = "CASA"
print(texto)
texto = texto.lower()
print(texto)

# reemplazar cadenas
texto = "el arbol sobre la montaña"
print(texto)
texto = texto.replace('arbol', 'auto')
print(texto)

print('\n')
print("********* LISTAS **********")
# listas parecidos a los array en js
empity_list = []
print(empity_list)
fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Felipe"}, (1, 3, 5)]
print(fullfiled_list)
print('\n')

# la funcion list permite convertir a una lista
print(list('concurso'))
print('\n')


# la funcion range toma un rango de valores
range_one = range(50)
print(list(range_one))
print('\n')

# agregar un item a la lista
numeros = [1, 4, 6]
print(numeros)
numeros.append(10)
print(numeros)
print('\n')



# seleccionar o extraer un elemnto de la lista, esto es con la posicion
print(numeros[2])
print('\n')


# iterar una lista
lista = ["carmen","elena","lucia","sara","patricia"]
for i in lista:
    print(i)


print('\n')
# eliminar un elemento de una lista, lista.remove(valor), lista.pop(posicion), del lista[posicion]
lista.remove("elena")
print(lista)
print('\n')


# modificar una lista
lista[1] = "natalia"
print(lista)
print('\n')


print("********* TUPLAS **********")
# Son inmutable
# Se generen usando parentesis
print('\n')
empity_tuple = ()
fullfille_tuple = (1, "Felipe", 500.87)
print(empity_tuple, fullfille_tuple)
print(type(fullfille_tuple))
print('\n')
one_tuple = ('juan',)
print(one_tuple)
print(type(one_tuple))
print('\n')


# otra forma de declarar las tuplas, pero esto no es lo ideal, mejor utilizar parentesis
hojas = 'carta', 'oficio'
print(hojas)
print(type(hojas))
print('\n')


# convertir una lista a una tupla
empty_tuple_2 = tuple()
print(empty_tuple_2)

list_to_convert = [2,6,8,9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)
print('\n')




# EXISTE UNA FORMA MAS DIRECTA DE HACER ESTO MISMO DIRECTAMENTE SOBRE LA TUPLA
# reverse()
print("Reverse")
list_tupla = (1, 2 , 3, 4, 5)
print(list_tupla)
list_tupla = list(list_tupla)
print(list_tupla)
list_tupla.reverse()
print(tuple(list_tupla))
print('\n')


# append()
print("append")
list_tupla = (1, 2 , 3, 4, 5)
print(list_tupla)
list_tupla = list(list_tupla)
print(list_tupla)
list_tupla.append(100)
print(tuple(list_tupla))
print('\n')




# extend


# remove
print("Remove")
list_tupla = (1, 2 , 3, 4, 5)
print(list_tupla)
list_tupla = list(list_tupla)
print(list_tupla)
list_tupla.remove(2)
print(tuple(list_tupla))
print('\n')



# clear()

# sort()
















