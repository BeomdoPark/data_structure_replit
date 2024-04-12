class Node():

    def __init__(self):
        self.data = None
        self.right_link = None
        self.left_link = None


def printNodes(start):
    current = start
    if current.right_link == None:
        return

    print("정방향 --> ", current.data, end=' ')
    while current.right_link != None:
        current = current.right_link
        print(current.data, end=' ')
    print()

    print("역방향 --> ", current.data, end=' ')
    while current.left_link != None:
        current = current.left_link
        print(current.data, end=' ')
    print()


memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    node.right_link = head
    node.left_link = None
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.right_link = node
        node.left_link = pre
        node.right_link = None
        memory.append(node)
    printNodes(head)
