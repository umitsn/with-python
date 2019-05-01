"""
umit sen - izmir - mayıs 2019 - umitsen.wordpress.com
bir sayı için kaprekar sabitini hesaplamadaki tüm tüm adımlarıları ayrıntıları ile ekrana yazdırır.
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
    txt = "%s.Adım = Sayi : %s Max : %s Min : %s Fark : %s"%(m,sayi,Smax,Smin,fark)
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
        print(a,n)
          
goster(7175)

