nab=int(input())                                       #nab-количество наборов
for g in range(nab):
    input()
    lin,col=list(map(int, input().split()))              #lin-строки, col-столбцы
    tab = []                                             #tab-таблица
    for i in range(lin):
        tab.append([int(j) for j in input().split()])
    kl=int(input())                                      #kl-количество кликов
    num_col=list(map(int, input().split()))              #num_col-номера столбцов
    for j in range(kl):
        n_col=num_col[j]-1
        tab.sort(key=lambda i: i[n_col])
    for i in range(lin):
        for j in range(col):
            print(tab[i][j],end=' ')
        print()
    print()
