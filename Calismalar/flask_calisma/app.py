from flask import Flask, request, render_template
import webbrowser
from threading import Timer
rakam_var=False
ozel_karakter=False
buyuk_harf=False
sifre_gizli=False
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def anasayfa():
    global rakam_var, ozel_karakter, buyuk_harf, sifre_gizli
    sinif_adi=""
    sonuc=""
    if request.method == "POST": # butona basınca POST değeri döndürür ve alttaki kod bloğu çalışır
        gelen_sifre = request.form.get("sifre")#gelen şifrreyi değişkene atadık
        sinif_adi=f"bekleniyor"
        sonuc=f'Şifre Güvenliği: '
        #----------- Şifre kontrolleri ----------#
        if len(gelen_sifre)  <4:
            sinif_adi="buyukluk"
            sonuc="Şifreniz en az 4 harfli olmalıdır!"
        if len(gelen_sifre) >= 4:
            rakam_var = False
            ozel_karakter=False
            buyuk_harf=False
            for karakter in gelen_sifre:
                    if karakter.isdigit():
                        rakam_var=True
                    if karakter.isupper():
                        buyuk_harf=True
                    if not karakter.isalnum():
                        ozel_karakter=True   
            if rakam_var == False:
                sinif_adi="rakam"
                sonuc="Şifrenizde en az 1 rakam bulunmalıdır!"
            elif buyuk_harf == False:
                sinif_adi="buyukharf"
                sonuc="Şifrenizde en az 1 büyük harf bulunmalıdır!"
            elif ozel_karakter == False:
                sinif_adi="ozelkarakter"
                sonuc="Şifrenizde en az 1 özel karakter bulunmalıdır! Örn: - _ * \\ / & + ? ="
            else:
                sinif_adi="guvenli"
                sonuc="✨Şifreniz güvenli🎉"
    return render_template("index.html", sonuc=sonuc, sinif_adi=sinif_adi)
if __name__ == "__main__":
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000/")).start()
    app.run(debug=True)