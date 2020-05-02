istenenKredi =1000
hesap=9000
minimumOlmasiGerekenHesap =10000

if hesap>=minimumOlmasiGerekenHesap:
    print("kredi verilebilir")
    print("ödemeler hesaplandı")
elif  hesap>=9000 and hesap<=9500:
    print("müdüre sorulacak")
elif  hesap>=9501 and hesap<=9999:
    print("genel müdüre sorulacak")
else:
    print("kredi alınamadı.")
print("islem sonu")

