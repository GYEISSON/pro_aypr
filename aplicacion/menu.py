#Menu Inicio


        
def menuInicial():
    print("INVENTARIO GROGUERIA\n")
    print("1 Agregar productos")
    print("2  Consultar productos" )
    print("3 Editar productos")
    print("4 Guardar en archivo")
    print("5 Salir")
    num = int(input())
    return num

def menuAgregar():
    print("MENU AGREGAR PRODUCTOS\n") 
    print("1 Agregar nuevo producto")
    print("2 Agregar existencias")
    print("3 para volver al menu anterior")
    num = int(input())
    return num
