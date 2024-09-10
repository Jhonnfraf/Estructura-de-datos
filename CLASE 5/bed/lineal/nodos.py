class Nodo_listaSE:
    """Clase que modela un nodo para le tipo de estructura lista simplemente 
    Enlazada.
    """
    def __init__(self,dato):
        """Metodo constructor de un nodo para una lista simplemente enlazada

        Parameters
        ----------
        dato : object
            El dato que se pasa al nodo
        """
        self.dato=dato
        self.sig=None

    def __str__(self):
        """Metodo que retorna la cadena de un nodo

        Returns
        -------
        str
            La cadena al ser retornada por el nodo, que incluye el dato
        """
        return f"{self.dato}"
        

    