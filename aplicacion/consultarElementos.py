#consultar productos



def buscarProductoCodigo(inventario,codigo):
    pos = -1
    for i in range(len(inventario)):
        if(inventario[i][0] == codigo):
            pos = i
            return pos
    return pos

def consultarProductoCodigo(inventario):
    codigo =  input("Codigo : ")
    pos = buscarProductoCodigo(inventario,codigo)
    if(pos !=-1):
        for i in range(1,len(inventario[pos])):    
            print(inventario[0][i]+" : ",inventario[pos][i])
    print()

def consultarProductoNombre(inventario):
    
    nombre = input("ingrese el nombre del producto: ")
    pos = -1
    for i in range(len(inventario)):
        if(inventario[i][1] == nombre):
            pos = i
            break
    if(pos !=-1):
        for i in range(1,len(inventario[pos])):    
            print(inventario[0][i]+" : ",inventario[pos][i])
    print()


def consultarProductoCategoria(inventario):
    categoria = input("ingrese la categoria del producto: ")
    for i in range(1,len(inventario)):
        for j in range(len(inventario[i][5])):
            
            if(inventario[i][5][j]==categoria):        
                for k in range(1,len(inventario[i])):
                    print(inventario[0][k]+" : ",inventario[i][k])
                print()
def consultarProductosAgotados(inventario):
    for i in range(1,len(inventario)):
        if(int(inventario[i][-1]) == 0):
            for k in range(1,len(inventario[i])):
                print(inventario[0][k]+" : ",inventario[i][k])
            print()

def consultarProductosN(inventario):
    numero=int(input("productos con existencias mayores a: "))
    for i in range(1,len(inventario)):
        if(int(inventario[i][-1]) >numero):
            for k in range(1,len(inventario[i])):
                print(inventario[0][k]+" : ",inventario[i][k])
            print()

def consultarTodo(inventario):
    for i in range(1,len(inventario)):
        for k in range(1,len(inventario[i])):
             print(inventario[0][k]+" : ",inventario[i][k])
        print()
