function topla() {
    let a = document.getElementById("sayi1").value;
    let b = document.getElementById("sayi2").value;
    let sonuc = parseInt(a) + parseInt(b);
    document.getElementById("ekranayaz").innerHTML = sonuc;
    console.log("Toplama işlemi yapıldı: " + sonuc);
}
function cikar() {
    let a = document.getElementById("sayi1").value;
    let b = document.getElementById("sayi2").value;
    let sonuc = parseInt(a) - parseInt(b);
    document.getElementById("ekranayaz").innerHTML = sonuc;
    console.log("Çıkarma işlemi yapıldı: " + sonuc);
}
function carp() {
    let a = document.getElementById("sayi1").value;
    let b = document.getElementById("sayi2").value;
    let sonuc = parseInt(a) * parseInt(b);
    document.getElementById("ekranayaz").innerHTML = sonuc;
    console.log("Çarpma işlemi yapıldı: " + sonuc)
}
function bol() {
    let a = document.getElementById("sayi1").value;
    let b = document.getElementById("sayi2").value;
    if (b == 0) {
        alert("bir sayı 0'a bölünmez!");
    } else {
        let sonuc = parseInt(a) / parseInt(b);
        sonuc = sonuc.toFixed(2); // Sonucu iki ondalık basamakla göster
        document.getElementById("ekranayaz").innerHTML = sonuc;
        console.log("Bölme işlemi yapıldı: " + sonuc);
    }
    }