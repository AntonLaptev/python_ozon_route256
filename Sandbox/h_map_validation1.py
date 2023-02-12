kl_nab=int(input())
for q in range(kl_nab):
    y,x=list(map(int, input().split()))
    sl={}
    s=''
    spis=[[0 for j in range(x)] for i in range(y)]
    for i in range(y):
        s=input()
        for j in range(len(s)):
            if s[j]!='.':
                if s[j] in sl:sl[s[j]]+=1
                else: sl[s[j]]=1
        for q in range(x):
            spis[i][q]=s[q]
    for key in sl:
        visited = []
        queue=[]
        colour=key
        f=False
        for i in range(y):
            if not f:
                for j in range(x):
                    if spis[i][j]!='.' and spis[i][j]==colour:
                        f=True
                        visited.append([i,j])
                        if 0<=j-2<=x-1 and spis[i][j]==spis[i][j-2]:
                            queue.append([i,(j-2)])
                        if 0<=j+2<=x-1 and spis[i][j]==spis[i][j+2]:
                            queue.append([i,(j+2)])
                        if 0<=i-1<=y-1 and 0<=j-1<=x-1 and spis[i][j]==spis[i-1][j-1]:
                            queue.append([(i-1),(j-1)])
                        if 0<=i-1<=y-1 and 0<=j+1<=x-1 and spis[i][j]==spis[i-1][j+1]:
                            queue.append([(i-1),(j+1)])
                        if 0<=j-1<=x-1 and 0<=i+1<=y-1 and spis[i][j]==spis[i+1][j-1]:
                            queue.append([(i+1),(j-1)])
                        if 0<=i+1<=y-1 and 0<=j+1<=x-1 and spis[i][j]==spis[i+1][j+1]:
                            queue.append([(i+1),(j+1)])
                    if f:break
        while len(queue)!=0:
            if queue[0] not in visited: visited.append(queue[0])
            i=int(queue[0][0])
            j=int(queue[0][1])
            if 0<=j-2<=x-1 and spis[i][j]==spis[i][j-2]:
                if [i,(j-2)] not in queue and [i,(j-2)] not in visited:
                    queue.append([i,(j-2)])
            if 0<=j+2<=x-1 and spis[i][j]==spis[i][j+2]:
                if [i,(j+2)] not in queue and [i,(j+2)] not in visited:
                    queue.append([i,(j+2)])
            if 0<=i-1<=y-1 and 0<=j-1<=x-1 and spis[i][j]==spis[i-1][j-1]:
                if [(i-1),(j-1)] not in queue and [(i-1),(j-1)] not in visited:
                    queue.append([(i-1),(j-1)])
            if 0<=i-1<=y-1 and 0<=j+1<=x-1 and spis[i][j]==spis[i-1][j+1]:
                if [(i-1),(j+1)] not in queue and [(i-1),(j+1)] not in visited:
                    queue.append([(i-1),(j+1)])
            if 0<=j-1<=x-1 and 0<=i+1<=y-1 and spis[i][j]==spis[i+1][j-1]:
                if [(i+1),(j-1)] not in queue and [(i+1),(j-1)] not in visited:
                    queue.append([(i+1),(j-1)])
            if 0<=i+1<=y-1 and 0<=j+1<=x-1 and spis[i][j]==spis[i+1][j+1]:
                if [(i+1),(j+1)] not in queue and [(i+1),(j+1)] not in visited:
                    queue.append([(i+1),(j+1)])
            del queue[0]
        if len(visited)==sl[colour]:
            otvet='YES'
        else:
            otvet='NO'
            break
    print (otvet)