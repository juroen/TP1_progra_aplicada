"""
Creador: Juan Rodolfo Enrique Alarcon Alpa  

"""

class Myarray1():
    
    def __init__ ( self , lista , r , c , by_row ) : 
        """
        Metodo Creador de instancia de la Myarray1, cada instancia es una matriz escrita de esta manera

        La lista solo puede ser lista sin otras listas adentro solo int o float, /// tipo list///
        La lista contiene todos los elementos de la matriz


        r cantidad de filas de la matriz  /// tipo int///

        c cantida de columnas de la matriz  /// tipo int///

        by_row  indica de que manera esta creada la lista: /// tipo bool///
        
        Si va en un sentido horizontal,  linea por linea de la matriz en True

        Si va en un sentido vertical, columna por columna de la matriz es False        


        """

        if type(r) == int and type(c) == int and type(by_row) == bool:
            
        
            #aca se corrobora que los parametros de entrada del metodo sean los requeridos para crear la instancia
            sigue = True
            for x in lista:
                # Corroboro que todos los elementos de lista sean los requeridos
                if type(x) != float:
                    if type(x) != int:
                        sigue  =  False
                if sigue:
                    self.lista  = lista   
                    self.r  = r  
                    self.c  = c   
                    self.by_row = by_row  
        else:
            print ('CREANDO UNA INSTANCIA NO VALIDA')
    
    """
        YA QUE CADA INSTANCIA CREADA TIENE DOS FORMAS DE ESTAR EXPRESADA SIENDO LA MISMA.

        A PARTIR DE ESTE PUNTO LA MAYORIA DE LOS METODOS TIENEN UNA FORMA DE FUNCIONAR

        DEPENDIENDO DEL TIPO DE MATRIZ QUE SE LE ENVIE PARA USAR

        a partir de esto entre en un trade off:
         
        por ejemplo uno era:
         
             agregar mas lineas de codigo y reducir la cantidad de returns o reducir las lineas y usar dos returns

             entre otros. 

        Dependiendo del caso tome diferentes decisiones acorde el metodo y el contexto competente
    
    """


    def get_pos ( self , j , k ):
        """
        Este metodo toma las coordenadas
        
        j   = Fila   /// tipo int///  desde 1 hasta la cantidad de filas n EXCLUSIVAMENTE

        k   = Columna  /// tipo int///    desde 1 hasta la cantidad de columnas n EXCLUSIVAMENTE
        
        en la matriz y devuelve la posicion m asociada en la lista elems
        
        en caso de poner valores fuera de los limites el metodo no funciona
         
        en este caso tomo que 

        m tiene valores entre    0  y   n = len(lista)-1

        """
        if 0 < j  <= self.r   and    0 < k  <=  self.c :
            if self . by_row:
                return ( j - 1 ) * self.c +  ( k - 1 )
            else:
                return ( k - 1 ) * self.r + ( j - 1 )
        else:
            print('VALORES FUERA DE LA MATRIZ')

    def get_coords ( self , m ) :
        """
        toma una posicion m en la lista y devuelve en forma de tupla las
        
        coordenadas j (filas),k(columnas) correspondientes en la matriz.

        en este caso tomo que 

        m /// tipo int ///tiene valores entre    0  y   n = len(lista)-1 EXCLUSIVAMENTE

        """
        if 0 < m < len ( self . lista ):
            if self . by_row:
                j = m // self.c + 1
                k = m % self.c + 1
                return ( j , k )
            else: 
                k = m // self.r + 1
                j = m % self.r + 1
                return ( j , k )
        else:
            print('Valor fuera del rango')
    
    def switch ( self ) :
        """
        Es un metodo que devuelve un objeto con la misma matriz, pero
        alterando la lista elems y cambiando el valor de verdad de by_row.
        
        En esta caso me vi obligado a utilizar dos returns
        
        """
        if self . by_row:
            new = []
            for line in range ( self . c ):
                for value in range ( line , len ( self . lista ), self.c ):
                    new . append ( self. lista [value] )
            return Myarray1( new , self.r , self.c , False )
        
        elif self . by_row == False:
            new = []
            for line in range ( self.r ):
                for value in range ( line , len ( self. lista ) , self.r ):
                    new . append ( self . lista [value] )            
            return Myarray1 ( new , self.r , self.c , True )
    

    def get_row (self , j_ ):
        """
        Este metodo retorno el valor de una/s fila/s de la matriz seleccionada con el/los valor/es j de entrada
        
        j_: puede ser de tipo:
                    ///int o list/// EXCLUSIVAMENTE                 
                
        En caso que algun valor de j no se encuentre en el rando adecuado a la matrix 
        se muestra un error en el valor

        Siempre devuelve una lista de lista ya que esta preparada para devolver varias listas que serian varias filas
        
        """
        if type ( j_ ) == int:
            j = list ( j_ )
                
        if type ( j_ )  == list :
            seguir = True
            j= j_.copy()
            for entradas  in  j:
                if type ( entradas ) != int:
                    seguir = False
                if entradas <= 0 or entradas >  self.r :
                    seguir = False
            if seguir :                    
                nuevo, coco= self.cambio_inicial(True)  
                total = []
                for letra in j:
                    ram = []
                    for i in range (letra-1 ,  len(self.lista) , self.c ):
                        ram . append ( nuevo . lista [i]  )
                    total . append(ram)
                print(total)
                return total
            if seguir == False:
                print ('VALORES FUERA DEL RANGO ESTABLECIDO')
        else:
            print ('VALORES FUERA DEL RANGO ESTABLECIDO')
   
    def get_col ( self , k_):
        """
        Este metodo retorno el valor de una/s cloumnas/s de la matriz seleccionada con el/los valor/es k de entrada

        k_: puede ser de tipo:
                    ///int o list/// EXCLUSIVAMENTE   

        En caso que algun valor de k no se encuentre en el rando adecuado a la matrix 
        se muestra un error en el valor

        Siempre devuelve una lista de lista ya que esta preparada para devolver varias listas que serian varias columnas
        
        """
        if type ( k_ ) == int:
            k = list ( k_ )
        
        if type ( k_ )  == list :
            seguir = True
            k = k_.copy()
            for entradas  in  k:
                if type ( entradas ) != int:
                    seguir = False
                if entradas <= 0 or entradas >  self.c :
                    seguir = False
            if seguir : 
                nuevo, coco= self.cambio_inicial(False)  
                total = []
                for letra in k:
                    ram = []
                    for i in range (letra-1,len(nuevo.lista),nuevo.r):
                        ram . append ( nuevo . lista [i]  )
                    total . append(ram)
                print(total)
                return total
            if seguir == False:
                print ('VALORES FUERA DEL RANGO ESTABLECIDO')
        else:
            print ('VALORES FUERA DEL RANGO ESTABLECIDO')
      

    def get_elem ( self , j , k ):
        
        """
        Este metodo toma las coordenadas
        
        j   = Fila   /// tipo int///  desde 1 hasta la cantidad de filas n EXCLUSIVAMENTE

        k   = Columna   /// tipo int///   desde 1 hasta la cantidad de columnas n EXCLUSIVAMENTE
        
        en la matriz y devuelve el elemnto en la posicion solicitada de la matriz
        
        en caso de poner valores fuera de los limites el metodo no funciona
         

        """
        if type (j) == int and type (k) == int:
            if  0 < j  <= self.r   and    0 < k  <=  self.c :
                return self . lista [ self . get_pos (j , k) ]

        else:
            print('VALORES FUERA DE LA MATRIZ')
    
    def cambio_inicial ( self, okay ):
        """
        posible funcion  a usar
        """
        if self.by_row == okay:            
            nuevo= self.switch()
            cambiar = True
        else:   
            nuevo = self.co_py()  
            cambiar=False
        return nuevo,cambiar


    def del_row ( self , j_):
        """
        Este metodo retorno una matriz seleccionada eliminando la fila con el valor j de entrada
        
        j_: puede ser de tipo:
                    ///int o list/// EXCLUSIVAMENTE                 
                
        En caso que algun valor de j no se encuentre en el rando adecuado a la matrix 
        se muestra un error en el valor

        
        """
        
        if type ( j_ ) == int:
            j = [j_]
            seguir = True    
        elif type ( j_ )  == list :
            j= j_.copy()
            seguir = True
           
        for entradas  in  j:            
            if type ( entradas ) != int:
                seguir = False
            if entradas <= 0 or entradas >  self.r:
                seguir = False
        if seguir :
            nuevo, coco= self.cambio_inicial(False)                
            new= nuevo.lista
            j.sort(reverse=True)
            for letra in j:
                for X in range( (letra-1) * self.c + self.c - 1  ,   (letra-1) * self.c - 1  ,  -1):
                    new.pop(X)                
            nuevo.lista = new
            nuevo.r = nuevo.r-1  
                         
            if coco:           
                nuevo = nuevo.switch()                  
            return nuevo
        if seguir == False:
            print ('VALORES FUERA DEL RANGO ESTABLECIDO')
        else:
            print('VALORES FUERA DE LA MATRIZ')
    
    def del_col(self,k_) :
        
        """
        Este metodo retorno una matriz seleccionada eliminando la fila con el valor j de entrada
        
        k_: puede ser de tipo:
                    ///int o list/// EXCLUSIVAMENTE                 
                
        En caso que algun valor de j no se encuentre en el rando adecuado a la matrix 
        se muestra un error en el valor

        
        
        """
        
        if type ( k_ ) == int:
            k = [k_]
            seguir = True
                
        if type ( k_)  == list:
            seguir = True
            k= k_.copy()
        
        for entradas  in  k:
            if type ( entradas ) != int:
                seguir = False
            if entradas <= 0 or entradas >  self.c:
                seguir = False
        if seguir :
            nuevo, coco= self.cambio_inicial(True)                
            new= nuevo.lista.copy()
            k.sort(reverse=True)
            for letra in k:
                for X in range( (letra-1) * self.r + self.r - 1  ,   (letra-1) * self.r - 1  ,  -1):
                    new.pop(X)                
            nuevo.lista = new
            nuevo.c = nuevo.c-1  
            
            if coco:           
                nuevo = nuevo.switch() 

            return nuevo
        if seguir == False:
            print ('VALORES FUERA DEL RANGO ESTABLECIDO')
        else:
             print('VALORES FUERA DE LA MATRIZ')

    def swap_rows(self,j,k):
       
        """
       
        Este metodo retorno una matriz seleccionada intercambiando  la fila j con la fila K que son valores  de entrada
        
        j   = Fila  1 /// tipo int///  desde 1 hasta la cantidad de filas n EXCLUSIVAMENTE

        k   = fila 2   /// tipo int///   desde 1 hasta la cantidad de filas n EXCLUSIVAMENTE     

        j tiene que si o si ser diferente de k sino muestra un cartel de que no son valores adecuados            
                
        En caso que algun valor de j o k no se encuentre en el rango adecuado de la matrix 
        se muestra un error en el valor
       
        """
        
        if type (j) == int and type (k) == int:
            if  0 < j  <= self.r   and    0 < k  <=  self.r :
                if j != k:
                    nuevo, coco= self.cambio_inicial(False)                
                    new = nuevo.lista.copy()   
                    mi = min(j,k)
                    ma = max(j,k)                    
                    for X in range( (mi-1)*self.c , (mi-1)* self.c + self.c ):                        
                        Z= new[X]
                        new[X]= new [ X + (ma-mi)* self.c]
                        new[X + (ma-mi)* self.c]= Z
                    nuevo.lista = new
                    if coco:
                        nuevo = nuevo.switch()
                    return nuevo                    
                else:
                    print(' valores no permitidos')
            else:   
                print(' valores no permitidos')
        else:
            print(' valores no permitidos')

    def swap_cols(self,l,m) :
        
        """
       
        Este metodo retorno una matriz seleccionada intercambiando  la columna j con la columna K que son valores  de entrada
        
        j   = columna  1 /// tipo int///  desde 1 hasta la cantidad de columnas n EXCLUSIVAMENTE

        k   = columna 2   /// tipo int///   desde 1 hasta la cantidad de columnas n EXCLUSIVAMENTE     

        j tiene que si o si ser diferente de k sino muestra un cartel de que no son valores adecuados            
                
        En caso que algun valor de j o k no se encuentre en el rango adecuado de la matrix 
        se muestra un error en el valor
       
        """
        if type (l) == int and type (m) == int:
            if  0 < l  <= self.c   and    0 < m  <=  self.c :
                if l != m:
                    nuevo, coco =  self . cambio_inicial(True)                
                    new = nuevo . lista . copy() 
                                        
                    mi = min ( l , m )
                    ma = max ( l , m )                    
                    
                    for X in range( (mi-1) * self.r  , (mi-1) * self.r + self.r ):                        
                        Z = new [ X ]
                        new [X] = new [ X + (ma-mi)* self.r]
                        new [X + (ma-mi)* self.r]= Z
                    nuevo.lista = new
                    if coco:
                        nuevo = nuevo.switch()
                    return nuevo                    
                else:
                    print(' valores no permitidos')
            else:   
                print(' valores no permitidos')
        else:
            print(' valores no permitidos')
   
    def scale_row(self,j,x):
        """
        Este metodo retorno una matriz seleccionada multiplocando la fila j con el valor  x que son valores  de entrada
        
        j   = fila  1 /// tipo int///  desde 1 hasta la cantidad de filas n EXCLUSIVAMENTE

        x    /// tipo int o float///  cualquier valor dentro de esos tipos de variables EXCLUSIVAMENTE     
               
        En caso que algun valor de j o x no cumpla las condiciones adecuadas
        se muestra un error en el valor
       
        """


        if type(x) == float or type(x) == int:
            if type (j) == int:
                if  0 <  j  <= self.r:
                    nuevo, coco =  self . cambio_inicial(True)                
                    new = nuevo . lista . copy()                     
                    for X in range( (j-1)*self.c , (j-1)* self.c + self.c ):
                        new[X]= new[X] * x                    
                    nuevo.lista = new
                    
                    if coco:
                        nuevo = nuevo.switch()
                    return nuevo
                else:
                    print(' valores no permitidos')
            else:   
                print(' valores no permitidos')
        else:
            print(' valores no permitidos')

    def scale_col(self,k,y):
        """
        Este metodo retorno una matriz seleccionada multiplocando la columna k con el valor  y que son valores  de entrada
        
        k   = columna  1 /// tipo int///  desde 1 hasta la cantidad de columnas n EXCLUSIVAMENTE

        y   /// tipo int o float///  cualquier valor dentro de esos tipos de variables EXCLUSIVAMENTE     
               
        En caso que algun valor de k o y no cumpla las condiciones adecuadas
        se muestra un error en el valor
       
        """
                
        if type(y) == float or type(y) == int:
            if type (k) == int:
                if  0 <  k  <= self.c:
                    nuevo, coco =  self . cambio_inicial(False)                
                    new = nuevo . lista . copy()                     
                    for X in range( (k-1)*self.r , (k-1)* self.r + self.r  ):
                        new[X]= new[X] * y                    
                    nuevo.lista = new                    
                    if coco:
                        nuevo = nuevo.switch()
                    return nuevo
                else:
                    print(' valores no permitidos')
            else:   
                print(' valores no permitidos')
        else:
            print(' valores no permitidos')

    def transpose(self) :
        """
        Este metodo retorna una matriz seleccionada traspuesta
       
        """
        z = self.r
        self.r = self.c
        self.c = z
        if self.by_row == False:            
            self.by_row= True
        else:   
            self.by_row = False
        nuevo= self.co_py()
        return nuevo
    
    def flip_cols(self):        
        """
        este metedo devuelve una copia del elemento de la clase,
        
        reflejado especularmente en sus columnas        
        
        """
        nuevo, coco =  self . cambio_inicial(True)               
        new=[]
        for X in range ( len(nuevo) - self.r  ,  -1   ,  - self.r ):            
            for Y in range ( X  ,  X + self.r ):                
                new . append ( nuevo [Y] )
        nuevo . lista = new        
        if coco:
            nuevo = nuevo.switch()
        return nuevo
    
    def flip_rows(self) :
        """
        este metedo devuelve una copia del elemento de la clase,
        
        reflejado especularmente en sus filas        
        
        """
        nuevo, coco =  self . cambio_inicial(True)
        new=[]
        for X in range( len(nuevo)- self.c , -1, - self.c ):            
            for Y in range( X , X+ self.c):
                print(new)
                new.append(nuevo[Y])        
        nuevo . lista = new        
        if coco:
            nuevo = nuevo.switch()
        return nuevo
    
    def co_py(self):
        """
        Este metodo tiene simplemente la funcion de devolver una copia del mismo objeto de entrada

        sin aplicar ningun cambio
        
        """
        
        r1=self.r
        c1=self.c
        by_row1=self.by_row
        return Myarray1(self.lista.copy(),r1,c1,by_row1)

    def det(self):
        """
        este metodo devuelve el determinante de la matriz, si es cuadrada.

        y lo calcula a traves del metodo de cofactores

        utilizando recursion      
        
        """
        #siempre como TRUE        
        if self.r  != self.c :
            print ( 'IMPOSIBLE CALCULAR EL DETERMINANTE DE ESTA MATRIZ' )
        else:
            inicial, coco= self . cambio_inicial ( False )    

            if  self.r == 2 and self.c == 2:
                fax = self . lista . copy ()                
                return fax [0] * fax [3] - fax [1] * fax [2]   
                   
            else: 
                final = []
                for j in range(  0, inicial.r  ):  

                    mat_0 = self . co_py()                    
                    mat_1 = mat_0 . del_col((j+1))                    
                    mat_2 = mat_1 . del_row(1)

                    final . append ( ((-1) **(j)) * (inicial . lista [j]) * mat_2.det() )            
            valor = 0
                        
            for numero in final:
                valor = valor + numero
            print ( valor )
            return valor

    def add(self,B):
        
        if type(B) == Myarray1:            
            print("hola hola hola")
            if self.c == B.c and self.r == B.r:
                sumado = []
                for X, Y in zip (self.lista  , B.lista ):
                    sumado.append(X+Y)            
            print(sumado)

        elif type(B) == float or type(B) == int :
            lista = self.lista
            resultado = map(lambda numero: numero + B, lista)
            self.lista=list(resultado)
            print(self.lista)
            return self
        else: 

            print(' valores fuera de rangos permitidos')
   
    def sub(self,B):
        if type(B) == Myarray1:            
            print("hola hola hola")
            if self.c == B.c and self.r == B.r:
                sumado = []
                for X, Y in zip (self.lista  , B.lista ):
                    sumado.append(X-Y)            
            print(sumado)

        elif type(B) == float or type(B) == int :
            lista = self.lista
            resultado = map(lambda numero: numero - B, lista)
            self.lista=list(resultado)
            print(self.lista)
            return self
        else: 
            print(' fuera de los rangoooossss')

    def rprod(self,B):
        if type(B) == Myarray1:            
            if self.c == B.r:
                if B.by_row:            
                    nueva= B.switch().lista
                else:   
                    nueva = B.lista.copy()  
                print(nueva)
                total= []  
                for lineaA in range(0, len (self.lista),self.c):
                    for columnaB in range (0, len(B.lista), B.r):                        
                        listadoA = []
                        listadoB = []
                        suma=0
                        for columnaA in range(lineaA,lineaA+self.c):
                            listadoA.append(self.lista[columnaA])
                        for lineaB in range(columnaB,columnaB+ B.r):
                            listadoB.append(B.lista[lineaB])
                        for X, Y in zip (listadoA  , listadoB ):
                            suma += (X*Y)
                        total.append(suma)        
            print(total)
            return Myarray1(total,self.r, B.c,True)
        
        elif type(B) == float or type(B) == int :
            lista = self.lista
            resultado = map(lambda numero: numero * B, lista)
            self.lista=list(resultado)
            print(self.lista)
            return self
        
        else:
            print('NO ANDUVO')        

    def lprod(self,B):
        if type(B) == Myarray1:            
            if self.r == B.c:
                if self.by_row:            
                    nueva= self.switch().lista
                else:   
                    nueva = self.lista.copy()  
                print(nueva)
                total= []  
                for lineaA in range(0, len (B.lista),B.c):
                    for columnaB in range (0, len(self.lista), self.r):                        
                        listadoA = []
                        listadoB = []
                        suma=0
                        for columnaA in range(lineaA,lineaA+B.c):
                            listadoA.append(B.lista[columnaA])
                        for lineaB in range(columnaB,columnaB+ self.r):
                            listadoB.append(self.lista[lineaB])
                        for X, Y in zip (listadoA  , listadoB ):
                            suma += (X*Y)
                        total.append(suma)        
            print(total)
            return Myarray1(total,B.r, self.c,True)
        
        elif type(B) == float or type(B) == int :
            lista = self.lista
            resultado = map(lambda numero: numero * B, lista)
            self.lista=list(resultado)
            print(self.lista)
            return self
        
        else:
            print('NO ANDUVO')  
    
    def ident(self):
        new=[]
        if self.c ==  self.r:    
            for X in range(0,len(self.lista)):
                new.append(0)
            
            for Y in range (0,len(self.lista),self.c +1):
                new[Y]= 1
            print(new)
        return Myarray1(new, self.r, self.c, True)
           
    def pow(self,n):
        
        if n%2!=0:
            print(self.lista)
            return self
        else:
            if n%2==0:                
                print(self.ident().lista)
            else:
                print('NADA DE NADA ')

