for i in range(30, 80 + 1):
    if i % 4 == 0:
        print(i, end=", ")

print()

for pares in range (15, 31, 2):
    print(pares, end=", ")

print()

for num in range(50, 9, -1):
    if num % 5 == 0:
        print(num, end=", ")

print()

result = 1
for producto in range(1, 30 + 1):
    if producto % 3 == 0:
        result *= producto
print(result)