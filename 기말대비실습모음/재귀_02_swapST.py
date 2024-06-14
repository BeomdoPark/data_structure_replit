# 두 문자열이 S와 T가 주어졌을 때, S를 T로 바꿀 수 있는지 확인하세요.
# ▪ 문자열을 바꿀 때는 두 가지 연산만 가능합니다.
# ✓ 문자열 뒤에 A를 추가한다.
# ✓ 문자열 뒤에 B를 추가하고 문자열을 뒤집는다.
# ▪ 첫째 줄에는 S가 입력되고 둘째 줄에는 T가 입력된다.
# ▪ S를 T로 바꿀 수 있으면 1을 출력하고 바꿀 수 없으면 0을 출력하세요

answer = 0


def can_sub(s, t):
    global answer
    if len(s) > len(t):  # 문자열 길이가 s가 크면 불가능
        return answer

    if len(s) <= len(t):
        # 문자열 길이가 같아질 때까지 반복
        s_a = add_a(s)
        s_b = add_b(s)
        can_sub(s_a, t)
        can_sub(s_b, t)
    # 재귀를 len(s) == len(t)일 때까지 반복 후
    # s와 t가 같아지면 answer = 1
    if s == t:
        answer = 1
        return answer
    else:
        return answer


def add_a(s):
    s += "A"
    return s


def add_b(s):
    s += "B"
    s = s[::-1]
    return s


s = input()
t = input()
can_sub(s, t)
print(answer)
