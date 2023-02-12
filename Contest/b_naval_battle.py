from collections import Counter
kl_nab = int(input())
for q in range(kl_nab):
    x = list(map(int, input().split()))
    t = dict(Counter(x))
    print(t)
    if t.get(4) == 1 and t.get(3) == 2 and t.get(2) == 3 and t.get(1) == 4:
        print('YES')
    else:
        print('NO')
