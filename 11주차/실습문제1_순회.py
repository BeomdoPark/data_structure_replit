# 이진 트리를 입력받아 전위, 중위, 후위 순회 한 결과를 출력하세요.
#  첫째 줄에는 이진 트리의 노드 개수(N) 입력
#  둘째 줄 부터 N개의 줄에 각 노드와 왼쪽 자식 오른쪽 자식 노드 입력
#  노드의 이름은 A부터 차례대로 알파벳 대문자로 입력
#  A가 루트 노드가 되고, 자식 노드가 없는 경우 “ . ” 으로 입력


# 트리노드 기본 틀 class
class TreeNode:

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


def make_binary_tree(nodes, node, left, right):
    if node not in nodes:
        nodes[node] = TreeNode()
        nodes[node].data = node
    if left != '.':
        nodes[left] = TreeNode()
        nodes[left].data = left
        nodes[node].left = nodes[left]
    if right != '.':
        nodes[right] = TreeNode()
        nodes[right].data = right
        nodes[node].right = nodes[right]


#전위, 중위, 후위 순회 함수 선언
# left 또는 right로 들어갈 때는 재귀로 들어감
def preorder(node):
    if node is None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)  # 재귀로 left
    print(node.data, end='->')
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')


#이진 트리 입력하여 이차원 리스트에 저장
lines = int(input())

nodes = {}
for _ in range(lines):
    node, left, right = input().split()
    make_binary_tree(nodes, node, left, right)

root_node = nodes['A']
##################################################
print('전위 순회 : ', end=' ')
preorder(root_node)
print('끝')

print('중위 순회 : ', end=' ')
inorder(root_node)
print('끝')

print('후위 순회 : ', end=' ')
postorder(root_node)
print('끝')
