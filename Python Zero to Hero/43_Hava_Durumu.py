import requests
import json


while True:
    
    sehir =input("Lütfen Şehir Giriniz")
    
    apikey = "87ab45eeebfb0d465eeb947495ebc5e9"

    adres = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(sehir,apikey)

    baglan = requests.get(adres)

    sorgu = baglan.json()

    havadurumu = sorgu["weather"][0]["description"]
    havasicaklik = sorgu["main"]["temp"]
    hissedilensicaklik = sorgu["main"]["feels_like"]
    minsicaklik = sorgu["main"]["temp_min"]
    maxsicaklik = sorgu["main"]["temp_max"]
    basinc = sorgu["main"]["pressure"]
    nem = sorgu["main"]["humidity"]

    print("{} İçin Hava Durumu Bilgileri...\n\nSıcaklık: {} \nDurum: {}\nHissedilen Sıcaklık:{}\nEn Düşük Sıcaklık:\nEn Yüksek Sıcaklık: {}\nBasınç: {}\nNem: {}".format(sehir.capitalize(),havasicaklik,havadurumu.title(),hissedilensicaklik,minsicaklik,maxsicaklik,basinc,nem))