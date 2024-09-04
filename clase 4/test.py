from bed.lineales.lse import lista_SE
if __name__=="__main__":
    lista=lista_SE()
    lista.adicionar(5)
    lista.adicionar(6)
    lista.adicionar(7)
    lista.adicionar(2)
    lista.adicionar("Yo no funciono")
    lista.recorrer()