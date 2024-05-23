import os


class TreeNode():

    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


nameAry = []

dir_path = 'C:\\Program Files\\Common Files'
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(file)
        nameAry.append(file_path)

memory = []
root = None

node = TreeNode()

#루트 노드 생성
node.data = nameAry[0]
root = node
# memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name == current.data:
            memory.append(node.data)
            break
        elif name < current.data:
            if (current.left == None):
                current.left = node
                break
            current = current.left
        elif name > current.data:
            if (current.right == None):
                current.right = node
                break
            current = current.right

memory = list(set(memory))
print(memory)
