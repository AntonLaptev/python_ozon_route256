kl = int(input().strip())
for j in range(kl):
    kl_t = int(input().strip())
    znaki_m = []
    znaki = set()
    for n in range(kl_t):
        znaki_m += [input()]
    otvet = len(znaki_m)
    for n in znaki_m:
        s = ''
        r = n[0]
        kl = 0
        for c in range(len(n)):
            if n[c] != r:
                kl = 1
                s += n[c]
            else:
                kl += 1
                if kl == 2:
                    s += n[c]
            r = n[c]
        znaki.add(s)
    print(len(znaki))
