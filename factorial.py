factorial = int(input()) #numero dado
result = 1

for i in range(1, factorial + 1): #fuerzas a incluir el numero dado con n +1
    result *= i #esto es lo mismo que result = result * i
        
print(result) #dejar fuera del bucle para que solo me de el resultado final de lo
# contrario me dice step por step (paso por paso)