call= False

if call:
    A1 = Myarray1( [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] , 10 , 2 , True)
    A2 = Myarray1( [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] , 10 , 2 , True)

    B2= Myarray1( [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 10 , 2 , False)
    C= Myarray1 ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] , 4 , 5 , True )
    D= Myarray1 ([1,6,11,16,2,7,12,17,3,8,13,18,4,9,14,19,5,10,15,20] , 4 , 5 , False)
    Dedo = Myarray1 ([10,11,15,20,21,25,30,31,35,40,41,45] , 4 , 3 , True)




    #bueno = Myarray1( [1,2,3,4,5,6,7,11,9] , 3 , 3 , True)
    bueno2 = Myarray1( [1,2,3,8,4,5,6,10,7,11,9,12,8,10,12,25] , 4 , 4 , True)

    Masti1=  Myarray1( [1,2,3,4] , 2 , 2 , True)
    Masti2=  Myarray1( [1,2,3,4] , 2 , 2 , True)



    bueno = Myarray1( [1,2,3,4,5,6,7,11,9] , 3 , 3 , True)

    bueno_false = Myarray1( [1,4,2,5,3,6] , 3 , 2 , True)
    bueno_true = Myarray1( [1,2,3,4,5,6] , 3 , 2 , False)

    #A.get_coords(7)
    #A.get_pos(1,1)
    #A.switch()
    #B.switch()
    #B.switch()
    #B.get_col(4)
    #B.get_elem(4,1)
    #A.del_col(1)
    #C.swap_cols(4,2)
    #C.scale_row(3,2)
    #D.scale_col(3,2)
    #Dedo.transpose()
    #bueno2.det()
    #C.flip_cols()
    #C.flip_rows()

    #A1.sub(A2)

    #print(type(A2))
    #Masti1.rprod(Masti2)

    #bueno.rprod(2)

    bueno_inv = Myarray1( [1,2,3,4,5,6] , 2 , 3 , True)

    #bueno_false.lprod(bueno_inv)
    #bueno_inv.lprod(bueno_false)


