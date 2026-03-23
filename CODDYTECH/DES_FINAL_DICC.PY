#Crea una función llamada view_contact que muestre los detalles de un contacto específico.
#Tu función debe:
#Tomar un diccionario de libro de contactos como parámetro
#Obtener un nombre de contacto de la entrada del usuario (usando input())
#Mostrar los detalles del contacto si se encuentra
#Imprimir "Contact not found!" si el contacto no existe
#Al mostrar un contacto, usa este formato exacto:
#Name: [name]
#Phone: [phone]
#Email: [email]
#Address: [address]

def view_contact(contacto):
    nombre = input()
    if nombre not in contacto:
        print("Contact not found!")
    elif nombre in contacto:
        print(f"Name: {nombre}")
        phone = contacto[nombre]["phone"]
        print(f"Phone: {phone}")
        email = contacto[nombre]["email"]
        print(f"Email: {email}")
        address = contacto[nombre]["address"]
        print(f"Address: {address}")
#Mejorado
#observacion en el if
def view_contact(contacto): 
    nombre = input()

    if nombre not in contacto:
        print("Contact not found!")
    else: 
        datos = contacto[nombre] #guarda la busqueda del diccionario

        print(f"Name: {nombre}")
        print(f"Phone: {datos['phone']}")
        print(f"Email: {datos['email']}")
        print(f"Address: {datos['address']}")