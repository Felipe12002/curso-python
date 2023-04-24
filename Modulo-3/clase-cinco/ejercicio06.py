# Se le asignado un tarea para programar un algoritmo para una lavadora, debe 
# investigar cuanta agua se neceita para lavar prendas
# con las siguientes caracteriticas, algodon, nilon, poliester, debe investigar 
# para una lavadora de xx kg cuantas prendas de cada una puede 
# lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder 
# calcular lo siguiente

# Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la 
# cantidad de ropa a lavar es 14, # entonces necesitas 5 * 1.1 ^ (14 - 10) cantidad de agua.

# Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
# La función aceptará 2 argumentos: - carga lavadora y ropa.




# Funcion para determinar que el valor ingresado sea un numero entero y no decinal
def es_numerico(m):
    try:
        int(m)
        return True
    except ValueError:
        return False


print('\n')
print("********** Lavadora ***********")

# peso en kg de una prenda de algodón (inventado)
# algodon = 0.5 

# Peso en kg de una prenda de nylon  (inventado)
# nylon = 0.2 

# peso en kg de una prenda de poliester  (inventado)
# poliester = 0.3 

# n es el numero de prendas del mismo tipo
n = 1 

#  litros de agua minima que necesita la lavadora para funcionar  (inventado)
agua = 5


# solicito al usuario la capacidad de la lavadora a utilizar, que puede variar entre 7 kg a 25 kg  (inventado)
# y verifico que el valor ingresado sea un numero entero, sea positivo y este en el rango determinado
lavadora = input("Cuantos kg es la carga de la lavadora: ")
while es_numerico(lavadora) == False or int(lavadora) < 7 or int(lavadora) > 25:
    print("Debes ingresar un número entero positivo entre 7 y 25")
    lavadora = input(("Cuantos kg es la carga de la lavadora: "))
    print('\n')


# solicito al usuario que tipo de prenda quiere lavar, pensado que todas serán del mismo tipo
# verifico que los datos ingresados sean correctos
prenda = input("Que tipo de prenda quieres lavar: " '\n' + "[1] Algodón" '\n' + "[2] Nylón" '\n' + "[3] Poliester" '\n' '\n')
while es_numerico(prenda) == False or int(prenda) < 1 or int(prenda) > 3:
    print("Debes seleccionar una de las 3 alternativas")
    prenda = input("Que tipo de prenda quieres lavar: " '\n' + "[1] Algodón" '\n' + "[2] Nylón" '\n' + "[3] Poliester" '\n' '\n')
    print('\n')


# de acuerdo al valor ingresado asigno un peso de cada penda  (inventado)
if prenda == '1':
    peso = 0.5
elif prenda == '2':
    peso = 0.3
elif prenda == '3':
    peso = 0.2


# cambie la formula entregada ya que era posible determinar lo solicitado
# adapte a la siguiente formula  (inventado)
pesodelavado = 5 
while pesodelavado < int(lavadora):
    agua = 5 + 1.1 * n * peso
    pesodelavado = agua + n * peso
    n = n + 1


# el peso de lavado no puede ser mayoar a la capacidad de la lavadora
agua = round(5 + 1.1 * (n-2) * peso, 2)
pesodelavado = round(agua + (n-2) * peso,2)

print("la cantidad de prendas que puedo lavar es: " + str(n-2) )
print("La cantidad de agua necesaria para una carga de prendas es de: " + str(agua) + " Lts")
print("El peso total del agua + la ropa es: " + str(pesodelavado) + " kg")
print('\n')




