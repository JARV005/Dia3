#Menu con 4 opciones 
#Agregar datos de usuario
# , eliminar, 
# Consultar datos de un usuario( con posibilidad de modificar) 
# lista de usuarios 

Lista=[]





Menu=0
while Menu!= 5:
    Menu=input("Seleccione que desea hacer \n 1. Agregar usuario \n 2. Editar usuario \n 3. Eliminar usuario \n 4. Mostrar lista de usuarios \n 5. Salir del menu \n  ")
    Menu=int(Menu)

    
    if Menu==1:
        
        Nombre=input("Ingrese el nombre del usuario ")
        Apellido=input("Ingrese el apellido del usuario ")
        Correo=input("Ingrese el correo del usuario ")
        Edad=input("Ingrese la edad del usuario ")
        Edad=int(Edad)
        Lista.append(Nombre)
        Lista.append(Apellido)
        Lista.append(Correo)
        Lista.append(Edad)
        
    if Menu==2:
        Nombre=input("Ingrese el nombre del usuario a modificar ")
        NuevoNom=input("Ingrese el nuevo nombre ")
        
        nuevoN=[Nombre.replace(Nombre,NuevoNom) for NuevoNom in Nombre]
    if Menu==4:
        print(Lista)


    persona = {
        "Nombre": Nombre,
        "Apellido": Apellido,
        "Edad": Edad,
        "Correo": Correo
    }
    Lista.append(persona)

for persona in Lista:
    print(persona)

