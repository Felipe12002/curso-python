

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere 
# una pizza vegetariana o no, y en función de su respuesta le muestre un 
# menú con los ingredientes disponibles para que elija. Solo se puede eligir 
# un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
# todos los ingredientes que lleva.



pizza_vegetariana = ['pimiento', 'tofu']
pizza_no_vegetariana = ['peperoni', 'jamon', 'salmon']


tipo_pizza = str(input("Qué tipo de pizza quieres? (vegetariana/normal): "))
print("Ingredientes disponibles :")
if tipo_pizza == "vegetariana":
    print(pizza_vegetariana)
    ingrediente = str(input("Qué ingrediente vegetariano desea? "))
else:
    print(pizza_no_vegetariana)
    ingrediente = str(input("Qué ingrediente normal desea? "))

print(f"La base de la pizza tiene tomate, mozarella y le sumaste {ingrediente}")





print('\n')
