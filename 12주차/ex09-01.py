class Graph():

    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = Graph(5)

GS25 = 0
CU = 1
Seven11 = 2
MiniStop = 3
Emart24 = 4

G1.graph[GS25][CU] = G1.graph[CU][GS25] = 1
G1.graph[GS25][Seven11] = G1.graph[Seven11][GS25] = 1
G1.graph[CU][MiniStop] = G1.graph[MiniStop][CU] = 1
G1.graph[CU][Seven11] = G1.graph[Seven11][CU] = 1
G1.graph[Seven11][MiniStop] = G1.graph[MiniStop][Seven11] = 1
G1.graph[Emart24][MiniStop] = G1.graph[MiniStop][Emart24] = 1

stack = []
visitedAry = []
stack.append(current)
visitedAry.append(current)

current = 0
while (len(stack) != 0):
    next = None
    #vertex 0 -> 1 -> 2 -> 3 -> 4
    for vertex in range(5):

        #만약 vertex가 연결되어있으면
        #current를 next로 업데이트 하고 stack에 저장
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break

    # next가 있으면 해당 노드 방문 후 정보저장
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    # next 없으면 current를 이전 방문 노드로 되돌림
    else:
        current = stack.pop()

재고 = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90],
      ['Emart24', 40]]

max = 0
idx = 0

for i in range(5):
    if max <= 재고[visitedAry[i]][1]:
        max = 재고[visitedAry[i]][1]
        idx = i

print("허니버터칩 최대 --> ", 재고[idx][0], max)
