def secure_compare(str1, str2):
    if len(str1) != len(str2):
        return False
    result = 0
    for x, y in zip(str1, str2):
        result |= ord(x) ^ ord(y)
    return result == 0