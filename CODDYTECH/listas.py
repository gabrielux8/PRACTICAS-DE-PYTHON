""" Crea un programa que tome una lista e imprima:

Para listas con 5 o más elementos: los primeros dos y los últimos dos elementos
Para listas con menos de 5 elementos: solo el primero y el último elemento
 """
lst = [1, 2, 3, 4, 5, 6]
n = len(lst)
new = []
if n > 5:
    new.insert(0,lst[0])
    new.insert(1,lst[1])
    new.append(lst[-2])
    new.append(lst[-1])
else:
    new.insert(0,lst[0])
    new.append(lst[-1])
print(new)
