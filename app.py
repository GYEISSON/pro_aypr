#Modulo principal de la aplicación
from aplicacion.prepareElementos  import *
from aplicacion.menu import *
from aplicacion.agregarProductos import *

def menu(inventario):
    
    opcion = menuInicial()
    while(opcion != 5):
        if(opcion ==1):
            opcion = menuAgregar()
            while(opcion!=3):
                if(opcion ==1):
                    inventario = agregarNuevoProducto(inventario)
                elif(opcion==2):
                    inventario = agregarProductoExistente(inventario)
                opcion = menuAgregar()
                
        elif(opcion==2):
            continue
        elif(opcion==3):
            continue
        elif(opcion==4):
            continue
        opcion = menuInicial()
    print(inventario)
    return menu

def main():
    inventario = prepareElementos()
    menu(inventario)
    
main()


