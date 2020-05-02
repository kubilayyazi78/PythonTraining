faktoriyel=int(input("Faktoriyeli hesapalanacak sayıyı giriniz : "))
toplam=0

if  faktoriyel<0:
    print("0 dan küçük olamaz")
elif  faktoriyel ==0:
    toplam=1
    print("faktoriyel = : "+ str(faktoriyel))
else:
    for fak in range(faktoriyel,0,-1):
        toplam=toplam+(faktoriyel*fak-1)
print(toplam)        
