from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def anasayfa():
    if request.method == "POST": # butona basınca POST değeri döndürür ve alttaki kod bloğu çalışır
        gelen_sifre = request.form.get("sifre")#gelen şifrreyi değişkene atadık
        return f"Alınan şifre: {gelen_sifre}"
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)