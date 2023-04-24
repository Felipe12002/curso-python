# diccionarios
variable = {}
print(variable)
variable = {
    "id:":1,
    "nombre:": "Felipe",
    "edad:": 102
}
print(variable)


# practicar como obtener un elemento, añadir un elelmento, 
# modificar y eliminar

var = {
    "lunes": 30.0,
    "martes": 25.2,
    "miercoles": 12,
    "jueves": 16.5,
    "viernes": 25.2,
    "sabado": 27.1,
    "domingo": 11.0
}
print(var)
print('\n')

#si no existe la variable buscada, la crea en el diccionario
var['deporte']="football"
print(var)
print('\n')


# cuando declaro con dict no tengo que colocar la doble comilla en el keys
# PERO EL MAS OPTIMO ES CREAR EL DICCIONARIO CON LAS LLAVES {}
empty_dic_2 = dict()
print(empty_dic_2)

full_dict = dict(
    genero = "M",
    nacionalidad = "E"
)
print(full_dict)
print('\n')

# iteracion de diccionarios: por valores o por clave-valor
# segun sus valores
empleado = {
    "name": "valeria",
    "apellido": "roso",
    "edad": 18,
    "rut": "11.111.111-1"
}
print(empleado)

for variablex in empleado.values():
    print(variablex)
    
print('\n')
var = {
    "lunes": 30.0,
    "martes": 25.2,
    "miercoles": 12,
    "jueves": 16.5,
    "viernes": 25.2,
    "sabado": 27.1,
    "domingo": 11.0
}
print(var)

for x in var.values():
    print(x)
print('\n')

# segun su clave-valor, aqui imprime el keys y su valor
var = {
    "lunes": 30.0,
    "martes": 25.2,
    "miercoles": 12,
    "jueves": 16.5,
    "viernes": 25.2,
    "sabado": 27.1,
    "domingo": 11.0
}
print(var)
for a, b in var.items():
    print(a, b)
print('\n')



# condicionales
print("********** condicionales **********")
edad = 20
if edad >18:
    print("eres mayor de edad")
    
print('\n')

temperatura = 35
if temperatura >= 37:
    print("Alerta de temperatura alta")
else:
    print("La temperatura es normal")

print('\n')


temperatura = 5
pais = 'chile'

if temperatura < 10:
    if pais == 'Chile':
        print('cccc')
    else:
        print('zzz')
else:
    if pais == 'Chile':
        print('111')
    else:
        print('222')


if temperatura < 10:
    print("Es altamente probable que nieve")
elif temperatura >= 10 and temperatura <= 20:
    print("Es medianamente probable que nieve")
else:
    print("No hay probabilidad de nieve")

print('\n')

# ejercicio
print("********** ejercicio **********")
#escriba un programa que permita adivinar un personaje de marvel en base a esta 3 preguntas
# puede volar
# Es humano
# Tiene mascara

volar = "si"
humano = "no"
mascara = "si"

if volar == "si" and humano != "si" and mascara != "no":
    print("El personaje es Superman (DC)")
elif volar != "si" and humano == "si" and mascara == "si":
    print("El personaje es Spiderman (Marvel)")
else:
    print("Deberías tener mayor informacion")
    
print('\n')


# Ciclos
print("********** ciclos ***********")
want_exit = 'n'
while want_exit == 'n':
    print("Hola como estas")
    want_exit = input("¿Quieres salir S/N?: ")

print("Fuera de While")


# break, nos permite romper un ciclo
want_exit = 'n'
run_questions = 0
while want_exit == 'n':
    print("Hola como estas")
    want_exit = input("¿Quieres salir S/N?: ")
    run_questions += 1
    if run_questions == 4:
        print("Alcanzaste el maximo permitido")
        break

print("Fuera de While")







