from collections import Counter
import operator
kl=int(input())
for q in range(kl):
    kl_p=int(input())

    #a=list(map(str, input().split()))
    a=[]
    sh=1
    for i in input().split():
        if sh==1:
            a.append(i)
        else:
            if z!=i: a.append(i)
        z=i
        sh+=1
    #print(a)

    a_count = dict(Counter(a))
    #print(a_count)
    x = max(a_count.items(), key=operator.itemgetter(1))
    #print(x[1])
    if x[1]!=1:print('NO')
    else: print('YES')