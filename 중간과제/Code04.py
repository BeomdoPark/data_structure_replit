import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def is_palindrome(head):
    palindrome_str = ""
    current = head
    while current != None:
        palindrome_str += current.data
        current = current.link
    if palindrome_str == palindrome_str[::-1]:
        return True
    else:
        return False


if __name__ == __main__:

    data_array = []

    print("숫자 입력, 엔터 두번 입력 시 종료")

    while True:
        user = sys.stdin.readline()
        if user == "\n":
            break
        else:
            user = user.strip()
            node = Node()
            head = node
            data_array.append(user)
    is_palindrome(data_array)
