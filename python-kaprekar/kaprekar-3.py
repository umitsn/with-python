"""
umit sen - izmir - mayıs 2019 - umitsen.wordpress.com
1000'den 9999'a kadar (tüm rakamları birbirine eşit olmayan) sayılar için bu sayıların  
kaç adımda kaprekar sayısına ulaştığını hesaplar ve ekrana yazdırır.
"""
def kontrol(n):
    sayi = str(n)
    liste = [int(x) for x in sayi]
    if (liste.count(liste[0])==4):
        return False
    else:
        return True
    
def islem(n):
    sayi = str(n)
    liste = [int(x) for x in sayi]
    min2max = sorted(liste)
    max2min = min2max[::-1]

    Smin = int("%s%s%s%s"%(min2max[0],min2max[1],min2max[2],min2max[3]))
    Smax = int("%s%s%s%s"%(max2min[0],max2min[1],max2min[2],max2min[3]))
    fark = Smax-Smin
    if(fark < 1000):
        fark=fark*10
    return fark

for i in range(1000,9999+1):
    if kontrol(i):
        a = i
        durum = True
        n=1

        while durum:
            ns = islem(i)
            if(ns == 6174):
                durum = False
            else:
                i = ns
                n +=1
        print(a,n)
