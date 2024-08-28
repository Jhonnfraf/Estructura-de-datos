class Nodo_listaSE:
    def __init__(self,dato):
        self.dato=dato
        self.sig=None

    def __str__(self):
        return f"{self.dato}"
        
if __name__=="__main__":
    nodo1=Nodo_listaSE(8)
    nodo2=Nodo_listaSE(5)
    nodo3=Nodo_listaSE(10)
    nodo4=Nodo_listaSE(2)

    nodo1.sig=nodo2
    nodo2.sig=nodo3
    nodo3.sig=nodo4
    nodo4.sig=None

    aux=nodo1
    while aux is not None:
        print(aux)
        aux=aux.sig




    #print(nodo1.sig.sig.sig)
    #print(nodo4)
    