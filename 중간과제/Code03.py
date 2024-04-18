# 3번. 두 숫자 인덱스 리턴 문제
nums_list = input("nums_list(공백으로 구분하여 숫자 입력) = ").split()
nums_list = list(map(int, nums_list))
goal = int(input("goal = "))

# nums가 많을 경우 모든 경우의 수가 출력됨
for i in range(len(nums_list)):
    for j in range(i + 1, len(nums_list)):
        if nums_list[i] + nums_list[j] == goal:
            print([i, j])
            # break <-하나의 경우만 출력하려면 추가
