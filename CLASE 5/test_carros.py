from bed.lineal.lse import lista_SE

class Carro:
    """Clase que implementa el funcionamiento de un carro,
    que posee una placa, marca y modelo. Tener en cuenta lo siguiente
    - la placa tiene que tener el formato: "LLL NNN", donde l es letra
    y n es número.
    - Los modelos validos son a partir del año 2000 unicamente. por defecto
    el año del modelo sera 2000.
    -Un carro sera igual que otro si tienen la misma placa y marca
    """
    def __init__(self,placa,marca,modelo=2000):
        if self.validar(placa):
            self.placa=placa
            self.marca=marca
            self.modelo=modelo
        else:
            raise ValueError("No se creó el carro")
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,año_modelo):
        if año_modelo >= 2000:
            self.__modelo=año_modelo
        else:
            raise ValueError("El año del modelo debe ser 2000 o posterior")



    def __eq__(self, otro_car):
        return (self.placa == otro_car.placa 
                and self.marca == otro_car.marca)

    def __str__(self):
        return f"{self.placa}/{self.marca}/{self.modelo}"
    
    def validar(self, placa):
        cont=0
        for caracter in placa:
            if caracter.isalpha() and caracter.isupper() and cont<=3:
                cont+=1
            if caracter.isnumeric():
                cont+=1
        if cont==6:
            print("PLACA VALIDA")
            return True
        else:
            print("Placa no valida")
        

class CarroPirata:
    def __init__(self,placa,marca,modelo=2000):
        self.placa=placa
        self.marca=marca
        self.modelo=modelo

    def __eq__(self, otro_car):
        return (self.placa == otro_car.placa 
                and self.marca == otro_car.marca)


    def __str__(self):
        return f"{self.placa}/{self.marca}/{self.modelo}"
    




if __name__=="__main__":
    list_carros=lista_SE()
    car1=Carro("QKJ 789","Renault",2010)
    list_carros.adicionar(car1)
    list_carros.adicionar(Carro("AWX 456","Mazda",2005))
    carb=Carro("RTY 159","Toyota",2018)
    list_carros.adicionar(carb)
    
    try:
        car3=Carro("QKJ 789","Renault",1980)
        print(car3)
        car3.modelo=1985
    except ValueError as e:
        print(e)


    print("----------PRUEBAS------------\n")
    list_carros.recorrer()

    print("-----------------------------\n")

    #car2=CarroPirata("QKJ 789","Renault")
    
    #placa=input("Placa a buscar: ")
    #marca=input("Marca a buscar: ")
    
    #car2=CarroPirata(placa,marca)
    #print("buscar carro :", list_carros.encontrar(car2))
    #print(list_carros.adicionar(car2))
    #print(car1==car2)

    print("\n-----------------------------")

    #car3=Carro("1QE 12","Toyota")
    #print(car3)