import math
print( "MENU" )
print(" 1 consultar el stock por tipo de juguete")
print(" 2 buscar productos por rango de precios")
print(" 3 actualizar precio de un producto")
print(" 4 agregar un producto , codigo, nombre, marca, edad, tipo, precio y stock")
print(" 5 eliminar un producto por codigo")
print(" 6 ver todos los productos")
print(" 7 buscar un producto por codigo")
print(" 8 salir")

juguetes = {"0.1": ["camion", "lego"],
            "0.2": ["muñeca", "barbie"],
            "0.3" : ["pelota", "futbol"],
            "0.4": ["rompecabezas", "puzzle" ]}

inventario = { "0.1": [500, 5]
                , "0.2": [300, 3]
                , "0.3": [200, 2]
                , "0.4": [400, 4] }

opcion = int(input(" ingrese una opcion:   "))

def buscar_stock ( inventario, stock):
    buscar_nombre = input("ingrese el producto a buscar:     ")
    for codigos, datos in juguetes.items():
        nombre = datos[0]
        if nombre == buscar_nombre:
            stock = inventario[codigos][1]
            print(f" el juguete {juguetes[codigos][0]} tiene en stock {stock} U.")

def buscar_por_rango_precios(inventario, juguetes):
    p_min = int(input("Ingrese el precio mínimo: "))
    p_max = int(input("Ingrese el precio máximo: "))
    for codigo, valores in inventario.items():
        precio = valores[0]
        stock = valores[1]
        if p_min <= precio <= p_max and stock > 0:
                nombre = juguetes[codigo][0]
                print(f" {nombre} cuesta ${precio} y hay {stock} en stock.")   


def actualizar_precio(a):
      nuevo_precio = input("ingrese un el codigo:      ").upper()
      if nuevo_precio in inventario:
            nuevo_actualizado = int(input(" ingrese precio nuevo:     "))
            inventario[nuevo_precio][0] = nuevo_actualizado
            print(f"El precio actualizado de {nuevo_precio} es {nuevo_actualizado}")
def agregar_producto(inventario,juguetes):
       codigo = float(input("ingrese el codigo del producto:    "))

       if codigo in juguetes:
             print("codigo ya existe")
       else:
             codigo= input(" ingrese el codigo del nuevo producto      ")
             nombre= input(" ingrese el nombre del nuevo producto     ")
             marca= input(" ingrese el marca del nuevo producto      ")
             tipo= input(" ingrese el tipo del nuevo producto      ")
             precio= int(input(" ingrese el precio del nuevo producto   "))
             edad= int(input(" ingrese el edad del nuevo producto      "))
             juguetes [codigo]= [codigo,nombre,marca,tipo,edad]
             inventario [codigo]= [codigo,precio]
def eliminar_producto(juguetes, inventario):
    codigo = input("Ingrese el código del producto a eliminar: ")
    if codigo in juguetes or inventario:
          nombre = juguetes[codigo][0]
          del juguetes[codigo]
          del inventario[codigo]
          print(f"el juguete {nombre} ha sido eliminado")
def ver_productos(juguetes):
      for codigos in juguetes:
            print(f"{juguetes[codigos][0]},{inventario[codigos][0]},{inventario[codigos][1]}")

def buscar_porcodigo(juguetes):
      codigo = input("ingrese codigo del producto:   ")
      if codigo in juguetes:
            print(f" el juguete es {juguetes[codigo][0]}")
    
    
                

   




while True:
    if opcion == 1:
            buscar_stock( inventario, juguetes)
    elif opcion == 2:
            buscar_por_rango_precios(inventario, juguetes)
    elif opcion == 3:
            actualizar_precio(inventario)
    elif opcion == 4:
        agregar_producto(inventario,juguetes)
    elif opcion == 5:
        eliminar_producto(juguetes,inventario)
    elif opcion == 6:
        ver_productos(juguetes)
    elif opcion == 7:
        buscar_porcodigo(juguetes)
    elif opcion == 8:
        print("salir")
    break
      
