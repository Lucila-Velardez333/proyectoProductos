
print("**************************************")
print("SELECCIONE UNA OPCION: ")
print("1- agregar productos al inventario")
print("2- mostrar los productos registrados")
print("3- salir")
print("**************************************")

entrada = int(input("ingrese la opcion: "))

frutas= [
    ["naranja",10],["pomelo",3],["sandia",2]
]

while entrada!=0 :                                                                                      

    if(entrada == 1):
        print("ingrese los productos")  
        nombre =  input("Ingrese nombre de la fruta: ")
        stock =  input("Ingrese el stock de la fruta: ")
        nueva_fruta = [nombre,stock]
        frutas.append(nueva_fruta)
        print("Fruta agregada exitosamente.")
    elif(entrada==2):
        print("Frutas registradas: ")
        for fruta in frutas:
            print(f"Fruta:{fruta[0]} - Stock: {fruta[1]}")

    elif(entrada== 0):
        print("hasta pronto")
        break
    else:
        print("Opcion incorrecta")
    
    print("**************************************")
    print("SELECCIONE UNA OPCION: ")
    print("1- agregar productos al inventario")
    print("2- mostrar los productos registrados")
    print("0- salir")
    print("**************************************")

    entrada = int(input("ingrese la opcion: "))


















