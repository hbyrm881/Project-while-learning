import tkinter as tk
import requests 

pencere = tk.Tk()
pencere.title("Hava Durumu")
pencere.geometry("300x400")

entry = tk.Entry(pencere)
entry.pack(pady=40)

def havadurumu_al():
    sehir = entry.get()
    url = f"https://wttr.in/{sehir}?format=%t"
    entry.delete(0,tk.END)
    try:
        response = requests.get(url)
        sonuc.config(text=response.text)
    except Exception as e:
        sonuc.config(text="Bir sorun oldu.")

sonuc = tk.Label(pencere, text="")
sonuc.pack(pady=20)

buton = tk.Button(pencere,text="Sonuc",command=havadurumu_al)
buton.pack()


pencere.mainloop()