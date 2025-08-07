
def findArrays(N):
    print(f"Girilen Sayı : {N}")
    print("Bulunan Dizler :")
    print("-"*50)
    s = 0
    T = 2*N
    for k in range(1,N+1):
        if T % (k+1) == 0:
            x = ((T/(k+1))-k)/2.0
            if x.is_integer() and x>0:
                s +=1
                x = int(x)
                a1 = str(x).rjust(len(str(N)))
                a2 = str(x+k).rjust(len(str(N)))
                ts = str(k+1).rjust(len(str(N)))
                if k==1:
                    print(f"{str(s).zfill(4)} Dizi {a1} ve {a2}        Toplam {ts} Terim")
                else:
                    print(f"{str(s).zfill(4)} Dizi {a1} ve {a2} Arası. Toplam {ts} Terim")


findArrays(2025)
