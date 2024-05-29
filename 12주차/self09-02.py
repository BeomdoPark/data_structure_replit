class Graph():

    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = Graph(6)
stack = []
visitedAry = []
문별 = 0
솔라 = 1
휘인 = 2
쯔위 = 3
선미 = 4
화사 = 5

G1.graph[문별][솔라] = G1.graph[솔라][문별] = 1
G1.graph[문별][휘인] = G1.graph[휘인][문별] = 1
G1.graph[솔라][쯔위] = G1.graph[쯔위][솔라] = 1
G1.graph[휘인][쯔위] = G1.graph[쯔위][휘인] = 1
G1.graph[선미][쯔위] = G1.graph[쯔위][선미] = 1
G1.graph[화사][쯔위] = G1.graph[쯔위][화사] = 1
G1.graph[화사][선미] = G1.graph[선미][화사] = 1

current = 0
stack.append(current)
visitedAry.append(current)
while (len(stack) != 0):
    next = None
    for vertex in range(6):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()
print('방문순서 --> ', end="")
name_lst = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
for i in visitedAry:
    print(name_lst[i], end=" ")
