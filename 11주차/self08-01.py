class TreeNode():

    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

node9 = TreeNode()
node9.data = '다현'
node4.right = node9

node11 = TreeNode()
node11.data = '사나'
node6.right = node11


#전위, 중위, 후위 순회
# left 또는 right로 들어갈 때는 재귀로 들어감
def preorder(node):
    if node == None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node == None:
        return
    inorder(node.left)  # 재귀로 left
    print(node.data, end='->')
    inorder(node.right)


def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')


print('전위 순회 : ', end=' ')
preorder(node1)
print('끝')

print('중위 순회 : ', end=' ')
inorder(node1)
print('끝')

print('후위 순회 : ', end=' ')
postorder(node1)
print('끝')
