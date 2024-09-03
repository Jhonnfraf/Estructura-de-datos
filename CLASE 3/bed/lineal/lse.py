from nodos import Nodo_listaSE as nd #no usar "as" en parciales
#Para abrir las configuraciones usaremos Ctrl+","
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

if __name__=="__main__":
    lista=lista_SE()
    lista.adicionar(5)
    lista.adicionar(6)
    lista.adicionar(7)
    lista.adicionar(2)
    lista.adicionar("Yo no funciono")
    lista.recorrer()
        