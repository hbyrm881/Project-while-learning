import tkinter as tk

def yazdir():
    secilen = liste.get(tk.ACTIVE)
    print("Seçilen:", secilen)

pencere = tk.Tk()
pencere.title("Mini Tkinter App")

giris = tk.Entry(pencere)
giris.pack()

buton = tk.Button(pencere, text="Yazıyı Al", command=lambda: print(giris.get()))
buton.pack()

liste = tk.Listbox(pencere)
for meyve in ["Elma", "Armut", "Kiraz", "Muz"]:
    liste.insert(tk.END, meyve)
liste.pack()

sec_buton = tk.Button(pencere, text="Listeden Seç", command=yazdir)
sec_buton.pack()

pencere.mainloop()
