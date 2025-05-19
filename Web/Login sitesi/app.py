from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

KULLANICI_ADI = "Hasan"
SIFRE = "1234"

@app.route("/")
def giris ():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login ():
    kullanici_adi = request.form("kullanici_adi")
    sifre = request.form("sifre")

    if kullanici_adi == KULLANICI_ADI and sifre == SIFRE:
        return redirect(url_for('Hos Geldin'))
    else:
        return "Hatalı kullanıcı adı veya şifre. <a href='/'>Tekrar dene</a>"
    
app.route('/welcome')
def hosgeldin():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)