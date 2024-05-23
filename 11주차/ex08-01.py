class TreeNode():

    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


memory = []
root = None

nameAry = [
    '래쓰비캔커피', '래쓰비캔커피', '래쓰비캔커피', '도시락', '도시락', '삼각김밥', '래쓰비캔커피', '도시락',
    '코카콜라', '삼다수', '래쓰비캔커피', '래쓰비캔커피', '래쓰비캔커피', '츄파춥스', '츄파춥스', '래쓰비캔커피',
    '코카콜라', '츄파춥스', '삼각김밥', '코카콜라'
]

node = TreeNode()

#루트 노드 생성
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:

    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name == current.data:
            break
        elif name < current.data:
            if (current.left == None):
                current.left = node
                memory.append(node)
            current = current.left
        elif name > current.data:
            if (current.right == None):
                current.right = node
                memory.append(node)
            current = current.right

print('중복 O :', nameAry)
print('\n이진 탐색 트리 구성 완료!\n')

print('중복 X : ', end="")
for node in memory:
    print(node.data, end=' ')
