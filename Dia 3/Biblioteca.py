#Crear diccionario
biblioteca = {
    '001': {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    '002': {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949}
}


print("Menú de biblioteca \n","1. Agregar libro \n", "2. Ver todos los libros \n", "3. Buscar libro \n", "4. Modifica la informacion de un libro \n", "5. Eliminar libro \n", "6. Salir \n" )

accion=input("Seleccione una opcion entre 1-5 ")
accion=int(accion)
while accion!=6:

    if accion==1:

        print("\n    AGREGAR NUEVO LIBRO    ")
        id_libro = input("Ingrese el ID del libro: ")

        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        año = input("Año de publicación: ")

        biblioteca[id_libro] = {
            'titulo': titulo,
            'autor': autor,
            'año': int(año)
        }
        print(f"Libro '{titulo}' agregado con éxito!")
        # Preguntar si desea agregar otro libro
        continuar = input("¿Desea agregar otro libro? (si/no): ").strip().lower()
        if continuar == "no":
            break
    if accion==2:
        print("\n   TODOS LOS LIBROS    ")
        for id_libro, info in biblioteca.items():
            print(f"\nID: {id_libro}")
            print(f"Título: {info['titulo']}")
            print(f"Autor: {info['autor']}")
            print(f"Año: {info['año']}")
        break

    if accion==3:
        print("\n    BUSCAR LIBRO   ")
        criterio = input("Buscar por (ID/Título): ").lower()
        
        if criterio == 'id':
            id_libro = input("Ingrese el ID del libro: ")
            if id_libro in biblioteca:
                libro = biblioteca[id_libro]
                print("\nLibro encontrado:")
                print(f"ID: {id_libro}")
                print(f"Título: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"Año: {libro['año']}")
            else:
                print("No se encontró un libro con ese ID.")
        elif criterio == 'título' or criterio == 'titulo':
            titulo_buscar = input("Ingrese el título a buscar: ").lower()
            encontrados = False
            
            for id_libro, libro in biblioteca.items():
                if titulo_buscar in libro['titulo'].lower():
                    print("\nLibro encontrado:")
                    print(f"ID: {id_libro}")
                    print(f"Título: {libro['titulo']}")
                    print(f"Autor: {libro['autor']}")
                    print(f"Año: {libro['año']}")
                    encontrados = True
            
            if not encontrados:
                print("No se encontraron libros con ese título.")
    if accion==4:
        print("\n   ACTUALIZAR LIBRO   ")
        id_libro = input("Ingrese el ID del libro a actualizar: ")
        libro = biblioteca[id_libro]
        print("\nInformación actual del libro:")
        print(f"1. Título: {libro['titulo']}")
        print(f"2. Autor: {libro['autor']}")
        print(f"3. Año: {libro['año']}")
        
        campo = input("\n¿Qué campo desea actualizar? (1-3): ")
        
        if campo == '1':
            nuevo_valor = input("Nuevo título: ")
            libro['titulo'] = nuevo_valor
        elif campo == '2':
            nuevo_valor = input("Nuevo autor: ")
            libro['autor'] = nuevo_valor
        elif campo == '3':
            nuevo_valor = input("Nuevo año: ")
            libro['año'] = int(nuevo_valor)

        print("Libro actualizado con éxito!")

    if accion==5:
        print("\n--- ELIMINAR LIBRO ---")
        id_libro = input("Ingrese el ID del libro a eliminar: ")
        
        if id_libro in biblioteca:
            titulo = biblioteca[id_libro]['titulo']
            del biblioteca[id_libro]
            print(f"Libro '{titulo}' eliminado con éxito!")
    if accion==6:
        print("¡Adios!")





