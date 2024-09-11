print("NAME: ", __name__ ,"PAQUETE: ", __package__)
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE as nd
else:
    from bed.lineal.nodos import Nodo_listaSE as nd
#Para abrir las configuraciones usaremos Ctrl+","
class lista_SE:
    """Clase que implementa el funcionamiento de una lista simplemente enlazada
    """
    def __init__(self):
        """Metodo para la creacion de un elemento tipo lista S.enlazada
        """
        self.__cab = None
    
    def es_vacia(self):
        """Verifica que una lista esta vacia o no

        Returns
        -------
        bool
            retorna True si la lista esta vacia y False en caso contrario
        """
        if self.__cab is None: #Evitar usar "==" para comparaciones de referencias                 
            return True                                                                            
        return False                                                                               
        #Alternativa
        #return self.__cab is None  

    def adicionar(self,nuevo_dato):
        """adiciona un nodo a una lista

        Parameters
        ----------
        nuevo_dato : Nodo_listaSE (objeto)
            el nuevo dato que se adicionará a la lista
        """
        nuevo_nodo = nd(nuevo_dato)                                                                
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            #caso cuando la lista no esta vacia
            actual = self.__cab
            while actual.sig is not None: #while actual.sig:
                actual=actual.sig                                                                  
            actual.sig=nuevo_nodo #agrega un nuevo nodo a la lista
    
    def recorrer(self):
        """Metodo que recorre la lista imprimiendo los datos siempre y cuando no sea vacia
        """
        actual=self.__cab
        while actual: #while actual is not None:
            print(actual)
            actual=actual.sig
    
    def encontrar(self,dato_encontrar):
        """se ingresa un dato y verifica si este se encuentra en la lista

        Parameters
        ----------
        dato_encontrar : object
            dato a encontrar en la lista

        Returns
        -------
        object
            retorna el dato si se encuentra en la lista, y en caso contrario retorna None
        """
        #PRIMERA ALTERNATIVA
        actual=self.__cab
        while actual: #while actual is not None:
            if actual.dato == dato_encontrar:
                return actual.dato #retorna el dato actual
            actual=actual.sig
        return None #No es necesario

        #SEGUNDA ALTERNATIVA
        #while actual and actual.dato != dato_encontrar:
        #    actual=actual.sig
        #return actual.dato if actual else None
    
    def remover(self,item,por_pos=True):
        if por_pos:
            return self.__remover_pos(item)
        #CONSULTAR
        return self.__remover_dato(item)
    
    def __remover_pos (self,pos_elm):
        """remueve un dato que se le da el indice

        Parameters
        ----------
        pos_elm : int
            posicion del elemento que se desea eliminar

        Returns
        -------
        bolean
            retorna True
        """
        actual=self.__cab 
        indice=0
        anterior=None
        if pos_elm >= 0:
            while actual and indice < pos_elm:
                anterior=actual
                actual=actual.sig
                indice+=1
            if indice==0 and actual:
                self.__cab=actual.sig
            elif actual: 
                anterior.sig=actual.sig
        return True if actual and pos_elm == indice else False

# CONSULTAS:

    def __remover_dato(self,dato_elm):
        """Método que permite remover un nodo de la lista ya sea por una
        posición o por el dato correspondiente. Si es por dato, deberá
        remover cada uno de los nodos que contenga dicho dato.

        Parameters
        ----------
        item : object|int
            Puede corresponder al valor del dato a ser removido de la lista
            o a la posición en la lista a remover el dato.
            En el caso de remover por dato, se buscará todas las coincidencias
            del dato a eliminar en la lista y serán quitadas.
        por_pos : bool, optional
            Si es True, el método intentará remover un dato por su posición,
            de lo contrario se intentará hacerlo por su valor, por defecto True.

        Returns
        -------
        bool
            True cuando el dato es removido de la lista. False en caso
            contrario.
        """
        actual=self.__cab #ubicamos la cabecera
        anterior=None #inicializamos el valor del nodo anterior
        removido=True
        while actual:  #while actual is not none 
            if actual.dato==dato_elm: #si el dato actual es igual al dato a remover
                if anterior: #if anterior is not none
                    anterior.sig=actual.sig
                else: #if anterior is none (es el primer nodo)
                    self.__cab=actual.sig
                removido=True
            else:
                anterior=actual #nodo anterior igual al dato actual
            actual=actual.sig
        return True if removido else False

        


    def posicionar(self,nuevo_dato, pos):
        """Método que inserta un nuevo nodo en cualquier posición de la
        lista. Si la lista está vacía la única posición válida será
        cero. Si la lista ya contiene datos, serán válidas posiciones
        intermedias o la posición inmediatemente superior a la del último dato.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.
        pos : int, optional
            Posición a insertar en la lista, por defecto 0.

        Returns
        -------
        bool
            True cuando el dato es insertado en la lista. False en caso
            contrario.
        """
        actual=self.__cab
        nodo=nd(nuevo_dato)
        anterior=None
        indice=0
        if self.es_vacia():
            self.adicionar(nodo)
            return True
        if pos==0:
            self.__cab=nuevo_dato
        else:
            while actual and indice < pos-1:
                actual=actual.sig
                indice+=1
            if actual:
                nodo.sig=actual.sig
                actual.sig=nodo
            else:
                self.adicionar(nodo)
        return True if self.encontrar(nodo) else False



    def ubicar(self, pos):
        """Método que realiza la búsqueda de un dato en la lista dependiendo
        de la posición ingresada.

        Parameters
        ----------
        pos : int
            Corresponde a la posición en la lista a ubicar el dato.

        Returns
        -------
        object|None
            object si el dato es ubicado en la lista, None en caso contrario.
        """
        actual=self.__cab
        indice=0
        while actual:
            if indice==pos:
                return actual.dato
            actual=actual.sig
            indice+=1
        return None

    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista, o una
        cadena vacía en el caso de que la lista sea vacía.

        Returns
        -------
        str
            Si la lista no es vacía retornará una cadena en el foramato:
                "(dato_0) :>: (dato_1) :>: (dato_2) :>: ... :>: (dato_n)"
                "(7) :>: (8) :>: (5) :>: (5) :>: (9)"
            de lo contrario retornará una cadena vacía: ""
        """
        actual=self.__cab
        lista=""
        while actual:
            lista+=str(actual.dato)+" :>: "
            actual=actual.sig
        if lista:
            lista=lista[:-5] #para eliminar los ultimos caracteres de una cadena
        return lista
    
    def __len__(self):
        """Método que calcula el tamaño de la lista.

        Returns
        -------
        int
            El número de nodos que tiene la lista.
        """        
        actual=self.__cab
        contador=0
        while actual:
            contador+=1
            actual=actual.sig
        return contador
    def __iter__(self):
        """Método que devuelve un iterador sobre los elementos de la lista.

        Yields
        ------
        object
            El siguiente elemento en la lista.
        """
        actual = self.__cab
        while actual:
            yield actual.dato
            actual = actual.sig



        