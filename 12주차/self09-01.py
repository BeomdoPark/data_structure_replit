class Graph():

    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = Graph(4)

A = 0
B = 1
C = 2
D = 3
G1.graph[A][D] = G1.graph[D][A] = 1
G1.graph[D][B] = G1.graph[B][D] = 1
G1.graph[C][B] = G1.graph[B][C] = 1

print('## 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()
