import re


# if valid return true
pattern = re.compile(r"^[0-1]{16}$")
patternsasi = re.compile(r"^[0-1]{8,16}$")
patterlmap = re.compile(r"^[0-1]{8,16}$")


def is_valid_rcia(f1, f2, f3, f4, f5, f6):
    if re.fullmatch(pattern, f1) and re.fullmatch(pattern, f2) and re.fullmatch(pattern, f3) \
            and re.fullmatch(pattern, f4) and re.fullmatch(pattern, f5) and re.fullmatch(pattern, f6):
        return True
    else:
        return False


def is_valid_lmap(f1, f2, f3, f4, f5, f6, f7, f8):
    if re.fullmatch(patterlmap, f1) and re.fullmatch(patterlmap, f2) and re.fullmatch(patterlmap, f3) \
            and re.fullmatch(patterlmap, f4) and re.fullmatch(patterlmap, f5) and re.fullmatch(patterlmap, f6) \
            and re.fullmatch(patterlmap, f7) and re.fullmatch(patterlmap, f8):
        return True
    else:
        return False


def is_valid_sasi(f1, f2, f3, f4, f5, f6):
    if re.fullmatch(patternsasi, f1) and re.fullmatch(patternsasi, f2) and re.fullmatch(patternsasi, f3) \
            and re.fullmatch(patternsasi, f4) and re.fullmatch(patternsasi, f5) and re.fullmatch(patternsasi, f6):
        return True
    else:
        return False
