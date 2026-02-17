""" Crea un programa que reciba dos listas e imprima una nueva lista
con todos los elementos que están en la primera lista pero NO en la segunda lista.
 """
lst1 = [1,2,3,4,5]
lst2 = [2,4,6]
new_list = []
for i in lst1:
    if i not in lst2:
        new_list.append(i)

print(new_list)
