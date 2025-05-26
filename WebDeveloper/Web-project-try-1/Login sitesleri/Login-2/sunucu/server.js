const express = require("express");
const path = require("path");
const app = express();
const PORT = 3000;

// JSON body okumak için
app.use(express.json());

// Statik dosyaları sun (index.html, style.css, script.js)
app.use(express.static(path.join(__dirname, ".."))); // üst klasörden sun

const users = [];

app.post("/kayit", (req, res) => {
    const { username, password } = req.body;
    users.push({ username, password });
    res.json({ success: true, message: "Kayıt başarılı!" });
});

app.post("/giris", (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username && u.password === password);
    
    if (user) {
        res.json({ success: true, message: "Giriş başarılı!" });
    } else {
        res.json({ success: false, message: "Kullanıcı adı veya şifre hatalı!" });
    }
});

app.listen(PORT, () => {
    console.log(`Sunucu çalışıyor: http://localhost:${PORT}`);
});
