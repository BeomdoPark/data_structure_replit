# 6번. 홀짝 연결 리스트 문제
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start  # head로 초기화
    if current == None:
        return  # current가 노드 끝에 도달시 리턴

    # 첫 노드 출력
    print(current.data, end=" ")

    # 두 번째 이후 노드 출력
    while current.link != None:
        current = current.link  # current를 다음 노드로 이동
        print(current.data, end=" ")


# 전역 변수 생성
memory = []
head, current, pre = None, None, None
data_array = []


if __name__ == "__main__":
    print("linked_list = 숫자 하나씩 입력, 엔터 두번 입력 시 종료")
    while True:
        user_input = input()
        if not user_input:
            break
        else:  # 숫자 데이터 data_array에 저장
            data_array.append(int(user_input.strip()))
    print("입력된 데이터\t:", *data_array)

    # 첫 노드 생성
    node = Node()
    node.data = data_array[0]
    head = node
    memory.append(node)

    # 두 번째 이후 홀수 번째 노드 생성
    for data in data_array[2::2]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

        # 위의 for문 탈출 시의 마지막 node는
        # 아래 for문 동작 시,pre와 자동으로 이어짐
        # (node의 변수 Scope생각해보기)

    # 두 번째 이후 짝수 번째 노드 생성
    for data in data_array[1::2]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)  # 출력
