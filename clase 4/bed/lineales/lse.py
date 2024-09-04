#Para abrir las configuraciones usaremos Ctrl+","

print("NAME: ", __name__ ,"PAQUETE: ", __package__)
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE as nd
else:
    from bed.lineales.nodos import Nodo_listaSE as nd

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


    def __remover_dato(self,dato_elm):
        pass
        


if __name__=="__main__":
    lista=lista_SE()
    lista.adicionar(5)
    lista.adicionar(6)
    lista.adicionar(7)
    lista.adicionar(2)
    lista.adicionar("Yo no funciono")
    #lista.recorrer()

    #numero=lista.encontrar(9)
    #print(numero)
    
    lista.remover(-5,True)

    lista.recorrer()