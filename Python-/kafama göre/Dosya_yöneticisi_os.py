import os


flag = True
while flag:
    print("=== Mini Dosya Yöneticisi ===\n\n1- Bulunduğum Klasörü Göster\n2- Klasördeki Dosyaları Listele\n3- Yeni klasör Oluştur\n4- Dosya Sil\n5- Klasör Değiştir\n6- Çıkış")
    islem = input("Yapmak istediğiniz işlem numarsını giriniz: ")
    if islem == "1":
        print("şu anda bulunduğun klasör:")
        print(os.getcwd())
    
    elif islem == "2":
        print("Klasördeki Dosyalar: ")
        for item in os.listdir():
            print(item)

    elif islem == "3":
        yeni_klasor = input("Oluşturmak istedğiniz klasör adı: ")
        if not os.path.exists(yeni_klasor):
            os.mkdir(yeni_klasor)
            print(f"'{yeni_klasor}' adlı klasör oluştu. ")
        else:
            print("Bu isimde klasör zaten var.")
    
    elif islem == "4":
        silinecek = input("Silmek istediğiniz klasörün ismi: ")
        if os.path.exists(silinecek): 
            if os.path.isfile(silinecek):
                os.remove(silinecek)
                print(f"'{silinecek}' adlı dosya silindi.")
            elif os.path.isdir(silinecek):
                try:
                    os.rmdir(silinecek)
                    print(f"'{silinecek}' adlı klasör silindi.")
                except OSError:
                    print("Bu klasör boş değil. Sadece boş klasörler silinebilir.")
        else:
            print("Klasör bulunamadı.")

    elif islem == "5":
        yeni_klasor_yolu = input ("Geçmek istediğiniz klasör yolunu girin: ")
        if os.path.exists(yeni_klasor_yolu) and os.path.isdir(yeni_klasor_yolu):
            os.chdir(yeni_klasor_yolu)
            print("klasör değştirildi. yeni konum: ", os.getcwd())
        else:
            print("klasör Bulunamadı.")

    elif islem == "6":
        flag = False
        print("Çıkış yapılıyor.")

    else:
        print("Geçersiz işlem numarası girdiniz. ")