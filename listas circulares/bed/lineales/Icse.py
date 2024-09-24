print("NAME: ", __name__ ,"PAQUETE: ", __package__)
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE as nd
else:
    from bed.lineales.nodos import Nodo_listaSE as nd

class Lista_CSE:
    """Clase que implementa una lista circular simplemente enlazada
    """
    def __init__(self):
        """Metodo para la creacion de un elemento lcse
        """
        self.__cab=None
    
    def es_vacia(self):
        pass
    
    #AGREGAR 
    def adicionar(self,nuevo_dato):
        pass
    
    def posicionar(self,nuevo_dato,pos_rel=0):
        pass
    
    #SUPRIMIR
    def remover(self,item,por_pos=True):
        pass

    #BUSCAR
    def encontrar(self,dato_buscar):
        pass

    def encontrar_cuantos(self, dato_buscar):
        pass

    def ruleta(self, pos_rel):
        pass
    
    #RECORRER
    def __str__(self) -> str:
        pass

    #TAMAÑO
    def __len__(self):
        pass
