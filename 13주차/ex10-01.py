def bin(decimal):
    binary_string = ""
    if decimal == 0:
        return ""
    binary_string = str(decimal % 2)
    decimal = decimal // 2
    return bin(decimal) + binary_string


def octal(decimal):
    octal_string = ""
    if decimal == 0:
        return ""
    octal_string = str(decimal % 8)
    decimal = decimal // 8
    return octal(decimal) + octal_string


def hexa(decimal):
    hexa_string = ""
    if decimal == 0:
        return ""

    hexa_string = str(decimal %
                      16) if decimal % 16 < 10 else chr(decimal % 16 + 55)
    decimal = decimal // 16
    return hexa(decimal) + hexa_string


user = int(input("10진수 입력 -> "))

print(" 2진수 :\t" + bin(user))
print(" 8진수 :\t" + octal(user))
print(" 16진수:\t" + hexa(user))
