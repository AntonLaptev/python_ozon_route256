from collections import Counter
import operator
x=[[0]*8 for i in range(8)]
for i in range(8):
    st=input()
    for j in range(8):
        if st[j]=='*': x[i][j]=1
kl_f=int(input())
kl_st_f=int(input())
koord_f=[]
for i in range(kl_st_f):
    st_f=input()
    for j in range(len(st_f)):
        if st_f[j]=='*':
            koord_f.append([i,j])
sl_v={}
for i in range(8):
    for j in range(8):
        f=''
        for q in range(len(koord_f)):
            if 0<=i+koord_f[q][0]<=7 and  0<=j+koord_f[q][1]<=7:
                if x[i+koord_f[q][0]][j+koord_f[q][1]]==1:
                    f=''
                    break
                else:
                    f+=str(x[i+koord_f[q][0]][j+koord_f[q][1]])
        else:
            if len(f)==len(koord_f):
                for q in range(len(koord_f)):
                    x[i+koord_f[q][0]][j+koord_f[q][1]]=1
                v_stroka=0
                v_stolb=0
                v=0
                sl_v[str(i)+str(j)]=0
                for p in range(8):
                    if (0 not in x[p]) or (x[0][p]!=0 and x[1][p]!=0 and x[2][p]!=0 and x[3][p]!=0 and x[4][p]!=0 and x[5][p]!=0 and x[6][p]!=0 and x[7][p]!=0):
                        if 0 not in x[p]:
                            v_stroka+=1
                            v+=8
                        if x[0][p]!=0 and x[1][p]!=0 and x[2][p]!=0 and x[3][p]!=0 and x[4][p]!=0 and x[5][p]!=0 and x[6][p]!=0 and x[7][p]!=0:
                            v_stolb+=1
                            v+=8
                        v=v-(v_stroka*v_stolb)
                        sl_v[str(i)+str(j)]=v
                for q in range(len(koord_f)):
                    x[i+koord_f[q][0]][j+koord_f[q][1]]=0
if len(sl_v)==0:otvet=-1
else:
    k_i=int(max(sl_v.items(), key=operator.itemgetter(1))[0][0])
    k_j=int(max(sl_v.items(), key=operator.itemgetter(1))[0][1])
    for q in range(len(koord_f)):
        x[k_i+koord_f[q][0]][k_j+koord_f[q][1]]=1
    for p in range(8):
        if 0 not in x[p]:
            x[p]=[2,2,2,2,2,2,2,2]
    for p in range(8):
        if x[0][p]!=0 and x[1][p]!=0 and x[2][p]!=0 and x[3][p]!=0 and x[4][p]!=0 and x[5][p]!=0 and x[6][p]!=0 and x[7][p]!=0:
            x[0][p]=2
            x[1][p]=2
            x[2][p]=2
            x[3][p]=2
            x[4][p]=2
            x[5][p]=2
            x[6][p]=2
            x[7][p]=2
    otvet=0
    for l in range(8):
        for k in range(8):
            if x[l][k]==1:otvet+=1
print(otvet)