"""
Creador: Juan Rodolfo Enrique Alarcon Alpa  

"""

class Myarray1():
    
    def __init__(self,lista,r,c,by_row):
        
        self.lista= lista   
        self.r=r  # r = a la cantidad de filas
        self.c=c   # c = a la cantidad de columnas 
        self.by_row = by_row  # indica si la matriz fue cargada en orden columnas por columna False o fila por fila True
      
    def get_pos(self,j,k):
        if self.by_row:
            return (j-1)*self.c+(k-1)
        else:
            return (k -1)*self.r+(j -1)

    def get_coords(self,m):
        if self.by_row:

            j = m//self.c+1
            k = m%self.c+1
            print ('fila: ', j,'columna: ', k)
            x= (j,k)
            return x
        else: 
            k = m//self.r+1
            j = m%self.r+1
            print ('fila: ', j,'columna: ', k)
            x= (j,k)
            return x

    def switch(self) :
        if self.by_row:
            contador=0
            columna=1
            ram=[]
            for i in range (0,self.c):
                fila=1
                for f in range(i,len(self.lista),self.c):
                    ram.append(self.lista[self.get_pos(fila,columna)])
                    contador+=1 
                    fila+=1
                columna+=1
            self.lista= ram        
            #print(self.lista)
            self.by_row = False
            return self
        else:
            contador=0
            fila=1
            ram=[]
            for i in range (0,self.r):
                columna=1
                for f in range(i,len(self.lista),self.r):
                    ram.append(self.lista[self.get_pos(fila,columna)])
                    contador+=1 
                    columna+=1
                fila+=1  
            self.lista= ram        
            #print(self.lista)
            self.by_row = True
            return self
    
    def get_row(self, j):
        if self.by_row:
            
            ram=[]
            for i in range (j-1,len(self.lista),self.c):
                ram.append(self.lista[i])
                
            print(ram)
            return ram
        else:
            ram=[]
            for i in range ((self.r*(j-1)),(self.r*(j-1))+self.r):
                ram.append(self.lista[i])
            print(ram)
            return ram
    
    def get_col(self, k):
        if self.by_row:
            
            ram=[]
            for i in range ((self.c*(k-1)),(self.c*(k-1))+self.c):
            
                ram.append(self.lista[i])
                
            print(ram)
            return ram
        else:
            ram=[]
            for i in range (k-1,len(self.lista),self.r):
                ram.append(self.lista[i])
            print(ram)
            return ram

    def get_elem(self, j,k):
        
        if self.by_row:
            fila =1
            for i in range (k-1,len(self.lista),self.c):
                if fila == j:

                    print (f'Elemento: {self.lista[i]}')    
                    return self.lista[i]
                fila+=1
        else:
            columna =1
            for i in range (j-1,len(self.lista),self.r):
                if columna == k:

                    print (f'Elemento: {self.lista[i]}')    
                    return self.lista[i]
                columna+=1

    def del_row( self, j):
        if self.by_row == False:            
            new= self.switch().lista
            cambiar = True
        else:   
            new = self.lista.copy()  
            cambiar=False



        for X in range( (j-1)* self.c + self.c -1 ,(j-1)*self.c -1 , -1):
            new.pop(X)
        
        self.lista = new
        self.r = self.r-1
        
        if cambiar:           
            #print(self.switch().lista)
            return self
        else:                    
            #print(self.lista)
            return self
    
    def del_col(self,k) :
        if self.by_row:            
            new= self.switch().lista
            cambiar = True
        else:   
            new = self.lista.copy()  
            cambiar=False
       
        for X in range( (k-1)* self.r + self.r -1 ,(k-1)*self.r -1 , -1):
            new.pop(X)
        
        self.lista = new
        self.c = self.c - 1
        
        if cambiar:           
            #print(self.switch().lista)
            return self
        else:                    
            #print(self.lista)
            return self

    def swap_rows(self,j,k):
       
        if j != k:
            
            if self.by_row == False:
                nueva= self.switch()
                cambiar = True
            else:   
                nueva = self.lista.copy()  
                cambiar=False        
            
            mi = min(j,k)
            ma = max(j,k)

            new = nueva.copy()
            for X in range( (mi-1)*self.c , (mi-1)* self.c + self.c ):
                
                Z= new[X]
                new[X]= new [ X + (ma-mi)* self.c]
                new[X + (ma-mi)* self.c]= Z

            print(new)
            if cambiar:
                return new.switch()
            else:                    
                return new 

    def swap_cols(self,l,m) :
        
        if l != m:
            
            if self.by_row:
                nueva= self.switch()
                cambiar= True
            else:   
                nueva = self.lista.copy() 
                cambiar=False
            
            mi = min(l,m)
            ma = max(l,m)
            
            new = nueva.copy()
            for X in range( (mi-1)*self.r, (mi-1)* self.r + self.r ):
                
                Z= new[X]
                new[X]= new [ X + (ma-mi)* self.r]
                new[X + (ma-mi)* self.r]= Z

            print(new)
            if cambiar:
                return new.switch()
            else:                    
                return new
    
    def scale_row(self,j,x):
        
        if self.by_row == False:            
            nueva= self.switch().lista
            cambiar = True
        else:   
            nueva = self.lista.copy()  
            cambiar=False



        new = nueva.copy()
        for X in range( (j-1)*self.c , (j-1)* self.c + self.c ):
            new[X]= new[X] * x
        
        self.lista = new
        
        if cambiar:           
            print(self.switch().lista)
            return self
        else:                    
            print(self.lista)
            return self
     
    def scale_col(self,k,y):
        if self.by_row:            
            nueva= self.switch().lista
            cambiar = True
        else:   
            nueva = self.lista.copy()  
            cambiar=False

        new = nueva.copy()
        for X in range( (k-1)*self.r , (k-1)* self.r + self.r ):
            new[X]= new[X] * y
        
        self.lista = new
        
        if cambiar:           
            print(self.switch().lista)
            return self
        else:                    
            print(self.lista)
            return self

    def transpose(self) :
        z = self.r
        self.r = self.c
        self.c = z
        if self.by_row == False:            
            self.by_row= True
        else:   
            self.by_row = False
        return self
    
    def flip_cols(self):        
        if self.by_row:            
            nueva= self.switch().lista
            cambiar = True
        else:   
            nueva = self.lista.copy()  
            cambiar=False

        nueva.copy()
        new=[]
        for X in range( len(nueva)- self.r , -1, - self.r ):            
            for Y in range( X , X+ self.r):
                
                new.append(nueva[Y])
        self.lista = new        
        if cambiar:           
            print(self.switch().lista)
            return self
        else:                    
            print(self.lista)
            return self
    
    def flip_rows(self) :
        if self.by_row == False:            
            nueva= self.switch().lista
            cambiar = True
        else:   
            nueva = self.lista.copy()  
            cambiar=False
        nueva.copy()
        new=[]
        for X in range( len(nueva)- self.c , -1, - self.c ):            
            for Y in range( X , X+ self.c):
                print(new)
                new.append(nueva[Y])        
        self.lista = new        
        if cambiar:           
            print(self.switch().lista)
            return self
        else:                    
            print(self.lista)
            return self
    
    def co_py(self):
        r1=self.r
        c1=self.c
        by_row1=self.by_row
        return Myarray1(self.lista.copy(),r1,c1,by_row1)

    def det(self):
        #siempre como TRUE        
        if self.r  != self.c :
            pass
        else:
            if self.by_row == False:            
                self.switch()
            inicial = self.co_py()           
            if  self.r == 2 and self.c == 2:
                #print("  ENTRO ENTRO ENTRO ENTRO ENTRO ENTRO")
                fax= self.lista.copy()
                total= fax [0]*fax[3]   -   fax [1]*fax[2]
                print (total)
                return total            
            else: 
                final= []
                for j in range(  0, inicial.r  ):                    
                    listado = self.co_py()
                    borrado = listado.del_col(j+1)
                    llamada = borrado.del_row(1)
                    final.append( ((-1)**(j))*(inicial.lista[j])*llamada.det())            
            valor = 0
            for numero in final:
                valor= valor + numero
            print (valor)
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
            if  self.by_row == False:
                nueva  =  self.switch()
                cambiar  =  True
            else:   
                nueva =  self . co_py2()  
                cambiar  = False 
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
            if self.by_row:
                nueva= self.switch()
                cambiar = True
            else:   
                nueva = self.co_py2()  
                cambiar=False 
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
  
Masti1=  Myarray2( [[1,2],[3,4]], 2 , 2 , True)
bueno23 = Myarray2( [[1,2,3,8],[4,5,6,10],[7,11,9,12],[8,10,12,25]] , 4 , 4 , True)

bueno44 = Myarray2( [[1,2,3],[4,5,6],[7,11,9]] , 3 , 3 , True)

bueno_false44 = Myarray2( [[1,4],[2,5],[3,6]] , 3 , 2 , True)

bueno_false55 = Myarray2( [[1,4],[2,5],[3,6]] , 2 , 3 , False)


#Masti1.switch()

#bueno23.det2()

#bueno44.rprod2(bueno_false44)

#bueno_false44.lprod2(bueno44)

bueno23.ident2()