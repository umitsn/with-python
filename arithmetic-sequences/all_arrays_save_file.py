
sayi = 10
print(f"Girilen Sayı : {sayi}")
print("Bulunan diziler")
print("-"*50)
def findArray(sayi):
    s=0
    N = 2*sayi
    for k in range(1,sayi+1):
        if N % (k+1) == 0:
            x = ((N/(k+1))-k)/2.0
            if x.is_integer() and x>0:
                s += 1
    return [sayi,s]

for i in range(1,999998+1):
    sonuc = findArray(i)
    with open(f"{str(sonuc[1]).zfill(4)}.txt","a") as f:
        f.write(f"{sonuc[0]}\n")
print("Bitti...")