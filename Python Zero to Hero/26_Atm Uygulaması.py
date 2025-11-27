
print("""Merhabalar Hoşgeldiniz""")

veritabanı = { "ErenHesap":{
    "İsim" : "Eren",
    "Soyisim" : "Yalçın",
    "Kartsifre" : "1212",
    "HesapBakiye" : 10000,
    "KrediKartBorc" : 1500,
    "KrediKartBorcTarihi" : "20/11/2025"},
             "İzemHesap":{
    "İsim" : "İzem",
    "Soyisim" : "Türkmen",
    "Kartsifre" : "1234",
    "HesapBakiye" : 60000,
    "KrediKartBorc" : 12500,
    "KrediKartBorcTarihi" : "20/11/2025"}}
              
TakılanKart = dict(veritabanı["ErenHesap"])

hak = 2
sec = ""

for i in range(0,3):
    Sifre = input("Lütfen 4 haneli Şifrenizi Giriniz:")

    if Sifre == TakılanKart.get("Kartsifre"):
        print("""Merhaba Hoşgeldiniz Sayın {} {} 
Lütfen Yapmak İstediğiniz İşlemi Seçiniz...""".format(
            TakılanKart.get("İsim"), TakılanKart.get("Soyisim")))

        sec = input("""  
[1] Bakiye Sorgula
[2] Kredi Kart Borc Sorgula
[3] Para Cekme
[4] Para Yatırma
[Q] Kart İade\n   """)
    
    elif Sifre != TakılanKart.get("Kartsifre") and hak != 0:
         print("Hatalı Şifre Girdiniz. Kalan Hakkınız {}".format(hak))
         hak -=1

    elif Sifre != TakılanKart.get("Kartsifre") and hak == 0:
         # Son hakkı da yanlış girerse burada sadece mesaj verelim,
         # exit() ile programı bitirmeyelim ki for-else'ye düşebilesin.
        print("Kartınızı 3 defa Hatalı Girdiğinizden Dolayı Kartınız Bloke Olmuştur.")
         
    if sec != "":     
        if  sec == "1":
            print("Hesap Bakiyeniz {} TL'dir ".format(TakılanKart.get("HesapBakiye")))
            break
        
        elif sec == "2":
            print("Kredi Kartı Borç Bakiyeniz {} TL'dir, Son Ödeme Tarihiniz {}".format(
                TakılanKart.get("KrediKartBorc"), TakılanKart.get("KrediKartBorcTarihi")))
            break
        
        elif sec == "3":
            Miktar1 = int(input("Çekilicek Tutarı Giriniz:"))
            if TakılanKart.get("HesapBakiye") < Miktar1:
                print("Yetersiz Bakiye.")
                break
            else:
                print("Lütfen Paranızı Kontrol Ederek Alınız...")
                yenibakiye = TakılanKart.get("HesapBakiye") - Miktar1
                print("Kalan Bakiyeniz {} TL'dir".format(yenibakiye))
        
        elif sec == "4":
            Miktar2 = int(input("Lütfen Yatırılıcak Tutarı Giriniz:"))
            print("Paranız Hesabınıza Yatırılmıştır.")
            yenibakiye2 =  TakılanKart.get("HesapBakiye") + Miktar2
            print("Güncel Bakiyeniz {} TL'dir".format(yenibakiye2))
            break

        elif sec == "Q" or sec == "q":
            print("Teşekkürler, İyi Günler...")
            exit()
            
        
        else:
            print("Lütfen Geçerli Bir Giriş Yapınız!")

       # doğru şifre + işlemden sonra şifre döngüsünden çık

    # elif Sifre != TakılanKart.get("Kartsifre") and hak != 0:
    #      print("Hatalı Şifre Girdiniz. Kalan Hakkınız {}".format(hak))
    #      hak -=1

    # elif Sifre != TakılanKart.get("Kartsifre") and hak == 0:
    #      # Son hakkı da yanlış girerse burada sadece mesaj verelim,
    #      # exit() ile programı bitirmeyelim ki for-else'ye düşebilesin.
    #      print("Kartınızı 3 defa Hatalı Girdiğinizden Dolayı Kartınız Bloke Olmuştur.")
    #    # exit() KALDIRILDI

    else:
     # Buraya sadece for döngüsü HİÇ break görmeden biterse gelinir.
     # Yani: 3 denemenin HİÇBİRİNDE doğru şifre girilmemişse.
     print("Lütfen Geçerli Bir Giriş Yapınız!")
