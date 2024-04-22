def push(data):
    global SIZE, stack, top
    if (top >= SIZE - 1):
        print("스택이 꽉 찼습니다.")
    else:
        top += 1
        stack[top] = data


def pop():
    global SIZE, stack, top
    if (top == -1):
        print("스택이 비었습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data


SIZE = 5
stack = ["커피", "None", "None", "None", "None"]
top = 0

print(stack)
retData = pop()
print("추출한 데이터 --> ", retData)
print(stack)
retData = pop()
