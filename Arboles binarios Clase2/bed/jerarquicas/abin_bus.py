from bed.jerarquicas.abin import ArbolBin
from bed.jerarquicas.nodos import NodoArbol_Bin
from bed.jerarquicas.excepciones import (DuplicatedKeyError, 
                                         HomogeneityError)

class ArbolBinario_Bus(ArbolBin):
    def adicionar(self, nueva_clave): #Sobre-escritura metodo adicionar
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
        
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif nueva_clave > sub_arbol.clave:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq,nueva_clave)
        elif nueva_clave < sub_arbol.clave:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        else: #nueva_clave == sub_arbol.clave
            raise DuplicatedKeyError (nueva_clave)
        return sub_arbol

    def encontrar(self, clave_encontrar):
        return self.__encontrar(self.raiz,clave_encontrar)
    
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol:
            if sub_arbol.clave == clave_encontrar:
                return sub_arbol.clave
            elif clave_encontrar < sub_arbol.clave: #buscar izq
                return self.__encontrar(sub_arbol.izq, clave_encontrar)
            else: #clave_encontrar > sub_arbol.clave #buscar der
                return self.__encontrar(sub_arbol.der, clave_encontrar)
        return None
    
    def encontrar_minimo(self):
        """metodo que busca el valor minimo del arbol

        Returns:
            obj: dato/None
        """
        
    
    def encontrar_maximo(self):
        """metodo que busca el valor maximo del arbol

        Returns:
            obj: dato/None
        """
    
    def remover(self, clave_remover,mayor=True):
        """metodo que remueve un dato por mayor o menor de la clave seleccionada

        Parameters
        ----------
        clave_remover : objetc
            la clave o sub arbol para remover una hoja
        mayor : bool, optional
            Mayor = reemplazo por el hijo mayor de los menores
            Menor = reemplazo por el hijo menor de los menores, by default True

        Returns
        -------
        bool
            true si se elimina, false en caso contrario
        """
        