from bed.jerarquicas.nodos import NodoArbol_Bin
from random import random

class ArbolBin:
    def __init__(self):
        self.raiz = None
        
    def adicionar (self,nueva_clave):
        self.raiz = self.__adicionar(self.raiz,nueva_clave) #Subarbol#
    
    def __adicionar(self,sub_arbol,nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif random()<=0.5: #Por la izquierda
            nodo_izq = self.__adicionar(sub_arbol.izq,nueva_clave)
            sub_arbol.izq = nodo_izq
        else: #Por derecha
            nodo_der = self.__adicionar(sub_arbol.der,nueva_clave)
            sub_arbol.der = nodo_der
        return sub_arbol
    
    def encontrar (self,clave_encontrar):
        return self.__encontrar(self.raiz,clave_encontrar)
    
    def __encontrar (self, sub_arbol,clave_encontrar):
        if sub_arbol is not None:
            print(sub_arbol.clave, "<-->",clave_encontrar)
            print(("O" if sub_arbol.izq else "X")+" : "+("O"if sub_arbol.der else "X"))
            if sub_arbol.clave == clave_encontrar:
                return sub_arbol.clave
            else:
                clave_izq = self.__encontrar(sub_arbol.izq,clave_encontrar)
                if clave_izq == clave_encontrar:
                    return clave_izq
                clave_der = self.__encontrar(sub_arbol.der,clave_encontrar)
                if clave_der == clave_encontrar:
                    return clave_der
        return None
    

