#Ahora, crea la función add_contact que toma un argumento: contact_book (un diccionario). 
# La función debe:
#Obtener entrada para el nombre del contacto, teléfono, correo electrónico y dirección.
#Verificar si el nombre ya existe en el diccionario. Si es así, imprimir: "Contact already exists!".
#Si no, guardar el contacto en el siguiente formato:
#contact_book[name] = {
#	"phone": phone,
#	"email": email,
#	"address": address}
#Luego imprimir: "Contact added successfully!".
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact") 
    print("2. View Contact") 
    print("3. Edit Contact") 
    print("4. Delete Contact")
    print("5. List All Contacts") 
    print("6. Exit")

def add_contact(contact_book):
    name = input()
    telefono = input()
    correo = input()
    direccion = input()
    if name not in contact_book:
        contact_book[name] = {
            "phone": telefono,
            "email": correo,
            "address": direccion
        }
        print("Contact added successfully!")
    elif name in contact_book:
        print("Contact already exists!") #entrada: {} Alice 123-456-7890 alice@example.com 123 Main St


def view_contact(contacto):
    nombre = input()
    if nombre not in contacto:
        print("Contact not found!")
    elif nombre in contacto:
        name = contacto.get('name')
        print(f"Name: {name}")