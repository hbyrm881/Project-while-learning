function veri_al() {
    let a = document.getElementById("isimappi").value;
    if (a === "") {
        alert("Lütfen bir isim giriniz.");
    }
    else {
        console.log("Hoş Geldin " + a);
        document.body.innerHTML = "<h1>Hoş Geldin " + a + "</h1>";
         
    }
}