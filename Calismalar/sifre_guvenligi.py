import msvcrt

import os
import time
from rich import print
metin = ""
rakam_var=False
ozel_karakter=False
buyuk_harf=False
sifre_gizli=False
kapatma = ["|", "/", "\\"]
print("[bold purple]Sifre  guvenligi uygulamasına hos geldin! \n(Not cıkmak icin 5 kez q yazınız)\n (Yazdiginiz sifrenin ekranda gozukmemesini istiyorsanız istemiyorum yazin (sure bitince))")
time.sleep(6)

os.system('cls')
def guvenlik(mod, text):
    if mod == "gizli":
        print("*" * len(text))
    elif mod == "degil":
        print(text)
def programi_baslat():
    global rakam_var, ozel_karakter, buyuk_harf, metin, sifre_gizli, kapatma
    while True:
        try:
            harf = msvcrt.getch().decode('utf-8')
            os.system('cls')
            if harf == "\x08":
                metin=metin[:-1]
            else:
                metin += harf
            
            if metin == "qqqqq":
                for i in range(10):
                    os.system('cls')
                    print(f"Program Kapatiliyor... {kapatma[i % len(kapatma)]}", end="", flush=True)
                    time.sleep(0.3)
                break
            if metin == "istemiyorum":
                sifre_gizli = True
                metin=""
                os.system('cls')
                continue
            
            if sifre_gizli:
                guvenlik("gizli", metin)
            else:
                guvenlik("degil", metin)
            if len(metin) < 4:
                print("[bold red][!] Sifreniz cok kisa")
            if len(metin) >= 4:
                rakam_var = False
                ozel_karakter=False
                buyuk_harf=False
                for karakter in metin:
                    if karakter.isdigit():
                        rakam_var=True
                    if karakter.isupper():
                        buyuk_harf=True
                    if not karakter.isalnum():
                        ozel_karakter=True
                if rakam_var == False:
                    print("[bold yellow][!] Sifrenizde en az bir rakam olmalıdır", end="\r \r \r")
                elif buyuk_harf == False:
                    print("[red][!] Sifrenizde en az bir buyuk harf olmalıdır.")
                elif ozel_karakter == False:
                    print("[bold purple][!] Sifrenizde en az bir ozel karakter olmalıdır ornek: _ & / % - ^ , .")
                else:
                    print("[bold green][🎈] Sifreniz guvenli(Yeni birşey yapana kadar)", end="\r")
        except UnicodeDecodeError: #çökmesini engelliyoruz
            print("[bold red][!] Lutfen sadece ingilizce harf kullaniniz.")
programi_baslat()