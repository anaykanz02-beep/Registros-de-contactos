contactos = {}

nombre = input("Ingrese el nombre del contacto: ")
telefono = input("Ingrese el número telefónico: ")

contactos[nombre] = telefono

print("\nContactos registrados:")

for nombre, telefono in contactos.items():
    print("Nombre:", nombre, "- Teléfono:", telefono)

buscar = input("\nIngrese el nombre del contacto que desea buscar: ")

if buscar in contactos:
    print("Contacto encontrado.")
    print("Teléfono:", contactos[buscar])
else:
    print("El contacto no se encuentra registrado.")