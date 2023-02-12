k_p,k_d=list(map(int, input().split()))
sl={}
for i in range(k_p):
    sl[i+1]=[]
for i in range(k_d):
    kl,zn=list(map(int, input().split()))
    sl[kl].append(zn)
    sl[zn].append(kl)
for k,v in sl.items():
    r=[]
    for i in range(len(v)):
        r+=sl[v[i]]
    rr={0:0}
    for i in range(len(r)):
        if r[i]!=k and  r[i] not in v:
            if r[i] not in rr:
                rr[r[i]]=1
            else: rr[r[i]]+=1
    max_val =max(rr.values())
    rek=sorted(rr.items())
    for i in range(len(rek)):
        if rek[i][1]==max_val:print(rek[i][0],end=' ')
    print('')