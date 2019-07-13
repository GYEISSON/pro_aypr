#agregar productos

#agregar nuevo productos
def agregarNuevoProducto(inventario):
    print("Agregar Nuevo Producto\n")
    
    nombre = input("Nombre: ").replace(".","")
    descripcion = input("Descripcion: ").replace(".","")
    contradicciones = input("Contradicciones: ").replace(".","")
    precio = float(input("precio: "))
    grupos = input("grupos(separados por (,)): ").replace(".","").split()
    requiereFormulacion = input("requiereFormulacion(si | no): ").replace(".","")

    if("si" in requiereFormulacion): requiereFormulacion = True
    else: requiereFormulacion = False
    
    producto = [nombre,descripcion,contradicciones,precio,grupos,requiereFormulacion,1]
    inventario.append(producto)
    return inventario

def agregarProductoExistente(inventario):
    return inventario
