function showLogin() {
    document.querySelector(".start-screen").classList.add("hidden");
    
    const loginScreen = document.querySelector(".login-screen");
    loginScreen.classList.remove("hidden");
    
    // Animasyonu tetikle
    loginScreen.classList.remove("fade-in"); // önce temizle
    void loginScreen.offsetWidth;            // yeniden başlatmak için zorla repaint
    loginScreen.classList.add("fade-in");
}

function showRegister() {
    document.querySelector(".start-screen").classList.add("hidden");

    const registerScreen = document.querySelector(".register-screen");
    registerScreen.classList.remove("hidden");

    // Animasyonu tetikle
    registerScreen.classList.remove("fade-in");
    void registerScreen.offsetWidth;
    registerScreen.classList.add("fade-in");
}

function girisYap() {
    const girilenkullanici = document.getElementById("username").value;
    const girilenSifre = document.getElementById("password").value;

    const kayitliKullanici = localStorage.getItem("kullaniciAdi");
    const kayitliSifre = localStorage.getItem("sifre");

    if (!girilenkullanici | !girilenSifre) {
        alert("Lütfen kullanıcı adı ve şifreyi girin.");
        return;
    }

    if (girilenkullanici === kayitliKullanici && girilenSifre === kayitliSifre) {
        alert("Giriş başarılı!");
        // Burada istersen başka sayfa açabilirsin veya ekranda başka içerik gösterebilirsin
    } else {
        alert("Kullanıcı adı veya şifre hatalı!");
    }
}
function geriDon() {
    document.querySelector(".login-screen").classList.add("hidden");
    document.querySelector(".start-screen").classList.remove("hidden");
    document.querySelector(".register-screen").classList.add("hidden")
}
function kayitOl() {
    const email = document.getElementById("email").value.trim();
    const username = document.getElementById("username-register").value.trim();
    const password = document.getElementById("password-register").value;
    const password2 = document.getElementById("password-register2").value;

    if (!email ||  !username ||  !password || !password2) {
        alert("Lütfen tüm alanları doldurun.");
        return;
    }

    if (!email.includes("@") || !email.includes(".")) {
        alert("Geçerli bir e-posta adresi girin.");
        return;
    }

    if (password !== password2) {
        alert("Şifreler eşleşmiyor.")
        return;
    }

    //Bilgileri kaydet (localStorage)
    localStorage.setItem("kullaniciAdi", username);
    localStorage.setItem("sifre", password);

    alert("Kayıt Başarılı!");

    //Ekranı geri döndür
    document.querySelector(".register-screen").classList.add("hidden");
    document.querySelector(".start-screen").classList.remove("hidden");
}