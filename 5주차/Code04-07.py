#단순 연결 리스트 생성
# + 노드 삭제 함수 추가


#클래스 선언#
class Node():

  def __init__(self):
    self.data = None
    self.link = None


# head를 통해 Nodes를 출력하는 함수
def printNodes(start):
  current = start  # head로 초기화
  if current == None:
    return  #current가 노드 끝에 도달시 리턴

  #첫 노드 출력
  print(current.data, end=' ')

  #두 번째 이후 노드 출력
  while current.link != None:
    current = current.link  #current를 다음 노드로 이동
    print(current.data, end=' ')
  print()


def deleteNode(deleteData):
  global memory, head, current, pre

  if head.data == deleteData:  # 첫 번째 노드 삭제
    current = head
    head = head.link
    del (current)
    return

  current = head  # 첫 번째  외 노드 삭제
  while current.link != None:
    pre = current
    current = current.link
    if current.data == deleteData:
      pre.link = current.link
      del (current)
      return


# 전역 변수 생성
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인 코드
if __name__ == "__main__":
  #첫 노드 생성
  node = Node()
  node.data = dataArray[0]
  head = node
  memory.append(node)

  #두 번째 이후 노드를 생성
  for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

  printNodes(head)

  deleteNode("다현")
  printNodes(head)

  deleteNode("쯔위")
  printNodes(head)

  deleteNode("지효")
  printNodes(head)

  deleteNode("재남")
  printNodes(head)
