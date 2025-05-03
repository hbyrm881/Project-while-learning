import tkinter as tk
import requests

def hava_durumu_getir():
    sehir = entry.get()
    url = f"https://wttr.in/{sehir}?format=%t"
    entry.delete(0,tk.END)
    try:
        response = requests.get(url)
        sonuc.config(text=response.text)
    except Exception as e:
        sonuc.config(text="Hata oluştu!")

pencere = tk.Tk()
pencere.title("Hava Durumu App")
pencere.geometry("300x500")

entry = tk.Entry(pencere)
entry.pack(pady=10)

buton = tk.Button(pencere, text="Hava Durumunu Getir", command=hava_durumu_getir)
buton.pack(pady=5)

sonuc = tk.Label(pencere, text="")
sonuc.pack(pady=10)

pencere.mainloop()
