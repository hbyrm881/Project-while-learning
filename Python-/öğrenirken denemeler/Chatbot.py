def hal_hatir (cevap):
    if "merhaba" in cevap.lower():
        return "Merhaba nasıl yardımcı olabilirim? "
    elif "nasılsın" in cevap.lower():
        return "İyiyim sen nasılsın? "
    elif "iyi" in cevap.lower():
        return "Bunu duyduğuma sevindim"
    elif "hesapla" in cevap.lower():
        return "Hesap makinasına geçiliyor"
    else:
        return "Üzgünüm anlayamadım"
    
def hesap_makinesi (a,b,c):
    if c == "+":
        print("Toplamı : ", a+b)
    elif c == "-":
        print("Farkı : ", a-b)
    elif c == "*":
        print("Çarpımı : ", a*b)
    elif c == "/":
        print("Bölümü", a/b)
    else:
        print("Hata oldu")
        

while True:
    girdi = input("Ben : ")
    if girdi.lower() == "çık":
        print("programdan çıkılıyor")
        break
    print ("Bot : ", hal_hatir(girdi))
    if girdi.lower() == "hesapla":
        a = int(input("sayı 1 girn : "))
        b = int(input("sayı 2 girin : "))
        c = input("işlem seçin + - * / : ")
        print ("Bot : ",hesap_makinesi(a,b,c) )
    