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
