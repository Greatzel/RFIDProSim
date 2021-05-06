def formatvalue(value):
    if len(value) < 8:
        result = "00" + str(value)
    else:
        result = value
    return result


# def hemming weight(value): need to write hw algo!

def hemmingweight(value):
    count = 0
    for i in str(value):
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


def rotleft2(value, hw):
    # length of string minus hw
    strlength = len(value) - hw
    leftval = value[:-strlength]
    print("leftval: ", leftval)
    rightval = value[hw:]
    print("rightval: ", rightval)
    fres = rightval + leftval
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

    # recursive hash
    # bin1 is the number we will rotate
    # we will rotate bin1 by hw of bin2
    # bin3 is the K value given by user
    # edit: my brain hurt so seed = 4 ALWAYS
    # 16 bit enforced!


def recursivehash(bin1, bin2):
    print("RH type: ", type(bin2))
    newbin1 = str(bin1)
    p1 = newbin1[:4]
    p2 = newbin1[4:8]
    p3 = newbin1[8:12]
    p4 = newbin1[12:16]
    # print("seed: ",  bin2)
    if bin2 == 1:
        i = 0
    else:
        i = bin2 - 1
    # print("i: ", i)
    partitions = [p1, p2, p3, p4]
    # print(partitions)
    count = 0
    newbin = ""
    for part in partitions:
        # count += 1
        # print("count: ", count)
        if count != i:
            partxor = xorbin(part, partitions[i])
            partitions[count] = partxor[4:]
            # print("part in loop: ", part)
        newbin += str(partitions[count])
        count += 1

    # print("new partitions: ", partitions)
    return newbin
