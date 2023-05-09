

lista = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller','Einstein', 'Pele', 'Juanes'] 

magos_list =['Harry Houdini', 'David Blaine', 'Teller']

cientificos_list = [lista[1], lista[3], lista[6]]

otros_list = [elemento for elemento in lista
                    if elemento not in magos_list and elemento not in cientificos_list]


def hacer_grandioso():
    for mago in magos_list:
        print(f'El gran {mago}')



def imprimir_nombres():
  for elemento in lista:
    print(elemento)



print('\n*****************************************')
print('Todos los nombres de la lista antes de ser modificados son: ')
imprimir_nombres()


print('\n*****************************************')
print('Magos Grandiosos son: ')
hacer_grandioso()


print('\n*****************************************')
print('los cientificos son: ')
for cientifico in cientificos_list:
  print(cientifico)


print('\n*****************************************')
print('Los personajes restantes son: ')
for restantes in otros_list:
  print(restantes)


print('\n******************************************\n')






print('\n')
