#def print_product_details(product_data):
product_data = {"name":"Laptop","brand":"Dell","price":799.99,"stock":15}
longuitud = len(product_data) #longuitid del diccionario (4)
if longuitud == 0:
    print("No product information available")
else:
    for producto, descipcion in product_data.items():
        producto = producto.capitalize() #solo pone en mayusculas la primer letra, upper TODA la cadena
        print(f"{producto}: {descipcion}")