from G_Estudiantes import AddSt,PrintL,SearchSt, ModSt,DelStudent #Import functions from G_Estudiantes archive

#Create the menu
def Menu():
    #while loop to execute menu
    while True:
        print("\n     MENU    ")
        print(" 1. Añadir Estudiante")#Function Add Student
        print(" 2. Consultar Estudiante")#Function Search Student 
        print(" 3. Actualizar precio producto")#Function Update Student 
        print(" 4. Eliminar producto")#Function Delete Student
        print(" 5. Calcular valor total de inventario")
        print(" 6. Ver lista de estudiantes")
        print(" 7. Salir")
        Action = int(input("Ingrese una opción del 1 al 7: "))

        if Action==1:
            AddSt()
        elif Action == 2:
            SearchSt()
        elif Action == 3:
            ModSt()
        elif Action == 4:
            DelStudent()    
        elif Action == 6:
            PrintL()
        elif Action == 7:
            print("Adiós")
            break

Menu()