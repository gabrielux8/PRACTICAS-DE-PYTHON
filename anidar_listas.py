lst = [1, 2, 3]
new = []
reversa = lst[::-1] #almacena la lista de reversa
new = lst + reversa
primero = lst[0] #extrae el primer elemento de la lista

n = len(lst) #longitud de la lista
ultimo = lst[n - 1] #extrae el ultimo elemento de la lista

new.insert(0,primero) #indica donde se insertara el elemento

new.append(ultimo)

result = new + new
print(result)

#version mejorada por chat gpt
numbers = input().split()

# Paso 1: lista + reversa
reversa = numbers[::-1]
base = numbers + reversa

# Paso 2: agregar primero y último
primero = numbers[0]
ultimo = numbers[-1]

base.insert(0, primero)
base.append(ultimo)

# Paso 3: repetir dos veces
resultado = base * 2

print(resultado)

# 1 2 3 → [1, 1, 2, 3, 3, 2, 1, 3, 1, 1, 2, 3, 3, 2, 1, 3]