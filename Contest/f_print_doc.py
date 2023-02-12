t = int(input().strip())
# обработка очереди печати, флаг на наличие в очереди последней стр. очередь в int  и сортировка
for i in range(t):
    kol_print_ = int(input().strip())
    already_print__ = input().split(',')
    len_already_print_ = len(already_print__)
    already_print_ = []
    flag = 0
    for b in range(len_already_print_):
        x = already_print__[b]
        if x.isdigit():
            if int(x) == kol_print_:
                flag = 1
            x = [int(x), int(x)]
            if x not in already_print_:
                already_print_.append(x)
        else:
            y = x.split('-')
            y = [int(y[0]), int(y[1])]
            if y[1] == kol_print_:
                flag = 1
            if y not in already_print_:
                already_print_.append(y)
    already_print_.sort(key=lambda i: i[0])
    len_already_print = len(already_print_)
    itog = []  # сюда ответ кладем
    j = 1        # номер проверяемой страницы
    # проверка страниц очереди печати, если страница не входит, то в итог ее, плюс сразу диапазон делаем
    for k in range(len_already_print):
        list_ = already_print_[k]
        if list_[0] != list_[1]:  # проверяем диапазон страниц
            first = list_[0]
            last = list_[1]
            if last < j:
                continue
            if last == j:
                j += 1
                continue
            if first == j:
                j = last+1
            elif first > j:
                if first-j == 1:
                    itog.append(str(j))
                else:
                    mass1 = str(j)+'-'+str(first-1)
                    itog.append(mass1)
                j = last+1
            if first < j < last:
                j = last+1
        else:                       # проверяем одну страницу
            list_ = list_[0]
            last = int(list_)
            if last < j:
                continue
            if last == j:
                j += 1
            elif last > j and last-j > 1:
                mass = str(j)+'-'+str(last-1)
                itog.append(mass)
                j = last+1
            elif last > j and last-j == 1:
                itog.append(str(j))
                j += 2
    if j >= kol_print_:
        if flag == 0:
            itog.append(str(kol_print_))
    elif kol_print_-j == 0:
        itog.append(str(kol_print_))
    if kol_print_-j >= 1:
        mass = str(j)+'-'+str(kol_print_)
        itog.append(mass)
    itog = ','.join(itog)
    print(itog)