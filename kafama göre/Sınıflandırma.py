class araba():
    def __init__(self,model,marka,renk): #metot
        self.model=model
        self.marka=marka
        self.renk=renk
    def aracBilgisi(self):
        print("markası: ",self.marka)
        print("modeli: ", self.model)
        print("rengi: ", self.renk)


taksi = araba(2020,"fiat","yeşil")
taksi.aracBilgisi()
