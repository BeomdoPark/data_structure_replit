# 6번. 홀짝 연결 리스트 문제
class Node:
    def __init__(self):
        self.data = None
        self.link = None


# head노드 입력시 2개씩 묶어서 스왑. 반환값 없음
def swap_pairs(start):
    current = start
    while current != None:  # 뒤에 노드가 존재할 때,
        temp_data = current.data  # 현재노드 데이터 임시저장
        current.data = current.link.data  # 다음 노드 데이터를 현재 노드 데이터로 변경
        current.link.data = temp_data  # 임시저장한 데이터를 다음 노드 데이터로 변경
        current = (
            current.link.link if current.link.link.link else None
        )  # 두칸 점프 , 조건문 넣으면 홀수개 입력도 스왑 가능함


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

    # 두 번째 이후 노드를 생성
    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    swap_pairs(head)  # 스왑
    print("스왑 후\t\t: ", end="")
    printNodes(head)  # 출력
