z=[]
x=int(input())
for i in range(x):
    a,b=input().split()
    z.append(int(a)+int(b))
for i in range(len(z)):
    print(z[i])