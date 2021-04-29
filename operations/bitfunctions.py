def formatvalue(value):
    if len(value) < 8:
        result = "00" + str(value)
    else:
        result = value
    return result


# def hemming weight(value): need to write hw algo!

def hemmingweight(value):
    num = int(value, 2)
    n = str(bin(num))
    count = 0
    for i in n:
        if i == "1":
            count += 1
    return count


def rotleft(value, hw):
    print(value)
    dec = int(str(value), 2)
    print(dec)
    rot = (dec << hw) | (dec >> (16 - hw))
    print(rot)
    res = bin(rot).replace("0b", "")
    print(res)
    result = res[2:]
    return result
