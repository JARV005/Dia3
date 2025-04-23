# Lista vacía donde se almacenarán las personas con sus datos
personas = []

# Función para ingresar datos desde el usuario
def ingresar_dato():
    # Pedir datos al usuario
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))  # Convertimos a entero
    correo = input("Ingrese el correo: ")
    
    # Crear un diccionario con los datos de la persona
    persona = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Correo": correo
    }
    
    # Agregar el diccionario a la lista 'personas'
    personas.append(persona)

# Función principal para ingresar varias personas
def ingresar_personas():
    while True:
        ingresar_dato()
        continuar = input("¿Desea ingresar otra persona? (s/n): ").lower()
        if continuar != 's':
            break

# Llamar a la función para ingresar datos
ingresar_personas()

# Mostrar todos los datos organizados
print("\nDatos organizados:")
for persona in personas:
    print(persona)



        