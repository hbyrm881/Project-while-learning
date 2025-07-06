function showLogin() {
    document.querySelector(".start-screen").classList.add("hidden");

    const loginScreen = document.querySelector(".login-screen");
    loginScreen.classList.remove("hidden");

    loginScreen.classList.remove("fade-in");
    void loginScreen.offsetWidth;
    loginScreen.classList.add("fade-in");
}

function showRegister() {
    document.querySelector(".start-screen").classList.add("hidden");

    const registerScreen = document.querySelector(".register-screen");
    registerScreen.classList.remove("hidden");

    registerScreen.classList.remove("fade-in");
    void registerScreen.offsetWidth;
    registerScreen.classList.add("fade-in");
}

function geriDon() {
    document.querySelector(".login-screen").classList.add("hidden");
    document.querySelector(".register-screen").classList.add("hidden");
    document.querySelector(".start-screen").classList.remove("hidden");
}

function kayitOl() {
    const email = document.getElementById("email").value.trim();
    const username = document.getElementById("username-register").value.trim();
    const password = document.getElementById("password-register").value;
    const password2 = document.getElementById("password-register2").value;

    if (!email || !username || !password || !password2) {
        alert("Lütfen tüm alanları doldurun.");
        return;
    }

    if (!email.includes("@") || !email.includes(".")) {
        alert("Geçerli bir e-posta adresi girin.");
        return;
    }

    if (password !== password2) {
        alert("Şifreler eşleşmiyor.");
        return;
    }

    fetch("http://localhost:3000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, username, password })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        if (data.message === "Kayıt başarılı") {
            geriDon();
        }
    })
    .catch(err => {
        console.error(err);
        alert("Sunucu hatası.");
    });
}

function girisYap() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    if (!username || !password) {
        alert("Lütfen kullanıcı adı ve şifreyi girin.");
        return;
    }

    fetch("http://localhost:3000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        if (data.message === "Giriş başarılı") {
            // Giriş başarılıysa başka ekrana geçiş yapabilirsin
            console.log("Kullanıcı başarıyla giriş yaptı.");
        }
    })
    .catch(err => {
        console.error(err);
        alert("Sunucu hatası.");
    });
}
