import sqlite3
def insertar():
    db1=sqlite3.connect('productos.db')
    print ('estas en la funcion insertar')
    
    nombre1=input('ingresa producto ')
    calorias1=input('ingresa calorias ')#raw_input acepta caracteres y numeros
    sodio1=str(input('ingresa sodio '))#=str solo acepta numeros y lo almacena como string, sin str no se puede concatenar con los otros string"texto
    
    consulta=db1.cursor()
    strConsulta='insert into tabla(nombre,calorias,sodio)values("'+nombre1+'","'+calorias1+'","'+sodio1+'")'#ojo inser into debe estar en ingles y  las comillas y comas flotantes son como parentesis y escribir todo en la misma linea tambien
    print (strConsulta)
    consulta.execute(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()
def consultar():
    db2=sqlite3.connect('productos.db')#enlace a productos
    
    db2.row_factory=sqlite3.Row#preparar consulta
    consulta=db2.cursor()#habilita coneccion con metodo cursor
    consulta.execute('select*from tabla')#ejecuta la instruccion sql
    filas=consulta.fetchall()#metodo fetchall para guarda resultado de consulta
    lista=[]#crea lista vacia
    for fila in filas:#for hace un arreglo para agregar los registros
        s={}
        s['nombre']=fila['nombre']
        s['calorias']=fila['calorias']
        s['sodio']=fila['sodio']###str(fila['xxxx numero como caracter
        lista.append(s)
    consulta.close()
    db2.close()
    return (lista)
#consultar()linea 34
def plato():
    db3=sqlite3.connect('productos.db')#enlace a productos
    db3.row_factory=sqlite3.Row#preparar calorias
    prod1=input('\ningresa producto\n')
    prod2=input('con\n')
    calorias=db3.cursor()#habilita coneccion con metodo cursor
    calorias.execute('select*from tabla')#ejecuta la instruccion sql
    filas=calorias.fetchall()#metodo fetchall para guarda resultado de calorias
    lista=[]#crea lista vacia
    for fila in filas:#for hace un arreglo para agregar los registros
        s={}
        s['nombre']=fila['nombre']
        s['calorias']=fila['calorias']
        s['sodio']=fila['sodio']###str(fila['xxxx  numero como caracter
        if prod1==s['nombre']:
            k1=int(s['calorias'])
            na1=int(s['sodio'])
            
        if prod2==s['nombre']:
            k2=int(s['calorias'])
            na2=int(s['sodio'])
            
        #lista.append(s)
        
    calorias.close()
    na=na1+na2
    print (k1+k2,' calorias y ',na,' en sodio')
    db3.close()
    return (lista)
def menu():
    Opcion=input('\nIngresa la opcion deseada\n1.Consultar calorias y sodio del plato\n2.Ingresar nuevo producto\n3.Ver todos los productos de la base de datos\nIngrese otro numero para salir\n')
    if Opcion==1:
        
        ListaProductos=plato()#te envia a def plato
        
        #for producto in ListaProductos:
            #print(producto['nombre'])imprime cada producto de la lista de la base datos
        menu()#te mantiene en el menu
    elif Opcion==2:
        insertar()
        menu()
    elif Opcion==3:
        print('Producto','Calorias','Sodio')
        ListaProductos=consultar()
        for producto in ListaProductos:
            print(producto['nombre'],producto['calorias'],producto['sodio'])#la u antes del nombre indica que es texto
        menu()
    
menu()

