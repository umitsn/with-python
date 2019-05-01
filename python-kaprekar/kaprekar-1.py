"""
umit sen - izmir - mayıs 2019 - umitsen.wordpress.com
Girilen herhangi bir dört basamaklı sayının kaprekar sabiti ile sonuçlandığını gösterir.

"""

def kontrol(n):
    sayi = str(n)
    liste = [int(x) for x in sayi]
    if (liste.count(liste[0])==4):
        print("Girilen dört rakam birbirine eşit olamaz.")
        return False
    else:
        return True
    
def islem(n,m):
    sayi = str(n)
    liste = [int(x) for x in sayi]
    min2max = sorted(liste)
    max2min = min2max[::-1]

    Smin = int("%s%s%s%s"%(min2max[0],min2max[1],min2max[2],min2max[3]))
    Smax = int("%s%s%s%s"%(max2min[0],max2min[1],max2min[2],max2min[3]))
    fark = Smax-Smin
    if(fark < 1000):
        fark=fark*10
    txt = "%s.Adım = Sayi : %s Max : %s Min : %s Fark : %s"%(m,sayi,Smax,str(Smin).ljust(4),fark)
    print(txt)
    return fark

def goster(k):
    if kontrol(k):
        a = k
        durum = True
        n=1
        while durum:
            ns = islem(k,n)
            if(ns == k):
                durum = False
            else:
                k = ns
                n +=1
          
goster(3765)

"""
Ekran çıktısı : 
>>>
====== RESTART: \umitsen\Desktop\python-kaprekar\kaprekar-1.py ======
1.Adım = Sayi : 3765 Max : 7653 Min : 3567 Fark : 4086
2.Adım = Sayi : 4086 Max : 8640 Min : 468  Fark : 8172
3.Adım = Sayi : 8172 Max : 8721 Min : 1278 Fark : 7443
4.Adım = Sayi : 7443 Max : 7443 Min : 3447 Fark : 3996
5.Adım = Sayi : 3996 Max : 9963 Min : 3699 Fark : 6264
6.Adım = Sayi : 6264 Max : 6642 Min : 2466 Fark : 4176
7.Adım = Sayi : 4176 Max : 7641 Min : 1467 Fark : 6174
8.Adım = Sayi : 6174 Max : 7641 Min : 1467 Fark : 6174
>>>
NOT : kaprekar sabitine 7. adımda ulaştı fakar bir öncekiyle eşit olduğunu anlması için bir adım daha ilerletti ve 
sonucun eşitlendiğini görünce 9. adıma geçmeden kod çalışmasını durdurdu. Yani işlem 7 adım sürdü...
"""
