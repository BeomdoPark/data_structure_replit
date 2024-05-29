class Graph():

    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


##input data
edges1 = [[1, 2], [2, 3], [4, 2]]
edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]

# size1 = 4  # 1~4 숫자
# size2 = 5  # 1~5 숫자

# G1 = Graph(size1)
# G2 = Graph(size2)

# #G1 구현
# for i in range(size1 - 1):
#     row, col = edges1[i][0], edges1[i][1]
#     G1.graph[row - 1][col - 1] = 1
#     G1.graph[col - 1][row - 1] = 1
# #G2 구현
# for i in range(size2 - 1):
#     row, col = edges2[i][0], edges2[i][1]
#     G2.graph[row - 1][col - 1] = 1
#     G2.graph[row - 1][col - 1] = 1


def findCenter(edges):
    result = 0
    z1 = edges[0]

    for i in range(1, len(edges)):
        if edges[i][0] in z1:
            result = edges[i][0]
        elif edges[i][1] in z1:
            result = edges[i][1]
    return result


print(findCenter(edges1), "\n", findCenter(edges2), sep="")
