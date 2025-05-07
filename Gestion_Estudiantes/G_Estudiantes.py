#EStudiantes debe tener ID,Nombre,Edad, Notas
Students={ "100": {"Name": "Juan","Age":"17","Note":"3.0"},
             "200": {"Name": "Esteban","Age":"19","Note":"5.0"},
             "300": {"Name": "Johan","Age":"22","Note":"4.0"},
            "400":{"Name": "Daniel","Age":"18","Note":"2.0"},
             "500":{"Name": "Cristian","Age":"24","Note":"2.8"},
             
             }
NotasB=[]

#Function for add Student
def AddSt():
    print("     AÑADIR ESTUDIANTE     ")
    while True:
        ID = int(input("Ingrese el ID del estudiante: "))#Enter ID
        ID=str(ID)
        if ID in Students:#contidion "if" for     
            print(f"Estudiante con ID {ID} está en la lista")
        else:
            Name = input("Ingrese el nombre completo del estudiante: ").lower()#Enter name
            Age = int(input("Ingrese la edad del estudiante: "))#Enter age
            Note = float(input("Ingrese la nota del estudiante: "))#Enter note
            Students[ID] = {'Name': Name, 'Age': Age, "Note": Note}
            print(f"Estudiante con ID '{ID}'  llamado {Name} añadido correctamente.")
        
        
        print(Students)

        conti=input("¿Desea ingresar otro producto? si/no ").lower()
        if conti=="no":
            break
#Function for print dictionary
def PrintL():
    print("\n     INVENTARIO DISPONIBLE       ")
    print(Students)


#Function for search student
def SearchSt():
    print("\n     BUSCAR ESTUDIANTE      ")
    Select = input("Buscar por (ID/Nombre): ").lower()
    while True:
             
        if Select == 'id':
            Id_St = input("Ingrese el ID del estudiante: ")
            if Id_St in Students:
                    Stu = Students[Id_St]
                    print("\033[32m\nEstudiante encontrado: \033[0m")#
                    print(f"ID: {Id_St}")
                    print(f"Nombre: {Stu['Name']}")
                    print(f"Edad: {Stu['Age']}")
                    print(f"Nota: {Stu['Note']}")
            else:
                    print("No se encontró un libro con ese ID.")
        elif Select == 'nombre':
                Name_Search = input("Ingrese el nombre completo del estudiante a buscar: ")
                find = False
                
                for Id_St, Stu in Students.items():
                    if Name_Search in Stu['Name']:
                        print("\nLibro encontrado:")
                        print(f"ID: {Id_St}")
                        print(f"Nombre: {Stu['Name']}")
                        print(f"Edad: {Stu['Age']}")
                        print(f"Nota: {Stu['Note']}")
                        find = True
                
                if not find:
                    print("No se encontro un estudiante con ese nombre.")
        conti=input("¿Desea ingresar otro estudiante si/no ").lower()
        if conti=="no":
            break
        
            
            
            
       
        
def ModSt():
     while True:
        ID = int(input("Ingrese el ID del estudiante al que le desea modificar la nota: "))#Enter ID
        ID=str(ID)
        if ID in Students:
             NoteMod=Students[ID]
             print("\nInformación actual del estudiante: ")
             print(f"ID: {ID}")
             print(f"Nombre: {NoteMod['Name']}")
             print(f"Edad: {NoteMod['Age']}")
             print(f"Nota: {NoteMod['Note']}")
             new_value=input("Ingrese el nuevo valor de la nota: ")
             NoteMod["Note"]=new_value
             print("\033[32m\nNota actualizada con exito: \033[0m")
             print(f"ID: {ID}")
             print(f"Nombre: {NoteMod['Name']}")
             print(f"Edad: {NoteMod['Age']}")
             print(f"Nota: {NoteMod['Note']}")
        conti=input("¿Desea ingresar otro producto? si/no ").lower()
        if conti=="no":
            break

def DelStudent():
    print("\n     ELIMINAR ESTUDIANTE      ")
    while True:

        Id_St = input("Ingrese el ID del estudiante que desea eliminar: ")
        if Id_St in Students:
            Stu = Students[Id_St]
            print("\033[32m\nEstudiante encontrado: \033[0m")#
            print(f"ID: {Id_St}")
            print(f"Nombre: {Stu['Name']}")
            print(f"Edad: {Stu['Age']}")
            print(f"Nota: {Stu['Note']}")
            StDel=input(f"¿Desea eliminar el estudiante con ID {Id_St} si/no:  ").lower()
            if StDel=="si":
                del Students[Id_St]
                print("EStudiante eliminado con exito")
        else:
                        print("No se encontró un libro con ese ID.")
        conti=input("¿Desea eliminar otro estudiante si/no ").lower()
        if conti=="no":
            break
    
def PromNotes():
     while True:
          TotalN=0
          Note1=Students["Notes"]
          for Notes in Students.items():
               print()
               
             
             
             



        