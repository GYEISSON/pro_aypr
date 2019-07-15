#los siguisntes modulos crearan todos elementos de la aplicacion

def prepareElementos():
    inventario = [["Codigo","Nombre","Descipcion","Contraindicaciones",
                  "Precio","Grupos","Requiere formulacion","Existencias"]]
    
    return inventario

def cargarDatos(ruta,inventario):
    archivo= open(ruta,"r")
    line = archivo.readline()
    while(len(line)>1):
        print(line)
        codigo=nombre=descripcion=contradicciones=precio=grupos=requiereFormulacion=existencias=""
        if("Nombre :" in line):
            nombre = line[8:].strip()
            line = archivo.readline()
        if("Descripcion :" in line):
            descripcion = line[13:].strip()
            line = archivo.readline()
        if("Contraindicaciones :" in line):
            contradicciones = line[21:].strip()
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
        if("Codigo :" in line):
            codigo = line[8:].strip()
                 
        dato = [codigo,nombre,descripcion,contradicciones,precio,grupos,requiereFormulacion,existencias,codigo]
        print(dato)
        inventario.append(dato)
        line = archivo.readline()
    archivo.close()
    return inventario
        
    
