faktoriyel=int(input("Faktoriyeli hesapalanacak sayıyı giriniz : "))
toplam=1

if  faktoriyel<0:
    print("0 dan küçük olamaz")
elif  faktoriyel ==0:
    print("faktoriyel = : "+ str(toplam))
else:
    for fak in range(faktoriyel,0,-1):
        toplam=fak*toplam
    print(toplam)        
