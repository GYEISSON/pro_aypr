#Modulo principal de la aplicación
from aplicacion.prepareElementos  import *
from aplicacion.menu import *
from aplicacion.agregarProductos import *
from aplicacion.consultarElementos import *

def opcion1(inventario):
    opcion = menuAgregar()
    while(opcion!=3):
        if(opcion ==1):
            inventario = agregarNuevoProducto(inventario)
        elif(opcion==2):
            inventario = agregarProductoExistente(inventario)
        opcion = menuAgregar()
    return opcion

def opcion2(inventario):
    opcion = menuConsultar()
    while(opcion!=6):
        if(opcion ==1):
            codigo=input()
            consultarProductoCodigo(inventario,codigo)
        elif(opcion==2):
            nombre = input()
            consultarProductoNombre(inventario, nombre)
        elif(opcion==3):
            categoria = input()
            consultarProductoCategoria(inventario, categoria)
        elif(opcion==4):
            opcion2Categoria(inventario)
        opcion = menuAgregar()    
    return opcion

def opcion2Categoria(inventario):
    opcion =  menuConsularExistencias()
    while(opcion!=3):
        if(opcion==1):
            consutarProductosAgotados()
        elif(opcion ==2):
            numero=int(input())
            consultarProductosN(numero)
        menuConsularExistencias()

def menu(inventario):
    opcion = menuInicial()
    while(opcion != 5):
        if(opcion ==1):
           opcion=opcion1(inventario)     
        elif(opcion==2):
            opcion2 = opcion2(inventario)        
        elif(opcion==3):
            continue
        elif(opcion==4):
            continue
        opcion = menuInicial()
    print(inventario)
    return menu

def main():
    inventario = prepareElementos()
    ruta='datos.txt'
    inventario = cargarDatos(ruta,inventario)
    menu(inventario)
    
main()


