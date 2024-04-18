# 2번. 문자열 역순 출력 문제
import sys

string = list(sys.stdin.readline().strip())


def reverse_string(string):
    string.reverse()


reverse_string(string)
print(string)
