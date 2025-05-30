const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");
const cors = require("cors");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(express.static("public")); // frontend dosyalarını sunar

// Kullanıcı kayıt işlemi
app.post("/register", (req, res) => {
    const { email, username, password } = req.body;

    if (!email || !username || !password) {
        return res.status(400).json({ message: "Eksik bilgi" });
    }

    let users = [];

    if (fs.existsSync("users.json")) {
        const data = fs.readFileSync("users.json");
        users = JSON.parse(data);
    }

    // Aynı kullanıcı adı var mı kontrol
    if (users.find(user => user.username === username)) {
        return res.status(409).json({ message: "Kullanıcı zaten var" });
    }

    users.push({ email, username, password });
    fs.writeFileSync("users.json", JSON.stringify(users, null, 2));

    res.status(201).json({ message: "Kayıt başarılı" });
});

// Giriş işlemi
app.post("/login", (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.status(400).json({ message: "Eksik bilgi" });
    }

    if (!fs.existsSync("users.json")) {
        return res.status(401).json({ message: "Kullanıcı yok" });
    }

    const users = JSON.parse(fs.readFileSync("users.json"));

    const user = users.find(user => user.username === username && user.password === password);

    if (!user) {
        return res.status(401).json({ message: "Kullanıcı adı veya şifre hatalı" });
    }

    res.status(200).json({ message: "Giriş başarılı" });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
