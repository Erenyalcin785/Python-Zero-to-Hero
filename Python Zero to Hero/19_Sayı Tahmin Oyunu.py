sayi = 25
hak = 10

while hak>0:
    tahmin = int(input("Lütfen Pozitif Bir Tam Sayı Giriniz:"))
    if tahmin <0:
        print("Girdiginiz Sayı Pozitif Değil!")
        continue
    hak -=1
    if sayi == tahmin:
        print("Doğru Tahmin! :)")
        break
    elif sayi > tahmin:
        print("Yukarı, Kalan Hakkınız {}".format(hak))
    else:
        print("Aşağı, Kalan Hakkınız {}".format(hak))
    if hak == 0:
        print("Hakkınız Kalmamıştır. Doğru sayı {}".format(sayi))