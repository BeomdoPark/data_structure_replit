def addNumber(num1, num2):
    big_num = num1 if num1 >= num2 else num2
    small_num = num2 if num2 <= num1 else num1
    if big_num <= small_num:
        return small_num

    return big_num + addNumber(big_num - 1, small_num)


first = int(input('숫자1->'))
second = int(input('숫자2->'))
print(addNumber(first, second))
