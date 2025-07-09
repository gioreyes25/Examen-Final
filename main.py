from funciones import stock_marca,busqueda_precio,actualizar_precio
productos={
    "8475HD":["Hp",15.6,"8GB","DD","1T","Intel Core i5","Nvidia GTX1050"],
    "2175HD":["Lenovo",14,"16GB","SDD","512GB","Intel Core i5","Nvidia GTX1050"],
    "8762HD":["Asus",14,"16GB","DD","256GB","Intel Core i7","Nvidia GTX1050"],
    "2912HD":["Hp",15.6,"8GB","DD","1T","Intel Core i3","Nvidia RTX2080Ti"],
    "7452HD":["Asus",14,"4GB","DD","1T","Intel Core i5","Integrada"],
    "3242HD":["Lenovo",15.6,"4GB","DD","1T","ADM Ryzen 5","Nvidia GTX1050"],
    "6652HD":["Lenovo",15.6,"8GB","DD","1T","Adm Ryzen 7","Integrada"],
    "1202HD":["Dell",15.6,"8GB","DD","1T","Adm Ryzen 3","Nvidia GTX1050"],
}
stock={
    "8475HD":[389900,10],
    "2175HD":[299000,5],
    "8762HD":[199900,20],
    "2912HD":[499990,0],
    "7452HD":[799990,6],
    "3242HD":[389900,13],
    "6652HD":[389900,8],
    "1202HD":[389900,5],
}
while True:
    print(stock)
    print("1. Srock Marca")
    print("2. Busqueda Por Precio")
    print("3. Actualizar Precio")
    print("4. Salir")
    try:
        op=int(input("Ingrese una opcion: "))
    except: ValueError
    print("Ingrese una opcion Valida")
    match op:
        case 1:
            marca=input("Ingrese marca que desea buscar: ").capitalize()
            stock_marca(productos,stock,marca)
        case 2:
            while True:
                try:
                    p1=int(input("Ingrese rango de precio min: "))
                    p2=int(input("Ingrese rango de precio max: "))
                    break
                except: ValueError
                print("Solo se permiten numeros enteros")
            busqueda_precio(productos,stock,p1,p2)
        case 3:
            modelo=input("Ingrese modelo a buscar: ").upper()
            precio=int(input("Ingrese el nuevo precio: "))
            actualizar_precio(productos,stock,modelo,precio)
            while True:
                si=input("Desea volver a cambiar de precio otro modelo (Si o No): ").capitalize()
                if si =="Si":
                    modelo=input("Ingrese modelo a buscar: ").upper()
                    precio=int(input("Ingrese el nuevo precio: "))
                    actualizar_precio(productos,stock,modelo,precio)
                else:
                    break
        case 4:
            print("Programa Finalizado")
            break
                
            
            