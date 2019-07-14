#los siguisntes modulos crearan todos elementos de la aplicacion

def prepareElementos():
    inventario = [["Nombre","Descipcion","Contradicciones",
                  "Precio","Grupos","Requiere formulacion","Existencias"]]
    
    return inventario

def cargarDatos(ruta,inventario):
    archivo= open(ruta,"r")
    line = archivo.readline()
    while(line):
        print(line)
        nombre=descripcion=contradicciones=precio=grupos=requiereFormulacion=existencias=""
        if("Nombre :" in line):
            nombre = line[8:].strip()
            line = archivo.readline()
        if("Descripcion :" in line):
            descripcion = line[13:].strip()
            line = archivo.readline()
        if("Contradicciones :" in line):
            contradicciones = line[15:].strip()
            line = archivo.readline()
        if("Precio :" in line):
            precio = line[8:].strip()
            line = archivo.readline()
        if("Grupos :" in line):
            grupos = line[8:].replace(","," ").strip().split()
            line = archivo.readline()
        if("Requiere formulacion :" in line):
            requiereFormulacion = line[22:].replace(".","").strip()
            line = archivo.readline()
        if("Existencias :" in line):
            existencias = line[13:].strip()
            line = archivo.readline()
        dato = [nombre,descripcion,contradicciones,precio,grupos,requiereFormulacion,existencias]
        inventario.append(dato)
        line = archivo.readline()
        
    return inventario
        
    
