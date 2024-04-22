def push(data):
    global SIZE, stack, top
    if (top >= SIZE - 1):
        print("스택이 꽉 찼습니다.")
    else:
        top += 1
        stack[top] = data
        print(data, end=" -> ")


def pop():
    global SIZE, stack, top
    if (top == -1):
        print("스택이 비었습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        print(data, end=" -> ")
        return data


SIZE = 6
stack = [None for _ in range(SIZE)]
top = -1

print("과자집에 가는길", end=" : ")
push("주황")
push("초록")
push("파랑")
push("보라")
push("빨강")
push("노랑")
print("과자집")

print("우리집에 오는길", end=" : ")
pop()
pop()
pop()
pop()
pop()
pop()
print("우리집")
