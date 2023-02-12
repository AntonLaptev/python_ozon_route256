def check_plate(plate):
    if len(plate) == 5:
        if plate[0].isalpha() and plate[1].isdigit() and plate[2].isdigit() and plate[3].isalpha() and plate[4].isalpha():
            return True
    elif len(plate) == 4:
        if plate[0].isalpha() and plate[1].isdigit() and plate[2].isalpha() and plate[3].isalpha():
            return True
    return False


def divide_plates(s):
    res = []
    i = 0
    if i + 5 <= len(s):
        plate = s[i:i+5]
        if check_plate(plate):
            res.append(plate)
            i += 5
    else:
        if i + 4 <= len(s):
            plate = s[i:i+4]
            if check_plate(plate):
                res.append(plate)
                i += 4
    while i < len(s):
        if i + 5 <= len(s):
            plate = s[i:i+5]
            if check_plate(plate):
                res.append(plate)
                i += 5
                continue
        if i + 4 <= len(s):
            plate = s[i:i+4]

            if check_plate(plate):
                res.append(plate)
                i += 4
                continue
        return []
    return res


def process_data(data):
    s = data.strip()
    plates = divide_plates(s)
    if not plates:
        return '-'
    return ' '.join(plates)


def main():
    t = int(input().strip())
    for _ in range(t):
        data = input().strip()
        res = process_data(data)
        print(res)


if __name__ == '__main__':
    main()
