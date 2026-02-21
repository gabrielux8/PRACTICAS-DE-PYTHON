#Crea una función llamada frequency_counter que tome una lista data_list como argumento. 
#La función debe contar la frecuencia de cada elemento en la lista y devolver un diccionario 
#donde las claves son los elementos únicos de la lista y los valores son las cuentas de 
#cuántas veces aparece cada elemento.

#Por ejemplo, si la lista de entrada es [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 
#la función debe devolver un diccionario como este:
#{1: 1, 2: 2, 3: 3, 4: 4}

frecuencia = ["apple", "banana", "apple", "cherry", "banana", "banana"]
diccionario = {}
for i in frecuencia:
    if i not in diccionario: # si no se encuentra en el diccionario lo agrega con valor 1
        diccionario[i] = 1
    elif i in diccionario:
        conteo = diccionario.get(i) #esta variable para saber cuantos hay con esa key
        diccionario.update({i:conteo+1}) #le sumo uno si hay otra key
print(diccionario)
#recorrer la lista
#si en la lista existe aumentas el contador
#si no lo agregas

'''def frequency_counter(data_list):
    diccionario = {}
    for i in data_list:
        if i not in diccionario:
            diccionario[i] = 1
        elif i in diccionario:
            conteo = diccionario.get(i)
            diccionario.update({i:conteo+1})
    print(diccionario)'''