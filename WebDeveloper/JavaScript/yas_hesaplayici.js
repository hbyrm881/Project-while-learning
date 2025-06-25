function hesapla() {
    const yil = new Date().getFullYear();
    let a = document.getElementById("yas").value;
    let suankiYas = yil - a;
    if (a === "" || isNaN(a) || a < 1900|| a > yil) {
        alert("Lütfen geçerli bir yıl giriniz.");
    }
    else {
        console.log("Yaşınız: " + suankiYas)
        document.getElementById("ekran").innerHTML = "Yaşınız: " + suankiYas;
    }
}