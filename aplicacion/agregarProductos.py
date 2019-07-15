#agregar productos
from aplicacion.consultarElementos import *

#agregar nuevo productos
def agregarNuevoProducto(inventario):
    print("Agregar Nuevo Producto\n")
    
    nombre = input("Nombre: ").replace(".","")
    descripcion = input("Descripcion: ").replace(".","")
    contradicciones = input("Contradicciones: ").replace(".","")
    precio = float(input("precio: "))
    grupos = input("grupos(separados por (,)): ").replace(".","").split()
    requiereFormulacion = input("requiereFormulacion(si | no): ").replace(".","")
    codigo=input("Codigo: ")
    if("si" in requiereFormulacion): requiereFormulacion = True
    else: requiereFormulacion = False
    
    producto = [codigo,nombre,descripcion,contradicciones,precio,grupos,requiereFormulacion,1]
    inventario.append(producto)
    return inventario

def agregarProductoExistente(inventario):
    print("Agregar Producto Existente")
    codigo = input("codigo : ")
    pos = buscarProductoCodigo(inventario,codigo)
    if(pos!=-1):
        existencias = input("existencias : ")
        inventario[pos][-1] = str(int(inventario[pos][-1])+int(existencias))
    else:
        print("El Producto no se encuentra registrado.")
    return inventario
