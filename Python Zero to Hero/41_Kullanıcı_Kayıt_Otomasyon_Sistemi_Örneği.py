import re
import time

class Kayıt:
   
    def __init__(self,programad):

        self.programad = programad
        self.dongu = True
        

    def program(self):
        secim = self.menu()

        if secim == "1":
            print("Kayıt Ekleme Menüsüne Yönlendiriliyorsunuz...")
            time.sleep(3)
            self.kayitekle()

        elif secim == "2":
            print("Kayıt Silme Menüsüne Yönlendiriliyorsunuz...")
            time.sleep(3)
            self.kayitcikar()

        elif secim == "3":
            print("Veriler Okunuyor...")
            time.sleep(3)
            self.kayitoku()

        elif secim == "4":
            self.cikis()
    
            
            
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("Lütfen 1 ve 4 arasında Geçerli Bir Seçim Yapınız....")
            elif len(secim) != 1:
                raise Exception("Lütfen 1 ve 4 arasında Geçerli Bir Seçim Yapınız....")
        
        while True:
            try:
                secim = input("Merhabalar {} Otomasyon Sistemine Hoşgeldiniz\n\n Lütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n[1] Kayıt Ekle\n[2] Kayıt Sil\n[3] Kayıt Oku\n[4] Çıkış\n\n".format(self.programad))
                kontrol(secim)
            except Exception as hata:
                print(hata)
                # time.sleep(3)
            else:
                break
        return secim #dk23

    def kayitekle(self):

        def kontrolad(Ad):
            if Ad.isalpha() == False:
                raise Exception("Adınız Sadece Alfabetik Karakterlerden Oluşmalıdır....")
        while True:
            try:
                Ad = input("Lütfen Adınızı Giriniz.")
                kontrolad(Ad)
            except Exception as hataad:
                print(hataad)
                time.sleep(3)
            else:
                break

        def kontrolsoyad(Soyad):
            if Soyad.isalpha() == False:
                raise Exception("Soyadınız Sadece Alfabetik Karakterlerden Oluşmalıdır....")
        while True:
            try:
                Soyad = input("Lütfen Soyadınızı Giriniz.")
                kontrolsoyad(Soyad)
            except Exception as hatasoyad:
                print(hatasoyad)
                time.sleep(3)
            else:
                break

        def kontrolyas(Yas):
            if Yas.isdigit() == False:
                raise Exception("Yaşınız Sadece Rakamlardan Oluşmalıdır....")
        while True:
            try:
                Yas = input("Lütfen Yaşınızı Giriniz.")
                kontrolyas(Yas)
            except Exception as hatayas:
                print(hatayas)
                time.sleep(3)
            else:
                break

        def kontroltc(Tc):
            if Tc.isdigit() == False:
                raise Exception("TC Numaranız  Rakamlardan Oluşmalıdır....")
            elif len(Tc) != 11:
                raise Exception("TC Numaranız 11 Karakterden Olmalıdır. ")
        while True:
            try:
                Tc = input("Kimlik Numaranız:")
                kontroltc(Tc)
            except Exception as hatatc:
                print(hatatc)
                time.sleep(3)
            else:
                break

        def kontrolmail(Mail):
            if not re.search(".com",Mail):    
                raise Exception("Geçerli Bir Mail Adresi Giriniz.")

        while True:
            try:
                Mail = input("Mail Adresiniz::")
                kontrolmail(Mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(3)
            else:
                break #dk39
        
        with open("C:/Users/MONSTER/Desktop/anam.txt","r",encoding="utf-8") as Dosya:
            satırsayısı = Dosya.readlines()
        if len(satırsayısı) == 0:
            Id = 1
        else:
             with open("C:/Users/MONSTER/Desktop/anam.txt","r",encoding="utf-8") as Dosya:
                 Id = int(Dosya.readlines()[-1].split("-")[0]) +1

        with open("C:/Users/MONSTER/Desktop/anam.txt","a+",encoding="utf-8") as Dosya:
            Dosya.write("{}-{} {} {} {} {}\n".format(Id,Ad,Soyad,Yas,Tc,Mail))
            print("Veriler İşlenmiştir!\n")

        self.menudon() 
        

    def kayitcikar(self):
        y = input("Lütfen Silmek istediğiniz kişinni id numarasını giriniz...:")
        with open("C:/Users/MONSTER/Desktop/anam.txt","r",encoding="utf-8") as Dosya:
            liste = []
            liste2 = Dosya.readlines()
            for i in range(0,len(liste2)):
                liste.append(liste2[i].split("-")[0].strip())

        del liste2[liste.index(y)]

        with open("C:/Users/MONSTER/Desktop/anam.txt","w+",encoding="utf-8") as Yenidosya:

            for i in liste2:
                Yenidosya.write(i)
        print("Kayıt Siliniyor...")
        time.sleep(3)
        print("KayıT Başarıyla Silindi")
        
        self.menudon()


    def kayitoku(self):
        with open("C:/Users/MONSTER/Desktop/anam.txt","r",encoding="utf-8") as Dosya:
            for i in Dosya:
                 print(i)
            self.menudon()

    def cikis(self):
        print("Otomasyondan Çıkılıyor Teşekkürler....")
        time.sleep(2)
        self.dongu = False
        exit()
       

    def menudon(self):
        while True:
            x = input("Ana Menüye Dönmek İçin 6'ya, Çıkmak için 5'e Basınız.")
            if x =="6":
                print("Ana Menüye Dönülüyor")
                time.sleep(2)
                self.program()
                break
            elif x =="5":
                self.cikis()
                break
            else:
                print("Lütfen Geçerli Bir Seçim Yapınız")
            

Sistem = Kayıt("Eren Yalçın")
while Sistem.dongu:
    Sistem.program()

