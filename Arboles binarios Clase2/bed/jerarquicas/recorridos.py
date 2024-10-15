
def __pre_orden(sub_arbol):
    if sub_arbol:
        print(sub_arbol.clave)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)

def pre_orden(arbol_bin):
    __pre_orden(arbol_bin.raiz)

def str_pre_orden(arbol_bin,sep='|'):
    pass