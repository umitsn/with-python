"""
umit sen - izmir - mayıs 2019 - umitsen.wordpress.com
bir sayı için kaprekar sabitini hesaplamadaki tüm tüm işlem adımlarılarını ekrana yazdırır.
"""
def kontrol(n):
    sayi = str(n)
    liste = [int(x) for x in sayi]
    if (liste.count(liste[0])==4):
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
            if(ns == 6174):
                durum = False
            else:
                k = ns
                n +=1      
goster(3765)

"""
Örneğin ekran çıktısı : 
>>> 
====== RESTART: \umitsen\Desktop\python-kaprekar\kaprekar-2.py ======
1.Adım = Sayi : 3765 Max : 7653 Min : 3567 Fark : 4086
2.Adım = Sayi : 4086 Max : 8640 Min : 468  Fark : 8172
3.Adım = Sayi : 8172 Max : 8721 Min : 1278 Fark : 7443
4.Adım = Sayi : 7443 Max : 7443 Min : 3447 Fark : 3996
5.Adım = Sayi : 3996 Max : 9963 Min : 3699 Fark : 6264
6.Adım = Sayi : 6264 Max : 6642 Min : 2466 Fark : 4176
7.Adım = Sayi : 4176 Max : 7641 Min : 1467 Fark : 6174
>>> 
"""
