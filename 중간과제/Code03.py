import sys

nums = input("nums_(공백으로 구분하여 숫자 입력) = ").split()
nums = list(map(int, nums))
goal = int(input("goal = "))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == goal:
            print([i, j])
