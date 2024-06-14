def findCenter(edges):
    # 두 간선을 확인하여 중심 노드를 찾는다
    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
        return edges[0][0]
    else:
        return edges[0][1]


# 테스트 입력
edges1 = [[1, 2], [2, 3], [4, 2]]
edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]
# 출력 중심 노드
print(findCenter(edges1))  # 출력: 2
print(findCenter(edges2))  # 출력: 1
