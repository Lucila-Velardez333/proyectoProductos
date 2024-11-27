Galletitas = {
    1:{"id": 1, "Nombre":"Cerealitas","stock": 5, "precio":235, "año_de_vencimiento": 2026 },
    2:{"Nombre":"Merengadas","stock": 2, "precio":540, "año_de_vencimiento": 2027},
    3:{"Nombre": "Surtido", "stock": 3, "precio":1280, "año_de_vencimiento": 2030},
}
Golosinas = {
    1:{"nombre":"sugus","stock": 5, "precio":220},
    2:{"Nombre":"Pico dulce","stock": 56, "precio":80},
    3:{"Nombre": "flynn paff", "stock": 250, "precio":20},
}

Productos = {
    "galletitas": Galletitas,
    "golosinas": Golosinas,
}


entrada=-1

while entrada!=0 :                                                                                      
    print("**************************************")
    print("SELECCIONE UNA OPCION: ")
    print("1- agregar productos al inventario")
    print("2- mostrar los productos registrados")
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
        else:
            print("Opcion incorrecta")

    elif(entrada==2):
        print("Productos registrados: ")
        print(Productos["galletitas"])
        print(Productos["golosinas"])
    elif(entrada== 0):
        print("hasta pronto")
        break
    else:
        print("Opcion incorrecta")