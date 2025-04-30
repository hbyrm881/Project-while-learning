import tkinter as tk

pencere = tk.Tk()
pencere.title("Chat GPT dersi")
pencere.geometry("400x500")

etiket = tk.Label(pencere, text="Hoş geldin!", font=("Arial", 16))
etiket.pack(pady=20)

def tiklandi():
    etiket.config(text="Butona tıklandı!")

buton = tk.Button(pencere, text="Tıkla", command=tiklandi)
buton.pack()

pencere.mainloop()