def push(data):
    global SIZE, stack, top
    if (top >= SIZE - 1):
        print("스택이 꽉 찼습니다.")
    else:
        top += 1
        stack[top] = data
        print(data, end="")


def pop():
    global SIZE, stack, top
    if (top == -1):
        print("스택이 비었습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        print(data, end="")
        return data


with open("7주차/진달래꽃.txt", "r") as f:
    string = ""
    while True:
        line = f.readline()
        if not line: break
        string += line
    SIZE = len(string)
    stack = [None for _ in range(SIZE)]
    top = -1
    print("------       원본     ------")
    for s in string:
        push(s)
    print("\n------거꾸로 처리된 결과------")
    for _ in range(SIZE):
        pop()
    print()