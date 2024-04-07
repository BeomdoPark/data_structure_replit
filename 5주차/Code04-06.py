#단순 연결 리스트 생성
# + 노드 삽입 함수 추가


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


# head를 통해 Nodes를 삽입하는 함수
def insertNode(findData, insertData):
  global memory, head, current, pre

  if head.data == findData:  # 첫 번째 노드에 삽입
    node = Node()
    node.data = insertData
    node.link = head
    head = node
    return

  current = head
  while current.link != None:  # 중간 노드 삽입
    pre = current
    current = current.link
    if current.data == findData:
      node = Node()
      node.data = insertData
      node.link = current
      pre.link = node
      return

  node = Node()  # 첫, 중간 노드에 없을 경우 마지막 노드에 삽입
  node.data = insertData
  current.link = node


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

  insertNode("다현", "화사")
  printNodes(head)

  insertNode("사나", "솔라")
  printNodes(head)

  insertNode("재남", "문별")
  printNodes(head)