class Myarray2():
    
    def __init__(self,lista,r,c,by_row):
        
        self.lista= lista   
        self.r=r  
        self.c=c    
        self.by_row = by_row  # indica si la matriz fue cargada en orden columnas por columna False o fila por fila True

    def cambio_inicial2 ( self, okay ):
        """
        el fin de esta función es variar la forma de leer la matriz switcheandola

        en algunos casos me es mas util tenerla de una forma y otras de otra

        para ver de que forma quiero esa matriz existe el parametro de entrada okay

        OKAY siempre tiene que ser de  ///TIPO BOOL///


        """
        
        if self.by_row == okay:            
            nuevo= self.switch()
            cambiar = True
        else:   
            nuevo = self.co_py()  
            cambiar=False
        return nuevo,cambiar

    def get_pos2(self,j,k):
        if self.by_row:
            return (j-1)*self.c+(k-1)
        else:
            return (k -1)*self.r+(j -1)

    def get_coords2(self,m):
        if self.by_row:

            j = m//self.c+1
            k = m%self.c+1
            print ('fila: ', j,'columna: ', k)
            return j,k
        else: 
            k = m//self.r+1
            j = m%self.r+1
            print ('fila: ', j,'columna: ', k)

    def switch2(self) :
        if self.by_row:
            x = list(zip (*self.lista))            
            new= []
            for parte in x:
                new.append(list(parte))            
            return Myarray2(new,self.r,self.c,False)
        else:
            x = list(zip (*self.lista))            
            new= []
            for parte in x:
                new.append(list(parte))            
            return Myarray2(new,self.r,self.c,True)
    
    def get_row2(self, j):
        if self.by_row:            
            return self.lista[j-1]
        else:
            x= self.switch()
            return x.lista[j-1]

    def get_col2(self, k):
        if self.by_row:
            x= self.switch()
            return x.lista[k-1]
        else:
            return self.lista[k-1]

    def get_elem2(self, j,k):
        
        if self.by_row:
            return [j-1][k-1]
        else:
            return [k-1][j-1]

    def del_row2( self, j):
        if self.by_row:            
            new=self.lista
            new.pop(j-1)
            return Myarray2(new,self.r -1 , self.c , True)

        else: 
            new = self.switch().lista
            new.pop(j-1)
            X = Myarray2(new,self.r -1 , self.c , True)
            return X.switch()

    def del_col2(self,k) :
        if self.by_row:            
            new = self.switch2().lista
            new.pop(k-1)
            X = Myarray2(new,self.r  , self.c-1, False)
            return X.switch2()

        else: 
            new = self.lista
            new.pop(k-1)
            return Myarray2(new,self.r  , self.c -1 , True)

    def co_py2(self):
        r1=self.r
        c1=self.c
        by_row1=self.by_row
        return Myarray2(  self.lista.copy() , r1 , c1  , by_row1 )

    def swap_rows2(self,j,k):
       
        if j != k:  

            nueva, coco= self.cambio_inicial2(False)          
            
            mi = min ( j , k  )
            ma = max (j , k )
            new = nueva . lista . copy ()
            X = new.pop(ma - 1 )
            new.insert ( ma - 1,   new [ mi - 1 ]    )
            Y= new.pop ( mi -1 )
            new.insert ( mi - 1, X)
            nueva.lista = new
            if cambiar:
                return nueva.switch()
            else:                    
                return nueva

    def swap_cols2(self,l,m) :
        
        if l != m:
            nueva, cambiar= self.cambio_inicial(True)
            mi = min(l,m)
            ma = max(l,m)
            new = nueva.lista.copy()
            X = new.pop(ma-1)
            new.insert ( ma-1,   new[mi-1]    )
            Y= new.pop(mi-1)
            new.insert(mi-1, X)
            nueva.lista = new
            if cambiar:
                return nueva.switch()
            else:                    
                return nueva
    
    def scale_row2(self,j,x):
        
        if self.by_row == False:            
            nueva= self.switch()
            cambiar = True
        else:   
            nueva = self.co_py2()  
            cambiar=False

        new = nueva.lista.copy()
        for indice in range (0, len(new[j])):
            new[j][indice]=new[j][indice]* x   

        nueva.lista = new
        
        if cambiar: 
            return nueva.switch()
        else:   
            return nueva
     
    def scale_col2(self,k,y):
        if self.by_row:            
            nueva= self.switch()
            cambiar = True
        else:   
            nueva = self.co_py2()  
            cambiar=False

        new = nueva.lista.copy()
        for indice in range (0, len(new[k])):
            new[k][indice]=new[k][indice]* y   

        nueva.lista = new
        
        if cambiar: 
            return nueva.switch()
        else:   
            return nueva

    def transpose2(self) :
        nueva = self.co_py2()
        z = nueva.r
        nueva.r = nueva.c
        nueva.c = z
        if nueva.by_row == False:            
            nueva.by_row= True
        else:   
            nueva.by_row = False
        return nueva
    
    def flip_cols2(self):        
        if self.by_row:            
            nueva= self.switch()
            cambiar = True
        else:   
            nueva = self.co_py2()  
            cambiar=False
       
        new=nueva.lista.copy()
        new= list(reversed(new))
        nueva.lista= new

        if cambiar:           
            print(self.switch().lista)
            return self
        else:                    
            print(self.lista)
            return self
    
    def flip_rows2(self) :
        if self.by_row == False:            
            nueva= self.switch()
            cambiar = True
        else:   
            nueva = self.co_py2()  
            cambiar=False
       
        new=nueva.lista.copy()
        new= list(reversed(new))
        nueva.lista= new

        if cambiar:           
            print(self.switch().lista)
            return self
        else:                    
            print(self.lista)
            return self
   
    def det2(self):
        #siempre como TRUE        
        if self.r  != self.c :
            pass
        else:
            if self.by_row == False:            
                nueva= self.switch2()
                cambiar = True
            else:   
                nueva = self.co_py2()  
                cambiar=False
             
            inicial = nueva.lista.copy()   
            if  len(inicial) == 2 :                  
                return inicial [0][0]*inicial[1][1]   -  inicial [1][0] * inicial[0][1]
                  
            else: 
                final= []                
                for j in range(0, len(inicial)):                    
                    mat_0 = nueva.co_py2()                    
                    mat_1 = mat_0.del_row2(1)
                    mat_2 = mat_1.del_col2(j+1)
                    final.append( ((-1)**(j))*(inicial[0][j])*mat_2.det2())   
            valor = 0
            for numero in final:
                valor= valor + numero
            print (valor)
            return valor

    def add2(self,B):
        
        if type(B) == Myarray2 and self.c == B.c and self.r == B.r:            
            
            total=[]
            for X, Y in zip (self.lista  , B.lista ):
                sumado = []
                for a,b in zip (X,Y):    
                    sumado.append(a+b)
                total.append(sumado) 

            print(total)
            return Myarray2(total, self.r, self.c , self.by_row)

        elif type(B) == float or type(B) == int :
            
            total=[]
            for lista in self.lista:
                resultado = map(lambda numero: numero + B, lista)
                total.append(list(resultado))
    
            return Myarray2(total, self.r, self.c , self.by_row)
        else: 
            print(' valores fuera de rangos permitidos')
   
    def sub2(self,B):
        if type(B) == Myarray2 and self.c == B.c and self.r == B.r:            
            
            total=[]
            for X, Y in zip (self.lista  , B.lista ):
                sumado = []
                for a,b in zip (X,Y):    
                    sumado.append(a-b)
                total.append(sumado) 

            print(total)
            return Myarray2(total, self.r, self.c , self.by_row)

        elif type(B) == float or type(B) == int :
            
            total=[]
            for lista in self.lista:
                resultado = map(lambda numero: numero - B, lista)
                total.append(list(resultado))
    
            return Myarray2(total, self.r, self.c , self.by_row)
        else: 
            print(' valores fuera de rangos permitidos')

    def rprod2(self,B):
        """
        #siempre creo un resultado que se recorra como True

        """
        if type(B) == Myarray2 and self.c == B.r:            
            
            if B.by_row:            
                derecha= B.switch2()
            else:   
                derecha = B.co_py2()  
            
            if self.by_row == False:            
                izquierda=  self.switch2()
            else:   
                izquierda=  self.co_py2()

            total= []
            for lineaA in izquierda.lista:
                linea_x = []
                for columnaB in derecha.lista:
                    valor=0
                    for X,Y in zip(lineaA, columnaB):
                        valor+=(X*Y)

                    linea_x.append( valor   )
                total. append(linea_x)       
            print (total)

            return Myarray2(total, izquierda.r,derecha.c, True)

       
        elif type(B) == float or type(B) == int :
            
            total=[]
            for lista in self.lista:
                resultado = map(lambda numero: numero * B, lista)
                total.append(list(resultado))
    
            return Myarray2(total, self.r, self.c , self.by_row)
        else: 
            print(' valores fuera de rangos permitidos')

    def lprod2(self,B):
        """
        #siempre creo un resultado que se recorra como True

        """
        if type(B) == Myarray2 and  B.c == self.r:            
            
            if self.by_row:            
                derecha= self.switch2()
            else:   
                derecha = self.co_py2()  
            
            if B.by_row == False:            
                izquierda = B.switch2()
            else:   
                izquierda= B.co_py2()
            
            total= []
            for lineaA in izquierda.lista:
                linea_x = []
                for columnaB in derecha.lista:
                    valor=0
                    for X,Y in zip(lineaA, columnaB):
                        valor+=(X*Y)

                    linea_x.append( valor )
                total. append(linea_x)  

            print (total)
            return Myarray2(total, izquierda.r,derecha.c, True)
       
        elif type(B) == float or type(B) == int :            
            total=[]
            for lista in self.lista:
                resultado = map(lambda numero: numero * B, lista)
                total.append(list(resultado))    
            return Myarray2(total, self.r, self.c , self.by_row)
        else: 
            print(' valores fuera de rangos permitidos')
     
    
    def ident2(self):
        
        if self.c ==  self.r:    
            total= []
            for X in range(0,len(self.lista)):
                subtotal = []
                for Y in range(0,len(self.lista)):
                    if X == Y:
                        subtotal.append(1)                    
                    else:
                        subtotal.append(0)
                total.append(subtotal)

            print(total)
            return Myarray1(total, self.r, self.c, True)
        else:
            print('fuera de parametros')   
    
    def pow(self,n):
        
        if n%2!=0:
            print(self.lista)
            return self
        else:
            if n%2==0:                
                print(self.ident().lista)
            else:
                print('NADA DE NADA ')

if call:  
    Masti1=  Myarray2( [[1,2],[3,4]], 2 , 2 , True)
    bueno23 = Myarray2( [[1,2,3,8],[4,5,6,10],[7,11,9,12],[8,10,12,25]] , 4 , 4 , True)

    bueno44 = Myarray2( [[1,2,3],[4,5,6],[7,11,9]] , 3 , 3 , True)

    bueno_false44 = Myarray2( [[1,4],[2,5],[3,6]] , 3 , 2 , True)

    bueno_false55 = Myarray2( [[1,4],[2,5],[3,6]] , 2 , 3 , False)


    #Masti1.switch()

    #bueno23.det2()

    #bueno44.rprod2(bueno_false44)

    #bueno_false44.lprod2(bueno44)

    #bueno23.ident2()

Masti555 =  Myarray1( [1,2,3,4] , 2 , 2 , True)
bueno888 = Myarray1( [1,2,3,8,4,5,6,10,7,11,9,12,8,10,12,25] , 4 , 4 , True)
bueno999= Myarray1( [1,4,7,8,2,5,11,10,3,6,9,12,8,10,12,25] , 4 , 4 , False)



print(bueno999.swap_rows(2,7).lista)