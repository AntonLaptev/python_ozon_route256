def data_analysis(windows_num, patient_num, appointment_dict, itog):

    for i in range(2, patient_num+2):
        cur = appointment_dict[i]
        next_ = appointment_dict[i+1]
        next1 = appointment_dict[i+2]
        last = appointment_dict[i-1]
        if cur[1] < last[1]:     # если при пробежке вверх убежали дальше сортировки
            print("x")
            break
        if cur[1] == next_[1]:     # если есть 2 равные записи
            if cur[1]-1 > last[1]:  # бежим вниз
                if cur[1]-1 != 0:   # отсекаем 0
                    cur[1] = cur[1]-1
                    itog[cur[0]] = '-'
                    continue
            else:
                if cur[1]-1 != 0:   # отсекаем 0
                    for k in range(i-1, 1, -1):  # бежим вниз до 1 первого значения и сдвигаем
                        l = 0
                        if k == i-1 and itog[appointment_dict[k][0]] != '0':
                            break
                        if appointment_dict[k][1]-1 != appointment_dict[k-1][1] and itog[appointment_dict[k][0]] == '0':
                            for l in range(k, i+1):
                                appointment_dict[l][1] = appointment_dict[l][1]-1
                                itog[appointment_dict[l][0]] = '-'
                            break
                        if itog[appointment_dict[k-1][0]] != '0':
                            break
                    if l != 0:
                        continue
            if cur[1] == next1[1]: # если после действий выше не сдвинули текущую, то ошибка
                print("x")
                break

            if cur[1]+1 != next1[1]:  # бежим вверх, если пробежка вниз не дала результат,
                if cur[1] != windows_num:
                    next_[1] = cur[1]+1
                    itog[next_[0]] = '+'
                    continue
            else:
                if cur[1]+1 != windows_num+1:
                    for k in range(i+2, patient_num+2):

                        l = 0
                        if k == i+2 and appointment_dict[k][1] == appointment_dict[k+1][1]:
                            break
                        if appointment_dict[k][1] == windows_num:
                            break
                        if appointment_dict[k][1]+1 != appointment_dict[k+1][1] and itog[appointment_dict[k][0]] == '0':

                            for l in range(k, i, -1):

                                appointment_dict[l][1] = appointment_dict[l][1]+1
                                itog[appointment_dict[l][0]] = '+'
                            break
                    if l != 0:
                        continue
            print("x")
            break
    else:
        print(''.join(itog))


def input_data_():
    data_number = int(input())
    for _ in range(data_number):
        windows_num1, patient_num1 = map(int, input().split())
        appointment1 = list(map(int, input().split()))
        itog1 = ['0' for _ in range(patient_num1)]
        appointment_dict1 = []
        for i in range(0, patient_num1):
            appointment_dict1.append([i, appointment1[i]])
        appointment_dict1.append([i+1, windows_num1+2])
        appointment_dict1.append([i+2, windows_num1+2])
        appointment_dict1.append([i+3, windows_num1+2])
        appointment_dict1.sort(key=lambda i: i[1])
        if appointment_dict1[0][1] == 1:
            x = 0
        else:
            x = appointment_dict1[0][1]-2
        appointment_dict1.insert(0, [1, x])
        appointment_dict1.insert(0, [0, x])
        data_analysis(windows_num1, patient_num1, appointment_dict1, itog1)


input_data_()
