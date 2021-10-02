#!/usr/bin/env python
"""
umit sen - umitsen.wordpress.com
"""
def asalTest(n):
    durum = False 
    if n<2:
        durum = False
    if n==2 or n==3:
        durum = True
    kok = n**0.5
    for i in range(2,int(kok)+1):
        if n % i ==0 :
            durum = False
            break
        else:
            durum = True
    return durum
 
def hesapla(sayi):
    asalListesi = []
    for i in range(sayi+1):
        if asalTest(i):
            if sayi % i ==0:
                asalListesi.append(i)
    # bolunen = bolum * bolen
    bolunen = sayi
    i=0
    asallar = []
    bolunenler = [bolunen]
    while i<len(asalListesi):
        bolen = asalListesi[i]
        bolum = bolunen // bolen
        if bolum % bolen == 0:
            bolen = asalListesi[i]
            bolunen = bolum
            asallar.append(bolen)
        else:
            bolunen = bolum
            i +=1
            asallar.append(bolen)
        bolunenler.append(bolunen)
    return {"asallar":asallar,"bolunenler":bolunenler}

sayi = 36036
print(f'Girilen Sayı : {sayi}')
sonuc = hesapla(sayi)
for i in range(len(sonuc["asallar"])):
    fillLen = len(str(sayi))
    print(f'{str(sonuc["bolunenler"][i]).rjust(fillLen)} | {sonuc["asallar"][i]}')
print(f'{str(sonuc["bolunenler"][-1]).rjust(fillLen)} |')