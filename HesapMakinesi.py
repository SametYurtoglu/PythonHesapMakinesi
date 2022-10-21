
deger = str(input("işlem seç 1,2,3,4"))


if deger == "1":
    toplanılacaksayi1 = int(input("Toplanılacak Sayı Girin 1: "))
    toplanılacaksayi2 = int(input("Toplanılacak Sayı Girin 2: "))
    print("Sonuç:", toplanılacaksayi1 + toplanılacaksayi2)
if deger == "2":
    cıkarılacaksayi1 = int(input("Çıkarılacak Sayı Girin 1: "))
    cıkarılacaksayi2 = int(input("Çıkarılacak Sayı Girin 2: "))
    print("Sonuç:", cıkarılacaksayi1 - cıkarılacaksayi2)
elif deger == "3":
    capılacaksayi1 = int(input("Çarpılacak Sayı Girin 1:"))
    capılacaksayi2 = int(input("Çarpılacak Sayı Girin 2:"))
    print("Sonuç:", capılacaksayi1 * capılacaksayi2)
elif deger == "4":
    boluneceksayi1 = int(input("Bölünecek Sayı Girin 1:"))
    boluneceksayi2 = int(input("Bölünecek Sayı Girin 2:"))
    print("Sonuç:", boluneceksayi1 / boluneceksayi2)
else:
    print("Geçersiz")