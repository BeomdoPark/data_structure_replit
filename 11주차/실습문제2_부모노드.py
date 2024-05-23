# 트리노드 기본 틀 class
class TreeNode:

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None


def make_binary_tree(nodes, node1, node2):
    # if node not in nodes:
    #     nodes[node] = TreeNode()
    #     nodes[node].data = node
    if node1 in nodes:
        nodes[node2] = TreeNode()
        nodes[node2].data = node2
        nodes[node2].parent = node1
        # if nodes[node1].left is None:
        #     nodes[node1].left = nodes[node2]
        # else:
        #     node1.right = nodes[node2]
    elif node2 in nodes:
        nodes[node1] = TreeNode()
        nodes[node1].data = node1
        nodes[node1].parent = node2
        # if node2.left is None:
        #     node2.left = nodes[node1]
        # else:
        #     node2.right = nodes[node1]


#이진 트리 입력하여 이차원 리스트에 저장
lines = int(input())

nodes = {}
nodes['1'] = TreeNode()
nodes['1'].data = '1'

for _ in range(lines - 1):
    node1, node2 = input().split()
    make_binary_tree(nodes, node1, node2)

for i in range(2, lines + 1):
    if nodes[str(i)].parent is not None:
        print(nodes[str(i)].parent, end=" ")
