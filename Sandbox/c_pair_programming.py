kl=int(input())
for q in range(kl):
    kl_p=int(input())
    a=list(map(int, input().split()))
    zn=0
    ni=0
    nj=0
    f=0
    for i in range(kl_p):
        f=1
        if a[i]!=0:
            zn=a[i]
            ni=i
            for j in range(i+1,kl_p):
                if a[j]!=0:
                    if f==1:
                        f=0
                        r=abs(zn-a[j])
                        nj=j
                    else:
                        if r>abs(zn-a[j]):
                            r=abs(zn-a[j])
                            nj=j
            a[ni]=0
            a[nj]=0
            print(ni+1,nj+1)
    print()