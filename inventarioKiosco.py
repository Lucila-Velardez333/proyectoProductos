Galletitas = {
    1:{"Nombre":"Cerealitas","stock": 5, "precio":235, "año_de_vencimiento": 2026},
    2:{"Nombre":"Merengadas","stock": 2, "precio":540, "año_de_vencimiento": 2027},
    3:{"Nombre": "Surtido", "stock": 3, "precio":1280, "año_de_vencimiento": 2030},
}
Golosinas = {
    1:{"Nombre":"sugus","stock": 5, "precio":220},
    2:{"Nombre":"Pico dulce","stock": 56, "precio":80},
    3:{"Nombre": "flynn paff", "stock": 250, "precio":20},
}

Productos = {
    "galletitas": Galletitas, #se considera una categoria cuando no tiene clave
    "golosinas": Golosinas,
}


entrada=-1


def mostrar():
    #for + lo que quieres acceder + in + la estructura a recorrer.
    for categoria, producto in Productos.items():
        for clave,  prod in producto.items():
            if ("año_de_vencimiento" in prod) and (prod != " "):
                print("Galletitas: ")
                print(f"Nombre: {prod["Nombre"]}" )
                print(f"stock:  {prod["stock"]} ")
                print(f"precio:  {prod["precio"]} ")
                print(f"Año de vencimiento:  {prod["año_de_vencimiento"]} ")
            elif (prod != " ") :
                print("Golosinas: ")
                print(f"Nombre:  {prod["Nombre"]} ")
                print(f"stock:  {prod["stock"]} ")
                print(f"precio: {prod["precio"]} ")
            else:
                print("Nose encontro productos")


while entrada!=0 :                                                                                      
    print("**************************************")
    print("SELECCIONE UNA OPCION: ")
    print("1- agregar productos al inventario")
    print("2- mostrar los productos registrados")


    print("3- mostrar un producto ")
    print("4- eliminar los productos registrados")
    print("5- eliminar un producto ")
    print("6- Modificar los productos registrados")
    print("7- Modificar un producto registrado")
    print("8- Buscar un productos ")
    print("0- salir")
    print("**************************************")
    entrada = int(input("ingrese la opcion: "))
    
    if(entrada == 1):
        print("¿Que producto desea agregar?")
        print("1- agregar galletitas")
        print("2- agregar golosinas")
        print("0- volver atras")
        eleccion = int(input("Ingrese la opcion: "))  

        if(eleccion == 1):
            nombre =  input("Ingrese nombre de la galletita: ")
            stock =  int(input("Ingrese el stock de la galletita: "))
            precio = int( input("Ingrese el precio de la galletita: "))
            vencimiento =  input("Ingrese el año de vencimiento de la galletita: ")

            nueva_clave= len(Productos["galletitas"]) +1
            Productos["galletitas"][ nueva_clave]= {"nombre": nombre, "stock":stock,"precio": precio, "año_de_vencimiento": vencimiento}
            print("Galletita agregada exitosamente.")
        elif(eleccion == 2):
            nombre =  input("Ingrese nombre del fruta: ")
            stock =  int(input("Ingrese el stock del fruta: "))
            precio = int( input("Ingrese el precio de la golosina: "))

            nueva_clave= len(Productos["golosinas"]) +1
            Productos["golosinas"][ nueva_clave]= {"nombre": nombre, "stock":stock,"precio": precio}
            print("Golosina agregada exitosamente.")
        elif(eleccion == 3):
            print("")
        elif(eleccion == 4):
            print("")

        elif(eleccion == 5):
             print("")
        elif(eleccion == 6):
            print("")

        
        elif(eleccion == 7):
            print("")

        elif(eleccion == 8):
             print("")

        else:
            print("Opcion incorrecta")

    elif(entrada==2):
        print("Productos registrados: ")
        mostrar()
        print(Productos["galletitas"])
        print(Productos["golosinas"])



    elif(entrada== 0):
        print("hasta pronto")
        break
    else:
        print("Opcion incorrecta")