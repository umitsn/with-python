import random

uList = [chr(i) for i in range(65,91)]  ## A-Z",
lList = [chr(i) for i in range(97,123)] ## a-z",
nList = [chr(i) for i in range(48,58)]  ## 0-9",
sList = [chr(i) for i in [36,37,38,40,41,42,43]] ## $ % & ( ) * +",

def generatePassword(n):
    gList = [uList,lList,nList]
    cList = [random.choice(i) for i in gList]
    durum = True
    while durum:
        if len(cList) < n:
            k = random.choice(gList)
            cList.append(random.choice(k))
    else:
        durum = False  
    return ''.join(random.sample(cList,len(cList)))

for i in range(1,6):
    p = generatePassword(18)
    print(f"password {str(i).zfill(2)} : {p} : {len(p)}")
