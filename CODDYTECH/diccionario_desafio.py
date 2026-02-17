# Crea una función llamada check_inventory que tome dos parámetros: 
# inventory (un diccionario donde las claves son nombres de ítems y los valores son cantidades) y 
# item (una cadena que representa el ítem a verificar). La función debe:

# Verificar si el item existe como una clave en el diccionario inventory.
# Si el ítem existe en el inventario (independientemente de la cantidad), 
# devolver la cadena: "<item> is in stock. Quantity: <quantity>".
# Si el ítem no existe como una clave en el inventario, devolver la 
# cadena: "<item> is not in stock."
# Nota: Un ítem se considera "in stock" si existe en el diccionario de inventario, 
# incluso si su cantidad es 0. La función solo debe verificar la presencia de la clave, 
# no el valor de la cantidad.


def check_inventory(inventory, item):
    if item not in inventory:
        print(f"{item} is not in stock.")
    else:
        for i, quantity in inventory.items():
            if item == i:
                print(f"{item} is in stock. Quantity: {quantity}")