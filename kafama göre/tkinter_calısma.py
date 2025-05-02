import tkinter as tk

pencere = tk.Tk()
pencere.title("Görev listesi")
pencere.geometry("300x500")

entry = tk.Entry(pencere)
entry.pack(pady=20)

listbox = tk.Listbox(pencere, selectmode="multiple", width=40)
listbox.pack(pady=5)

liste = []

def ekle ():
    veri_al = entry.get()
    if veri_al:
        liste.append(veri_al)
        listbox.insert(tk.END,veri_al)
        entry.delete(0,tk.END)
        print("Eklendi : ",veri_al)
    else:
        print("Boş girdiniz")

def sil ():
    secili_index = listbox.curselection()
    if secili_index :
        for index in reversed (secili_index):
            listbox.delete(index)
            liste.pop(index)
            print("silindi",secili_index)
    else:
        print("Seçim yapın")

def tumu_sil ():
    if liste:
        liste.clear()
        listbox.delete(0,tk.END)
        print("Herşey silindi")
    else:
        print("Liste zaten boş")
        
buton_ekle = tk.Button(pencere, text="Ekle",width=15, height=2,command=ekle)  
buton_ekle.pack()  

buton_sil = tk.Button(pencere, text="Sil",width=15, height=2, command=sil)
buton_sil.pack()

buton_allsil = tk.Button(pencere, text="Hepsini sil",width=15, height=2, command=tumu_sil)
buton_allsil.pack()

pencere.mainloop()