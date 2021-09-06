"""
ümit şen 09.2021 bircalismaningunlugu@gmail.com
n! sayısının herhangi bir tamsayı böleninin sayısını hesaplar. Bolen sayı 5 seçilirse n! sayısının sonunda kaç sıfır bulunur.
"""
sayi = 51
bolen = 3

durum = True
liste = []
tmp = sayi
while durum:
    bolum = tmp // bolen
    if bolum >= bolen:
        liste.append(bolum)
        tmp = bolum
    else:
        liste.append(bolum)
        durum = False

print(f'Girilen sayı : {sayi} \nÇarpan : {bolen}')       
print(f'Bölüm Listesi : {liste} \n{sayi}! sayısı içinde toplam {sum(liste)} tane {bolen} çarpanı vardır.')
