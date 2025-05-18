import hashlib
import time

class Blok:
    def __init__(self, indeks, zaman, veri, onceki_hash):
        self.indeks = indeks
        self.zaman = zaman
        self.veri = veri
        self.onceki_hash = onceki_hash
        self.hash = self.hash_hesapla()

    def hash_hesapla(self):
        sha = hashlib.sha256()
        sha.update(f"{self.indeks}{self.zaman}{self.veri}{self.onceki_hash}".encode())
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.zincir = [self.ilk_blok()]

    def ilk_blok(self):
        return Blok(0, time.time(), "İlk blok", "0")

    def son_blok(self):
        return self.zincir[-1]

    def blok_ekle(self, veri):
        onceki_blok = self.son_blok()
        yeni_blok = Blok(
            indeks=onceki_blok.indeks + 1,
            zaman=time.time(),
            veri=veri,
            onceki_hash=onceki_blok.hash
        )
        self.zincir.append(yeni_blok)

    def zinciri_goster(self):
        for blok in self.zincir:
            print(f"\nBlok #{blok.indeks}")
            print(f"Tarih: {time.ctime(blok.zaman)}")
            print(f"Veri: {blok.veri}")
            print(f"Önceki Hash: {blok.onceki_hash}")
            print(f"Hash: {blok.hash}")

# Test
bc = Blockchain()
bc.blok_ekle("Hasan'ın ilk notu")
bc.blok_ekle("Bir şey daha yazıldı")
bc.blok_ekle("Son blok verisi")

bc.zinciri_goster()