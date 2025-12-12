import json
import re
import time
import random


DB_PATH = "C:/Users/MONSTER/Desktop/veritabani.json"

def veriyi_yukle():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        data = {
            "kullanicilar": [],
            "gorevler": [],
            "ticketlar": []
        }
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return data


def veriyi_kaydet(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def kullanici_adi_var_mi(data, kullanici_adi):
    for k in data["kullanicilar"]:
        if k["kullanici_adi"] == kullanici_adi:
            return True
    return False


def aktivasyon_kodu_olustur():
    return str(random.randint(1000, 9999))


#  KAYIT OL / GİRİŞ
def kayit_ol(data):
    print("\n--- KAYIT OL ---")

    while True:
        kullanici_adi = input("Kullanıcı adı: ").strip()

        if not kullanici_adi:
            print("HATA: Kullanıcı adı boş olamaz.")
            continue

        if len(kullanici_adi) < 3:
            print("HATA: Kullanıcı adı en az 3 karakter olmalı.")
            continue

        if not re.match(r"^[A-Za-z0-9_]+$", kullanici_adi):
            print("HATA: Kullanıcı adı sadece harf, rakam ve alt çizgi (_) içerebilir.")
            continue

        if kullanici_adi_var_mi(data, kullanici_adi):
            print("HATA: Bu kullanıcı adı zaten kullanılıyor. Başka bir tane dene.")
            continue

        break

    while True:
        mail = input("Mail adresi: ").strip()

        if not mail:
            print("HATA: Mail adresi boş olamaz.")
            continue

        if not re.search(r"^[^@]+@[^@]+\.[^@]+$", mail):
            print("HATA: Mail formatı yanlış.")
            continue

        break

    while True:
        sifre = input("Şifre: ").strip()

        hata_var = False

        if len(sifre) < 6:
            print("En az 6 karakter olmalı.")
            hata_var = True

        if not re.search(r"[A-Z]", sifre):
            print("En az 1 büyük harf olmalı (A-Z).")
            hata_var = True

        if not re.search(r"[a-z]", sifre):
            print("En az 1 küçük harf olmalı (a-z).")
            hata_var = True

        if not re.search(r"[0-9]", sifre):
            print("En az 1 rakam olmalı (0-9).")
            hata_var = True

        if hata_var:
            print("Lütfen şifreyi tekrar dene.\n")
            continue

        sifre_tekrar = input("Şifre tekrar: ").strip()
        if sifre != sifre_tekrar:
            print("Şifreler aynı değil, tekrar dene.\n")
            continue

        break

    kod = aktivasyon_kodu_olustur()


    masaustu = "C:/Users/MONSTER/Desktop/aktivasyon_kodu.txt"

    with open(masaustu, "w", encoding="utf-8") as Dosya:
        Dosya.write("Aktivasyon kodun: " + kod)
    
    print("Lütfen dosyayı aç ve içindeki kodu buraya yaz.\n")

    deneme_sayisi = 0
    while True:
        girilen = input("Aktivasyon kodu: ").strip()

        if girilen == kod:
            print("Aktivasyon başarılı.")
            break
        else:
            deneme_sayisi += 1
            print("HATA: Aktivasyon kodu yanlış.")

            if deneme_sayisi >= 3:
                print("Çok fazla yanlış deneme yaptın. Kayıt iptal edildi.")
                return None
            else:
                print("Tekrar deneyebilirsin.\n")

    # TÜM BİLGİLER TAM, KAYDI YAP 
    yeni = {
        "kullanici_adi": kullanici_adi,
        "sifre": sifre,
        "mail": mail
    }

    data["kullanicilar"].append(yeni)
    veriyi_kaydet(data)

    print("Kayıt başarılı! Artık giriş yapabilirsin.")
    return kullanici_adi 


def giris_yap(data):
    print("\n--- GİRİŞ YAP ---")
    kullanici_adi = input("Kullanıcı adı: ").strip()
    sifre = input("Şifre: ").strip()

    for k in data["kullanicilar"]:
        if k["kullanici_adi"] == kullanici_adi and k["sifre"] == sifre:
            print("Giriş başarılı!")
            return kullanici_adi

    print("HATA: Kullanıcı adı veya şifre yanlış.")
    return None

#   TO-DO (GÖREV)
def gorev_id_olustur(data):
    mevcut = []
    for g in data["gorevler"]:
        mevcut.append(g["id"])
    while True:
        yeni = random.randint(1, 999999)
        if yeni not in mevcut:
            return yeni


def gorev_ekle(data, kullanici):
    print("\n--- GÖREV EKLE ---")
    metin = input("Görev metni: ").strip()
    if not metin:
        print("HATA: Boş görev ekleyemezsin.")
        return

    yeni = {
        "id": gorev_id_olustur(data),
        "sahip": kullanici,
        "metin": metin,
        "tamamlandi": False
    }

    data["gorevler"].append(yeni)
    veriyi_kaydet(data)
    print("Görev eklendi.")


def gorevleri_listele(data, kullanici):
    print("\n--- GÖREVLERİM ---")

    liste = []
    for g in data["gorevler"]:
        if g["sahip"] == kullanici:
            liste.append(g)

    if len(liste) == 0:
        print("Hiç görevin yok.")
        return

    for g in liste:
        if g["tamamlandi"]:
            durum = "Tamamlandı"
        else:
            durum = "Bekliyor"

        print("ID:", g["id"], "|", g["metin"], "|", durum)


def gorev_tamamla(data, kullanici):
    gorevleri_listele(data, kullanici)
    try:
        sec = int(input("Tamamlanacak görev ID: "))
    except:
        print("HATA: Geçersiz ID.")
        return

    for g in data["gorevler"]:
        if g["id"] == sec and g["sahip"] == kullanici:
            g["tamamlandi"] = True
            veriyi_kaydet(data)
            print("Görev tamamlandı.")
            return

    print("Görev bulunamadı.")


def gorev_sil(data, kullanici):
    gorevleri_listele(data, kullanici)
    try:
        sec = int(input("Silinecek görev ID: "))
    except:
        print("HATA: Geçersiz ID.")
        return

    for g in data["gorevler"]:
        if g["id"] == sec and g["sahip"] == kullanici:
            data["gorevler"].remove(g)
            veriyi_kaydet(data)
            print("Görev silindi.")
            return

    print("Görev bulunamadı.")


def todo_menu(data, kullanici):
    while True:
        print("\n=== TO-DO MENÜ ===")
        print("1) Görev ekle")
        print("2) Görevleri listele")
        print("3) Görev tamamla")
        print("4) Görev sil")
        print("5) Geri dön")
        secim = input("Seçim: ")

        if secim == "1":
            gorev_ekle(data, kullanici)
        elif secim == "2":
            gorevleri_listele(data, kullanici)
        elif secim == "3":
            gorev_tamamla(data, kullanici)
        elif secim == "4":
            gorev_sil(data, kullanici)
        elif secim == "5":
            break
        else:
            print("HATA: Yanlış seçim.")

#   TICKET (DESTEK)
def ticket_id_olustur(data):
    # Önce mevcut ID'leri alalım
    mevcut = []
    for t in data["ticketlar"]:
        mevcut.append(t["id"])

    while True:
        yeni = random.randint(1, 999999)

        # Eğer bu ID daha önce kullanılmamışsa geri döndür
        if yeni not in mevcut:
            return yeni

def ticket_olustur(data, kullanici):
    print("\n--- TİCKET OLUŞTUR ---")
    konu = input("Konu: ").strip()
    aciklama = input("Açıklama: ").strip()

    if not konu:
        print("HATA: Konu boş olamaz.")
        return
    if not aciklama:
        print("HATA: Açıklama boş olamaz.")
        return

    yeni = {
        "id": ticket_id_olustur(data),
        "sahip": kullanici,
        "konu": konu,
        "aciklama": aciklama,
        "durum": "acik"
    }

    data["ticketlar"].append(yeni)
    veriyi_kaydet(data)
    print("Ticket oluşturuldu.")


def ticketlarimi_listele(data, kullanici):
    print("\n--- TİCKETLARIM ---")

    liste = []

    for t in data["ticketlar"]:
        if t["sahip"] == kullanici:
            liste.append(t)
            
    if len(liste) == 0:
        print("Ticket yok.")
        return

    for t in liste:
        print("ID:", t["id"], "| Konu:", t["konu"], "| Durum:", t["durum"])
        print("Açıklama:", t["aciklama"])



def ticket_durum_degistir(data, kullanici):
    ticketlarimi_listele(data, kullanici)
    try:
        sec = int(input("Güncellenecek ticket ID: "))
    except:
        print("HATA: Geçersiz ID.")
        return

    for t in data["ticketlar"]:
        if t["id"] == sec and t["sahip"] == kullanici:
            yeni_durum = input("Yeni durum (acik/kapali): ").strip().lower()
            if yeni_durum not in ["acik", "kapali"]:
                print("HATA: Durum sadece 'acik' veya 'kapali' olabilir.")
                return
            t["durum"] = yeni_durum
            veriyi_kaydet(data)
            print("Durum güncellendi.")
            return

    print("Ticket bulunamadı.")


def ticket_menu(data, kullanici):
    while True:
        print("\n=== TİCKET MENÜ ===")
        print("1) Ticket oluştur")
        print("2) Ticketları listele")
        print("3) Durum değiştir")
        print("4) Geri dön")
        secim = input("Seçim: ")

        if secim == "1":
            ticket_olustur(data, kullanici)
        elif secim == "2":
            ticketlarimi_listele(data, kullanici)
        elif secim == "3":
            ticket_durum_degistir(data, kullanici)
        elif secim == "4":
            break
        else:
            print("HATA: Yanlış seçim.")

#   ANA MENÜLER
def kullanici_ana_menu(data, kullanici):
    while True:
        print("\n=== ANA MENÜ ===")
        print("1) To-Do listem")
        print("2) Ticket sistemim")
        print("3) Çıkış yap")
        sec = input("Seçim: ")

        if sec == "1":
            todo_menu(data, kullanici)
        elif sec == "2":
            ticket_menu(data, kullanici)
        elif sec == "3":
            print("Çıkış yapılıyor...")
            time.sleep(1)
            break
        else:
            print("HATA: Yanlış seçim.")


def ana_menu():
    data = veriyi_yukle()

    while True:
        print("\n=== GİRİŞ MENÜSÜ ===")
        print("1) Giriş yap")
        print("2) Kayıt ol")
        print("3) Programı kapat")
        secim = input("Seçim: ")

        if secim == "1":
            kullanici = giris_yap(data)
            if kullanici:
                kullanici_ana_menu(data, kullanici)
        elif secim == "2":
            kayit_ol(data)
        elif secim == "3":
            print("Program kapanıyor...")
            break
        else:
            print("HATA: Yanlış seçim.")


if __name__ == "__main__":
    ana_menu()



