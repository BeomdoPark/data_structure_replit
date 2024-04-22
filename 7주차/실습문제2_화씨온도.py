def days_to_warmer_weather(F_list):
    idx = 1
    result = [0 for _ in range(SIZE)]

    for i in range(len(F_list)):
        while i + idx < SIZE:
            if F_list[i] < F_list[i + idx]:
                result[i] = idx
                idx = 1
                break
            else:
                idx += 1
    return result


if __name__ == '__main__':
    F = list(map(int, input("T = [ ] : 공백으로 구분하여 리스트 원소 입력\n").split()))
    SIZE = len(F)
    print(days_to_warmer_weather(F))
