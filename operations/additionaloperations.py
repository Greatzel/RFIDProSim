def formatvalue(value):
    if len(value) < 8:
        result = "00" + str(value)
    else:
        result = value
    return result
