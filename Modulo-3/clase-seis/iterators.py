# esto imprime cada caracter de la cadenausando for
words = "Esto es una cadena de texto"

for letter in words:
    print(letter)



# de esta forma imprime cada palabra de la cadena usando for
words = "Esto es una cadena de texto "
word = ' '
for letter in words:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ' '



# con break puedo detener la ejecucion 
print("\n----------------\n")
for letter in words:
    if letter != ' ':
        print(letter)
    else:
        break

print('\n')



# for tambien se puede utilizar en una lista
animals_list = ['gato', 'perro', 'pajaro', 'ardilla']

for animal in animals_list:
    print(animal)


print('\n')
list1 = range(2,3)
print(list1)
# siempre impre hasta un numero menso del rango
for number_in in range(1,10):
    print(number_in)


print('\n')
# tambien la funcion rango tiene un tercer paramentro, por defecto viene en 1, 
# pero este cada cuando se van a tomar los valores
for number_in in range(1,10, 3):
    print(number_in)




# for anidados
print('\n ---------- tabals de multiplicar ---------\n')
for num_tabla in range(1,10):
    for num_mu1 in range(1,10):
        result = num_tabla *num_mu1
        print(f'{num_tabla} x {num_mu1} = {result}')
    print("\n----------------------------\n")



print('\n')