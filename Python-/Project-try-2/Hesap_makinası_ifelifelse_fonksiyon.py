def toplama(a,b):
    print("Sonuç : ",a+b)
def cikarma(a,b):
    print("Sonuç : ",a-b)
def carpma(a,b):
    print("Sonuç : ",a*b)
def bolme(a,b):
    print("Sonuç : ",a/b)


sayi1 = int(input("İlk Sayıyı Giriniz..: "))
sayi2 = int(input("İkinci Sayıyı Giriniz..: "))

islem = input("İşlem Seçiniz : + , - , * , /  ")


if islem == "+" :
    toplama(sayi1,sayi2)
elif islem == "-" :
    cikarma(sayi1,sayi2)
elif islem == "*" :
    carpma(sayi1,sayi2)
elif islem == "/" :
    bolme(sayi1,sayi2)
else:
    print("Hatalı işlem..")

