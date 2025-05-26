import tkinter as tk
import os

pencere = tk.Tk()
pencere.title("Login Ekranı")
pencere.geometry("400x300")

DOSYA_ADI = "kullanıcılar.txt"

k_kullanici_adi = ["Hasan"]
k_sifre = ["123"]

if os.path.exists(DOSYA_ADI):
    with open(DOSYA_ADI, "r") as dosya:
        for satir in dosya:
            satir = satir.strip()
            if ":" in satir:
                ad , sifre = satir.split(":", 1)
                k_kullanici_adi.append(ad)
                k_sifre.append(sifre)

kullanici_ad = tk.Label(pencere, text="Kullanıcı adı :")
kullanici_ad.pack(pady=5)

entry_ka = tk.Entry(pencere)
entry_ka.pack()

sifre  = tk.Label(pencere, text="Şifre girin :")
sifre.pack()

entry_s = tk.Entry(pencere)
entry_s.pack()

def giris ():
    kullanici = entry_ka.get()
    sifre_ = entry_s.get()
    
    if kullanici in k_kullanici_adi:
        if sifre_ in k_sifre:
            sonuc_label.config(text="Giriş başarılı ✅", fg="green")
            entry_ka.delete(0,tk.END)
            entry_s.delete(0,tk.END)
        else:
            sonuc_label.config(text="Şifre hatalı ❌", fg="red")
    else:
        sonuc_label.config(text="Kullanıcı adı yanlış ❌", fg="red")
    

def kayit ():
    kullanici = entry_ka.get()
    sifre_ = entry_s.get()
    
    if not kullanici or not sifre_:
        sonuc_label.config(text="Kullanıcı adı ve şifre boş olamaz ❌", fg="red")
        return
    
    if kullanici in k_kullanici_adi:
        sonuc_label.config(text="Bu kullanıcı zaten kayıtlı ❌", fg="red")
        return

    k_kullanici_adi.append(kullanici)
    k_sifre.append(sifre_)

    with open(DOSYA_ADI, "a") as dosya:
        dosya.write(f"{kullanici}:{sifre_}\n")

    entry_ka.delete(0,tk.END)
    entry_s.delete(0,tk.END)
    sonuc_label.config(text="Kayıt Başarılı ✅", fg="green")

buton_cerceve = tk.Frame(pencere)
buton_cerceve.pack(pady=10)

giris_buton = tk.Button(buton_cerceve, text="Giriş", command=giris, width=10, height=1)
giris_buton.pack(side="left",padx=5)

kayit_buton = tk.Button(buton_cerceve, text="Kayıt Ol", command=kayit, width=10, height=1)
kayit_buton.pack(side="left",padx=5)

sonuc_label = tk.Label(pencere, text="", fg="blue", font=("Arial", 12))
sonuc_label.pack(pady=10)

pencere.mainloop()