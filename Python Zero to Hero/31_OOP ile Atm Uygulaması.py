class Musteri():
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartborc,sonodeme):
        self.ad = ad
        self.soyad = soyad
        self.kartsifre = kartsifre
        self.hesapbakiye = hesapbakiye
        self.kredikartborc = kredikartborc
        self.sonodeme = sonodeme

ErenHesap = Musteri("Eren","Yalçın","1111",10000,2500,"20/11/2025")
MehmetHesap = Musteri("Mehmet","Duyar","1234",50000,30000,"26/04/2025")

TakılanKart = ErenHesap

class ATM:
    def __init__(self,atmad):
        self.atmdad = atmad
        self.dongu = True
        self.giriskontrol()
        

    def program(self):
        secim = self.menu()
        
        if secim == 1:
            self.bakiye()
        if secim == 2:
            self.kkborc()
        if secim == 3:
            self.paracek()
        if secim == 4:
            self.parayatır()
        if secim == 5:
            self.cıkıs()


    def giriskontrol(self):
        hak = 2
        for i in range(0,3):
            sifre = input("Lütfen 4 Haneli Şifrenizi Giriniz:")
            if sifre == TakılanKart.kartsifre:
                self.program()
                return
            elif sifre != TakılanKart.kartsifre and hak != 0:
                print("Hatalı Şifre Girdiniz Kalan Hakkınız {}".format(hak))
                hak -= 1
            elif sifre != TakılanKart.kartsifre and hak == 0:
                print("Şifrenizi 3 Defa Hatalı Girdiiğinizden Dolayı Kartınız Bloke Olmuştur.")
                exit()


    def menu(self):
        secim = int(input("""Merhabalar, {}'a Hoşgeldiniz Sayın {} {}.\n\nLütfen Yapmak istediğiniz İşlemi Seçiniz...
                       
            [1] Bakiye Sorgulama
            [2] Kredi Kartı Borç Sorgulama
            [3] Para Çekme
            [4] Para Yatırma 
            [5] Kart İade 
                          
Seçim:""".format(self.atmdad,TakılanKart.ad,TakılanKart.soyad)))
        while secim < 1 or secim > 5:
            print("Lütfen 1 ve 5 Arasında Geçerli Bir Değer Giriniz...\nAna Menüye Dönülüyor")
            secim = int(input("Seçim:"))

        return secim

    def bakiye(self):

            print("Hesap Bakiyeniz: {} TL'dir".format(TakılanKart.hesapbakiye))
            self.dongu = False
            self.menudon()


    def kkborc(self):

        print("Kredi Kartı Borcunuz {} Son Ödeme Tarihli {} TL'dir.".format(TakılanKart.sonodeme,TakılanKart.kredikartborc))
        self.dongu = False
        self.menudon()

    def paracek(self):

        miktar = int(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz:"))
        
        if miktar > TakılanKart.hesapbakiye:

            print("Yetersiz Bakiye. Güncel Bakiyeniz {} TL'dir".format(TakılanKart.hesapbakiye))
            self.menudon()

        else:       

            TakılanKart.hesapbakiye -= miktar
            print("Kalan Bakiyeniz {} TL'dir".format(TakılanKart.hesapbakiye))
            self.menudon()

    def parayatır(self):

        miktar2 = int(input("Yatırmak İstediğiniz Tutarı Giriniz:"))
        TakılanKart.hesapbakiye += miktar2
        print("Hesaptaki Güncel Bakiyeniz: {} TL'dir".format(TakılanKart.hesapbakiye))
        self.menudon()


    def cıkıs(self):
        
        print("Bankamızı Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        exit()
        

    def menudon(self):
        x = int(input("""Ana Menüye Dönmek İçin Lütfen 7 tuşuna Basınız. Kart İade İçin 5'e Basınız..."""))
        if x == 7:

            self.program()
        
        elif x == 5:
        
            self.cıkıs()

Banka = ATM("Xbank")
while Banka.dongu:
    Banka.program()






    
        

