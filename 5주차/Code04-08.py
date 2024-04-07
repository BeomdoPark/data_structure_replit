#단순 연결 리스트의 노드 검색 함수


#클래스 선언#
class Node():

  def __init__(self):
    self.data = None
    self.link = None


def printNodes(start):
  current = start
  if current == None:
    return
  print(current.data, end=' ')
  while current.link != None:
    current = current.link
    print(current.data, end=' ')
  print()


def findNode(findData):
  global memory, head, current, pre

  current = head
  if current.data == findData:
    return current
  while current.link != None:
    current = current.link
    if current.data == findData:
      return current
  return Node()  # 빈 노드 반환


# 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인 코드
if __name__ == "__main__":

  node = Node()  # 첫 번째 노드
  node.data = dataArray[0]
  head = node
  memory.append(node)

  for data in dataArray[1:]:  # 두 번째 노드부터
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

  printNodes(head)

  #찾은 노드를 fNode에 복사
  fNode = findNode("다현")
  print(fNode.data)

  fNode = findNode("쯔위")
  print(fNode.data)

  fNode = findNode("재남")
  print(fNode.data)
