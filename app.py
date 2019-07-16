#Modulo principal de la aplicación
from aplicacion.prepareElementos  import *
from aplicacion.menu import *
from aplicacion.agregarProductos import *
from aplicacion.consultarElementos import *

def opcion1(inventario):
    opcion = menuAgregar()
    while(opcion!=2):
        if(opcion ==1):
            inventario = agregarNuevoProducto(inventario)
        opcion = menuAgregar()
    return opcion

def opcion2(inventario):
    opcion = menuConsultar()
    while(opcion!=6):
        if(opcion ==1):
            consultarProductoCodigo(inventario)
        elif(opcion==2):
            consultarProductoNombre(inventario)
        elif(opcion==3):
            
            consultarProductoCategoria(inventario)
        elif(opcion==4):
            opcion2Categoria(inventario)
        elif(opcion==5):
            consultarTodo(inventario)
        opcion = menuConsultar() 
    return opcion

def opcion2Categoria(inventario):
    opcion =  menuConsularExistencias()
    while(opcion!=3):
        if(opcion==1):
            consultarProductosAgotados(inventario)
        elif(opcion ==2):
            
            consultarProductosN(inventario)
        opcion = menuConsularExistencias()

def opcion3(inventario):
    opcion = menuEditarProductos()
    while(opcion!=4):
        if(opcion==1):
            inventario = agregarProductoExistente(inventario)
        elif(opcion==2):
            inventario = disminuirProductoExistente(inventario)
        elif(opcion==3):
            inventario =borrarProducto(inventario)
        opcion = menuEditarProductos
            


def menu(inventario):
    opcion = menuInicial()
    while(opcion != 5):
        if(opcion ==1):
           opcion=opcion1(inventario)     
        elif(opcion==2):
            opcion = opcion2(inventario)        
        elif(opcion==3):
            opcion = opcion3(inventario)
        elif(opcion==4):
            ruta='datos.txt'
            guardarDatos(inventario,ruta)        
        opcion = menuInicial()
    return menu

def main():
    inventario = prepareElementos()
    ruta='datos.txt'
    inventario = cargarDatos(ruta,inventario)
    menu(inventario)
    
main()


