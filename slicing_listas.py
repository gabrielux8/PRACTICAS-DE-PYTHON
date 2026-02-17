""" Crea un programa que reciba una lista como entrada e imprima cuatro nuevas listas basadas en las siguientes operaciones de slicing:

Una lista que contenga cada cuarto elemento, comenzando desde el índice 2
Una lista que contenga todos los elementos desde el 3er elemento hasta el 3er elemento desde el final
Una lista que contenga cada otro elemento en orden inverso, comenzando con el último elemento
Una lista que contenga los primeros tres y los últimos tres elementos de la lista original
Nombra las listas list1, list2, list3 y list4 - correspondientemente. """

original_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Write your code below
list1 = original_list[2::4]
list2 = original_list[2:-2]
list3 = original_list[::-2]
list4 = original_list[:3] + original_list[-3:]
# Don't change below this line
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)

""" Resultado esperado
List 1: ['3', '7', '11', '15']
List 2: ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
List 3: ['15', '13', '11', '9', '7', '5', '3', '1']
List 4: ['1', '2', '3', '13', '14', '15'] """