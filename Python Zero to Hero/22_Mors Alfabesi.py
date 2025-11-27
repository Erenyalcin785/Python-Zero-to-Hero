MorsKod ={ "A" : ".-",
          "B" : "-...",
          "C" : "-.-.",
          "D" : "-..",
          "E" : ".",
          "F" : "..-.",
          "G" : "--.",
          "H" : "....",
          "I" : "..",
          "K" : "-.-",
          "L" : ".-..",
          "M" : "--",
          "N" : "-.",
          "O" : "---",
          "P" : ".--.",
          "R" : ".-.",
          "S" : "...",
          "T" : "-",
          "U" : "..-",
          "V" : "...-",
          "W" : ".--",
          "X" : "-..-",
          "Y" :"-.--",
          "Z" :"--..",
          " " : "/"

}

Cümle = input("Lütfen Mors Alfabesine Çevireceğiniz Cümleyi Giriniz:")
Cümle = Cümle.upper()
for i in range(0,len(Cümle)):
    mors_indeks = Cümle[i]
    sonuc = MorsKod.get(mors_indeks)
    print(Cümle[i],chr(26),sonuc)


# cumle=input("Mors koduna çevireceğiniz cümleyi giriniz: ").upper()
# mors_cumle=""
# for i in range(0,len(cumle)):
#     cumle_indeks=cumle[i]
#     mors_kodu=MorsKod.get(cumle_indeks)
#     print(cumle[i], chr(26),mors_kodu)
#     mors_cumle+=mors_kodu + " "
# print("mors cümlesi: ", mors_cumle)