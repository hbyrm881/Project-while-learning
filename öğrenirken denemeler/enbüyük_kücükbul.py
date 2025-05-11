

sayilar = []

flag = True
while flag:
    try:
        sayi_girin = int(input("Bir sayı girin: (çıkmak için -1 yazın) : "))
        if sayi_girin == -1:
            flag = False
        else:
            sayilar.append(float(sayi_girin))
    except SyntaxError:
        print("Hata Yanlızca sayı girin")
    except NameError:
        print("Hata yanlızca sayı girin")

try:
    en_buyuk = sayilar[0]
    en_kucuk = sayilar[0]
except IndexError:
    print("\nEn az bir sayı girmelisin")

finally:
    toplam = 0

for sayi in sayilar:
    if sayi > en_buyuk:
        en_buyuk = sayi
    if sayi < en_kucuk:
        en_kucuk = sayi
    toplam += sayi

ortalama = toplam / len(sayilar)

print("\nen büyük sayı = {}\n" \
      "en küçük sayı = {}\n" \
      "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))
