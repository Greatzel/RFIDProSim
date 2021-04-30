def formatvalue(value):
    if len(value) < 8:
        result = "00" + str(value)
    else:
        result = value
    return result


# def hemming weight(value): need to write hw algo!

def hemmingweight(value):
    count = 0
    for i in value:
        if i == "1":
            count += 1
    return count


def rotleft(value, hw):
    # length of string minus hw
    remain = abs(len(str(value)) - hw)
    # convert string to int
    num = int(str(value), 2)
    # get left rotate value
    rotl = (num << hw)
    # get right rotate value
    rotr = (num >> remain)
    # binaryfy rotl and rotr
    rotlbin = bin(rotl).replace("0b", "")
    rotrbin = bin(rotr).replace("0b", "")
    # remove excess bits from rotlbin
    finalrotl = rotlbin[hw:-hw]
    # concatenate finalrotl and rotrbin
    res = int(str(finalrotl) + str(rotrbin))
    # pad 0s to res
    fres = format(res, '008')
    return fres


def xorbin(bin1, bin2):
    value = int(bin1, 2) ^ int(bin2, 2)
    res = format(value, '008b')
    return res


def andbin(bin1, bin2):
    value = int(bin1, 2) & int(bin2, 2)
    res = format(value, '008b')
    return res


def orbin(bin1, bin2):
    value = int(bin1, 2) | int(bin2, 2)
    res = format(value, '008b')
    return res
