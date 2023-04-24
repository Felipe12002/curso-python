# Escriba un programa que calcule el máximo común divisor entre dos números enteros.

def es_numerico(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


print('\n')
print("********** Máximo común divisor entre 2 números ***********")


n1 = input(("Ingrese el primer valor : "))
while es_numerico(n1) == False or n1 < '0':
    print("Debes ingresar un número entero positivo")
    n1 = input(("Ingrese el primer valor : "))
    print('\n')


n2 = input(("Ingrese el segundo valor : "))
while es_numerico(n2) == False or n2 == '0' or n2 < '0':
    print("Debes ingresar un número entero positivo")
    n2 = input(("Ingrese el segundo valor : "))
    print('\n')

n3 = 0

while n2 != 0:
    n3 = int(n2)
    n2 = int(n1) % int(n2)
    n1 = int(n3)

print("El máximo común divisor es: ", n1)

