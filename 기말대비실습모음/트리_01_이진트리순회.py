class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def pre_order(node):
    if node is None:
        return ""
    return node.key + pre_order(node.left) + pre_order(node.right)


def in_order(node):
    if node is None:
        return ""
    return in_order(node.left) + node.key + in_order(node.right)


def post_order(node):
    if node is None:
        return ""
    return post_order(node.left) + post_order(node.right) + node.key


# 입력 받기
n = int(input("노드 개수: "))
tree = {}

for _ in range(n):
    node_info = input().split()
    node, left, right = node_info[0], node_info[1], node_info[2]
    if node not in tree:
        tree[node] = Node(node)
    if left != ".":
        tree[node].left = Node(left)
        tree[left] = tree[node].left
    if right != ".":
        tree[node].right = Node(right)
        tree[right] = tree[node].right

# 트리의 루트 노드는 'A'로 설정
root = tree["A"]

# 결과 출력
print("전위 순회:", pre_order(root))
print("중위 순회:", in_order(root))
print("후위 순회:", post_order(root))
