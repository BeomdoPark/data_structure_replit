def checkBracket(expr):
    global top, stack, SIZE
    for ch in expr:
        if ch in '(':
            push(ch)
        elif ch in ')':
            out = pop()
            if out == '(':
                pass
            else:
                return False
        else:
            pass
    if top == -1:  #다 끝나고 비었으면
        return True
    else:
        return False


def push(data):
    global top, stack, SIZE
    top += 1  # push할때는 top먼저 증가시키고 해야 됨
    stack[top] = data


def pop():
    global top, stack, SIZE
    temp = stack[top]
    stack[top] = None
    top -= 1
    return temp


if __name__ == '__main__':
    rows = int(input())
    for i in range(rows):
        expr = input()
        SIZE = len(expr)

        stack = [None for _ in range(SIZE)]
        top = -1

        print(checkBracket(expr))
