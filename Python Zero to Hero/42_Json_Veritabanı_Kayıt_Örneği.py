import json
import re
import time
import random

class Site:
    def __init__(self):
        self.dongu = True
        self.veriler = self.verial()

    def program(self):

        secim = self.menu()

        if secim == "1":
            self.giris()
        elif secim =="2":
            self.kayitol()
        elif secim == "3":
            self.cikis()


    def menu(self):
        def kontrol(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lütfen 1 ve 3 arasında Geçerli Bir Seçim Yapınız..")
            elif len(secim) != 1:
                raise Exception("Lütfen 1 ve 3 arasında Geçerli Bir Seçim Yapınız..")
            
        while True:
            try:
                secim = input("Merhabalar Erenoska Sitesine Hoşgeldiniz.\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz\n\n[1] Giriş\n[2] Kayıt Ol\n[3] Çıkış\n\n")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        
        return secim
    

    def giris(self):

        print("Giriş Menüsüne Yönlendiriliyorsunuz...")
        time.sleep(2)

        kullaniciadi = input("Lütfen Kullanıcı Adınızı Giriniz:")
        sifre = input("Lütfen Şifrenizi Giriniz:")
        
        sonuc = self.giriskontrol(kullaniciadi,sifre) # sonuc yazarak dene 

        if sonuc == True:
            self.girisbasarili()
        else:
            self.girisbasarisiz()
            self.menu()

    
    def giriskontrol(self,kullaniciadi,sifre):
        
        self.veriler = self.verial()
        try:
            for kullanici in self.veriler["Kullanıcılar"]:
                if kullanici["Kullanıcıadı"] == kullaniciadi and kullanici["Sifre"] == sifre:
                    return True
        except TypeError:
            return False
        return False

    def girisbasarili(self):
        
        print("Kontrol Ediliyor...")
        time.sleep(2)
        print("Giriş Başarılı, Hoşgeldiniz...")
        self.sonuc = False
        self.dongu = False
    
    def girisbasarisiz(self):
        
        print("Kullanıcı Adı veya Şifre Hatalı!")
        time.sleep(2)
        self.menudon()

    def kayitol(self):
        def kontrolk(kullaniciadi):
            if len(kullaniciadi) <8:
                raise Exception("Kullanıcı Adı En Az 8 Karakterden Oluşmalıdır.")
        
        while True:
            try:
                kullaniciadi = input("Kullanıcı Adınız:")
                kontrolk(kullaniciadi)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break

        def kontrolsifre(sifre):
            if len(sifre) <8:
                raise Exception("Şifreniz En Az 8 Karakterden Oluşmalıdır.")
            elif not re.search("[^0-9]",sifre):
                raise Exception("Şifrenizde En Az Bir Tane  Rakam Olmalıdır.")
            elif not re.search("[^A-Z]",sifre):
                raise Exception("Şifrenizde En Az Bir Tane  Büyük Harf Olmalıdır.") 
            elif not re.search("[^a-z]",sifre):
                raise Exception("Şifrenizde En Az Bir Tane Küçük HarfOlmalıdır.")       
        while True:
            try:
                sifre = input("Şifreniz:")
                kontrolsifre(sifre)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break
        
        def kontrolmail(Mail):
            if not re.search(".com",Mail):
                raise Exception("Geçerli Bir Mail Adresi Giriniz.")
       
        while True:
            try:
                Mail = input("Mail Adresinizi Giriniz:")
                kontrolmail(Mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(2)
            else:
                break
        
        sonuc = self.kayitvarmi(kullaniciadi,Mail)
        if sonuc == True:
            print("Bu Kullanıcı Adı ve Mail Sistemde Kayıltı...")
        else:
            aktivasyonkodu=self.aktivasyongonder()
            ###
        while True:
            durum=self.aktivasyonkontrol(aktivasyonkodu) ### üstteki işaretten buraya taşıdın else düzgün çalışsın diye
            if durum == True:
                self.verikaydet(kullaniciadi,sifre,Mail)
                break
            else:
                print("Tekrar Deneyin...")
                #input("Gerçersiz Aktivasyon Kodu Lütfen Tekrar Giriniz.")


    def kayitvarmi(self,kullaniciadi,Mail):
        self.veriler = self.verial()
        try:
            for kullanici in self.veriler["Kullanıcılar"]:
                if kullanici["Kullanıcıadı"] == kullaniciadi and kullanici["Mail"] == Mail:
                    return True
        except KeyError:
            return False
        return False

        
    def aktivasyongonder(self):

        with open ("C:/Users/MONSTER/Desktop/Aktivasyon.txt","w",encoding="utf-8") as Dosya:
            aktivasyon = str(random.randint(10000,99999))
            Dosya.write("Aktivasyon Kodunuz:" + aktivasyon)
        return aktivasyon

        

    def aktivasyonkontrol(self,aktivasyon):
        aktivasyonkodual = input("Lütfen Size Gönderilen Aktivasyon Kodunu Giriniz.")
        if aktivasyon == aktivasyonkodual:
            return True
        else:
            return False

    def verial(self):
        yol = "C:/Users/MONSTER/Desktop/Kullanıcılıar.json"
        try:
            with open(yol,"r",encoding="utf-8") as Dosya:
                veriler = json.load(Dosya)
        except FileNotFoundError:
            with open(yol,"w",encoding="utf-8") as Dosya:
                Dosya.write("{}")
            with open(yol,"r",encoding="utf-8") as Dosya:
                veriler = json.load(Dosya)
        except json.JSONDecodeError:
            with open(yol, "w", encoding="utf-8") as Dosya:
                Dosya.write("{}")
            veriler = {}
                
        return veriler
        

    def verikaydet(self,kullaniciadi,sifre,Mail):
        self.veriler = self.verial()

        try:
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı": kullaniciadi,"Sifre":sifre,"Mail":Mail})
        except (TypeError,KeyError):
            self.veriler["Kullanıcılar"] = list()
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı": kullaniciadi,"Sifre":sifre,"Mail":Mail})
        with open ("C:/Users/MONSTER/Desktop/Kullanıcılıar.json","w",encoding="utf-8") as Dosya:
            json.dump(self.veriler,Dosya, ensure_ascii=False, indent=4)
            print("Kayıt Başarılı Şekilde Oluşturulmuştur.")
        self.menudon()

    
    def cikis(self):
        print("Çıkış Yapılıyor... ")
        time.sleep(2)
        self.dongu = False
        exit()

    
    def menudon(self):
        while True:
            x = input("Ana Menüye Dönmek İçin 5'e, Çıkmak İçin 6'ya basınız")
            
            if x == "5":
                print("Ana Menüye Dönülüyor...")
                time.sleep(2)
                self.program()    
                break

            elif x == "6":
                self.cikis()
                break
            
            else:
                print("Hatalı Tuşlama Yaptınız!")


Sistem = Site()
while Sistem.dongu:
    Sistem.program()