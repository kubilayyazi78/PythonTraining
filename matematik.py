class Matematik():
    def __init__(self,sayi1,sayi2):
        self.s1=sayi1
        self.s2=sayi2
        print("Matematik  Basladi(ref olustu)")
    def topla(self):
        return self.s1+self.s2 
    def cikar(self):
        return self.s1-self.s2
    def bol(self):
        return self.s1/self.s2 
    def carp (self):
        return self.s1*self.s2          

matematik=Matematik(8,4)

sonuc=matematik.bol()

print("somuc : " + str(sonuc))
