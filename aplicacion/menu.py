#Menu Inicio


        
def menuInicial():
    print("INVENTARIO GROGUERIA\n")
    print("1 Agregar productos")
    print("2 Consultar productos" )
    print("3 Editar productos")
    print("4 Borrar un producto por codigo de barras.")
    print("5 Guardar en archivo")
    print("6 Salir")
    num = int(input())
    return num

def menuAgregar():
    print("MENU AGREGAR PRODUCTOS\n") 
    print("1 Agregar nuevo producto")
    print("2 para volver al menu anterior")
    num = int(input())
    return num

def menuConsultar():
    print("MENU CONSULTAR INVENTARIO\n")
    print("1 Consultar por codigo de barras.")
    print("2 Consultar por nombre.")
    print("3 Consultar por categoria.")
    print("4 Consultar por existencias.")
    print("5 Consultar todos.")
    print("6 para volver al menu anterior")
    num = int(input())
    return num

def menuConsularExistencias():
    print("MENU CONSULTAR POR EXISTENCIAS")
    print("1 Consultar productos agotados.")
    print("2 Consultar productos superiores a N.")
    print("3 para volver al menu anterior")
    num = int(input())
    return num

def menuEditarProductos():
    print("MENU EDITAR PRODUCTOS")
    print("1 Agregar existencias")
    print("2 Disminuir existencias")
    print("3 Editar informacion")
    print("4 para volver al menu anterior")
    num = int(input())
    return num
    
