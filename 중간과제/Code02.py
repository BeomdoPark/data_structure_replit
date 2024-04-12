import sys

string = list(sys.stdin.readline().strip())


def reverse_string(string):
    string.reverse()
    print(string)


reverse_string(string)
