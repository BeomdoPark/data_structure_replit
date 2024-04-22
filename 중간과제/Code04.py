# 4번. 연결 리스트의 팰린드롬 판단
class Node:

    def __init__(self):
        self.data = None
        self.link = None


def is_palindrome(head):
    current = head
    data_list = []
    while current.link != None:
        data_list.append(current.data)
        current = current.link
    return "true" if data_list == data_list[::-1] else "false"


memory = []
head, current, pre = None, None, None
data_array = []

if __name__ == "__main__":
    print("linked_list = 숫자 하나씩 입력, 엔터 두번 입력 시 종료")
    while True:
        user_input = input()
        if not user_input:
            break
        else:
            data = int(user_input.strip())
            node = Node()
            data_array.append(data)
            if head == None:
                head = node
            else:
                current = head
                while current.link:
                    current = current.link
                current.link = node
    print("입력된 데이터\t:", *data_array)
    print(is_palindrome(head))
