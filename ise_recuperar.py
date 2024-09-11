class lista_SE:

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
        """adiciona un nodo a una lista Se

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

