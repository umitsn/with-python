"""
ümit şen 09.2021 bircalismaningunlugu@gmail.com
n! sayısının hangi asal sayı çarpanından kaç tane olduğunu hesaplar.
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
 
def asalCarpanlar(sayi):
    asalListesi = []
    for i in range(sayi+1):
        if asalTest(i):
            asalListesi.append(i)
    return asalListesi

def carpanSayisi(sayi):
    asalListesi = asalCarpanlar(sayi)
    res = {}
    for bolen in asalListesi:
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
        res[f'{bolen}'] = sum(liste)
    return res


sayi = 99
liste = carpanSayisi(sayi)
print(f'{sayi}! sayısı içerisinde : ')
for i in liste:
    print(f'\t{i} \tçarpanından {liste[i]} \ttane')
