#agregar productos
from aplicacion.consultarElementos import *

#agregar nuevo productos
def agregarNuevoProducto(inventario):
    print("Agregar Nuevo Producto\n")
    
    nombre = input("Nombre: ").replace(".","")
    descripcion = input("Descripcion: ").replace(".","")
    contraindicaciones = input("Contraindicaciones: ").replace(".","")
    precio = input("precio: ")
    grupos = input("grupos(separados por (,)): ").replace(".","").replace(","," ").split()
    requiereFormulacion = input("requiereFormulacion(si | no): ").replace(".","")
    codigo=input("Codigo: ")
    producto = [codigo,nombre,descripcion,contraindicaciones,precio,grupos,requiereFormulacion,1]
    inventario.append(producto)
    return inventario

def agregarProductoExistente(inventario):
    print("Agregar Existencias")
    codigo = input("codigo : ")
    pos = buscarProductoCodigo(inventario,codigo)
    if(pos!=-1):
        existencias = input("existencias : ")
        inventario[pos][-1] = str(int(inventario[pos][-1])+int(existencias))
    else:
        print("El Producto no se encuentra registrado.")
    return inventario

def disminuirProductoExistente(inventario):
    print("Disminuir Existencias")
    codigo = input("codigo : ")
    pos = buscarProductoCodigo(inventario,codigo)
    if(pos!=-1):
        existencias = input("existencias : ")
        inventario[pos][-1] = str(int(inventario[pos][-1])-int(existencias))
    else:
        print("El Producto no se encuentra registrado.")
    return inventario

def borrarProducto(inventario):
    codigo = input("Ingrese el codigo del elemento: ")
    pos = buscarProductoCodigo(inventario,codigo)
    if(pos!=-1):
        inventario.remove(codigo)        
    else:
        print("El Producto no se encuentra registrado.")
    
def guardarDatos(inventario,ruta):
    archivo = open(ruta,'w')
    print(inventario)
    for i in range(1,len(inventario)):
        for j in range(1,len(inventario[i])):
            print(inventario[i][j],"DATO")
            if(j==1):
                archivo.write("Nombre : "+inventario[i][j]+"\n")
            elif(j==2):
                archivo.write("Descripcion : "+inventario[i][j]+"\n")
            elif(j==3):
                archivo.write("Contraindicaciones : "+inventario[i][j]+"\n")
            elif(j==4):
                archivo.write("Precio : "+inventario[i][j]+"\n")
            elif(j==5):
                archivo.write("Grupos : ")
                for k in range(len(inventario[i][j])):
                    if(k<len(inventario[i][j])-1):
                        archivo.write(inventario[i][j][k]+",")
                    else:
                        archivo.write(inventario[i][j][k]+"\n")
            elif(j==6):
                archivo.write("requiereFormulacion(si | no): "+inventario[i][j]+'\n')
        
        archivo.write("Codigo : "+inventario[i][0]+"\n")        
    archivo.close()
