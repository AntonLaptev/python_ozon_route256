kl_nab=int(input())
for q in range(kl_nab):
    kl_otr=int(input())
    otvet='YES'
    x=[]
    for j in range(kl_otr):
        d=input()
        if otvet=='YES':
            x.append(d)
            d1=d[0:8]
            d2=d[9:17]
            #часы, минуты и секунды заданы корректно
            if int(d1[0:2])>23:
                otvet='NO'
            elif int(d1[3:5])>59:
                otvet='NO'
            elif int(d1[6:8])>59:
                otvet='NO'
            elif int(d2[0:2])>23:
                otvet='NO'
            elif int(d2[3:5])>59:
                otvet='NO'
            elif int(d2[6:8])>59:
                otvet='NO'
            #левая граница отрезка находится не позже его правой границы (но границы могут быть равны);
            elif d1>d2:
                otvet='NO'
        #никакая пара отрезков не пересекается (даже в граничных моментах времени)
    if otvet=='YES':
        x.sort()
        zn1=x[0]
        zn_k=zn1[9:17]
        for j in range(1,kl_otr):
            zn2=x[j]
            zn_n=zn2[0:8]
            if zn_k>=zn_n:
                otvet='NO'
            zn_k=zn2[9:17]
    print(otvet)