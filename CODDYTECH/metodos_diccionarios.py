my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)
# Output: dict_keys(['name', 'age', 'city'])
#imprime los keys

values = my_dict.values()
print(values)
# Output: dict_values(['Alice', 30, 'New York'])
#imprime los valores de los keys

items = my_dict.items()
print(items)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
#imprime en modo tupla key y valor

age = my_dict.get('age')
print(age)
# Output: 30
#imprime el valor de cierta key especificada

country = my_dict.get('country', 'USA')
print(country)
# Output: USA
#

city = my_dict.pop('city')
print(city)
# Output: 'New York'
print(my_dict)
# Output: {'name': 'Alice', 'age': 30}