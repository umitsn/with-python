"""
umit sen - izmir - mayıs 2019 - umitsen.wordpress.com
sayıları adım sayısına göre gruplandırıp bu sayıları her adım için ayrı ayrı oluşturduğu txt dosyasına kaydeder.
"""

gruplar = {}

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
        gruplar.setdefault(n,[]).append(a)

for i in [1,2,3,4,5,6,7]:
    dosya=open("%s.adimda-biten-sayilar.txt"%(i),"w")
    for k in gruplar[i]:
        dosya.write(str(k)+"\n")
    dosya.close()
print("bitti...")

"""
örnek:

1.adimda-biten-sayilar.txt
1036
1063
1137
1173
1247
1274
1306
1317
1357
...
...
...

5.adimda-biten-sayilar.txt
1000
1011
1033
1037
1045
1048
...
...
...
gibi
"""


