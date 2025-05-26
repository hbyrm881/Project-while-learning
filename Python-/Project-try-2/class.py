class Canlilar:
    ozellik = "Solunum"

    def __init__(self, bitkiler, hayvanlar, mantarlar, protistalar):
        self.bitkiler = bitkiler
        self.hayvanlar = hayvanlar
        self.mantarlar = mantarlar
        self.protistalar = protistalar

class Canli:
    def __init__(self, isim):
        self.isim = isim

class Bitki(Canli):
    def fotosentez(self):
        return f"{self.isim} fotosentez yapar."

class Hayvan(Canli):
    def hareket(self):
        return f"{self.isim} hareket eder."
kedi = Hayvan("Kedi")
print(kedi.hareket())

cicek = Bitki("Çiçek")
print(cicek.fotosentez())

canli1 = Canlilar(
    bitkiler=["Ağaç", "Çiçek"],
    hayvanlar=["Kedi", "Köpek"],
    mantarlar=["Şapkalı Mantar"],
    protistalar=["Amip"]
)

print("Canlıların ortak özelliği:", Canlilar.ozellik)
print("Bitkiler:", canli1.bitkiler)
print("Hayvanlar:", canli1.hayvanlar)
print("Mantarlar:", canli1.mantarlar)
print("Protistalar:", canli1.protistalar)
