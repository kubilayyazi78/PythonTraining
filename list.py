urunler = ["Laptop","Mouse","Keyboard"]
print(urunler)
print(type(urunler))
urunler.append("Telefon")
print(urunler)

ogrenciler1=["Kubilay","Alper","Hüseyin"]
ogrenciler2=["Hasan","Selim","Demir"]


ogrenciler1=ogrenciler2

ogrenciler2[0]="Belhanda"

print(ogrenciler1[0])

sayi1=10
sayi2=20

sayi1=sayi2

sayi2=30

print(sayi1)

isim="Kubi"

isim2="miray"

isim2=isim

isim="aa"

print(isim2)