a=[]
kl_d=int(input())
for i in range(kl_d):
    kl_t=int(input())
    a=list(map(int, input().split()))
    a.sort()
    sh=0
    zn=a[0]
    j=0
    su=0
    while j<kl_t:
        if zn==a[j]:
            sh+=1
        else:
            su+=(sh-sh//3)*zn
            sh=1
        zn=a[j]
        j+=1
    su+=(sh-sh//3)*zn
    print(su)