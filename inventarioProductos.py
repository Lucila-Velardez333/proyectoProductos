class Fruta:
    def __init__(self,nombre,stock):
        self.nom= nombre
        self.stock=stock



print("**************************************")
print("SELECCIONE UNA OPCION: ")
print("1- agregar productos al inventario")
print("2- mostrar los productos registrados")
print("0- salir")
print("**************************************")

entrada = int(input("ingrese la opcion: "))
fruta1 = Fruta("naranja",10)
fruta2 = Fruta("pomelo",3)
fruta3 = Fruta("sandia",2)
frutas= [
    fruta1 , fruta2, fruta3
]
k=0
def Mostrar():
    if frutas:
        print("Frutas registradas: ")
        for fruta in frutas:
            print(f"{fruta.nom} - Stock: {fruta.stock}")
    else:
        print("No hay frutas registradas.")

while entrada!=0 :                                                                                      

    if(entrada == 1):
        print("ingrese los productos")  
        nombre =  input("Ingrese nombre de la fruta: ")
        stock =  input("Ingrese el stock de la fruta: ")
        nueva_fruta = Fruta(nombre, stock)
        frutas.append(nueva_fruta)
        print("Fruta agregada exitosamente.")
    elif(entrada==2):
        print("Frutas registradas: ")
        Mostrar()

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


















