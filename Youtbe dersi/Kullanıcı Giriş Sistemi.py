kk = ["Hasan","Yusuf"]
kp = ["123","456"]
print("Sisteme giriş yapmak: G kaydolmak: K  :")
secim = input()

if secim.lower() == "k":
    ka = input("Kullanıcı adınız? :")
    pa = input("Parolanız? :")
    print("kaydolma başarılı şimdi giriş yapınız")

    print("Giriş yapınız")
    ka2 = input("\nKullanıcı adınız?: ")
    pa2 = input("\nParolanız?: ")

    if ka == ka2:
        if pa == pa2:
            print("Giriş Başarılı")
        else:
            print("Kullanıcı adı veya parola hatalı")
    elif pa == pa2:
        print("Kullanıcı adı veya parola hatalı")
    else:
        print("Kullanıcı adı veya parola hatalı")

elif secim.lower() == "g":
    gk = input("Kullanıcı adınız? :")
    gp = input("Parolanız? :")

    if kk == gk:
        if kp == gp:
            print("Giriş Başarılı")
        else:
            print("Kullanıcı adı veya parola hatalı")
    elif kk != gk:
        print("Kullanıcı adı veya parola hatalı")
    else:
        print("Kullanıcı adı veya parola hatalı")

else:
    print("Yanlış tuşlama yaptınız büyük küçük harfe dikkat edin")
