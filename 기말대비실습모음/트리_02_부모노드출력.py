class TreeNode:
    def __init__(self):
        self.data = None
        self.parent = None


def make_binary_tree(nodes, node1, node2):
    if node1 in nodes:
        nodes[node2] = TreeNode()
        nodes[node2].data = node2
        nodes[node2].parent = node1
    elif node2 in nodes:
        nodes[node1] = TreeNode()
        nodes[node1].data = node1
        nodes[node1].parent = node2


# 이진 트리 입력하여 이차원 리스트에 저장
lines = int(input("노드 개수: "))

nodes = {}
nodes["1"] = TreeNode()
nodes["1"].data = "1"

for _ in range(lines - 1):
    node1, node2 = input().split()
    make_binary_tree(nodes, node1, node2)

for i in range(2, lines + 1):
    if nodes[str(i)].parent is not None:
        print(nodes[str(i)].parent)
