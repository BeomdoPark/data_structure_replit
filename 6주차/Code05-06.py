class Node:

    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=" ")
    while current.link != start:
        current = current.link
        print(current.data, end=" ")
    print()


def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link

        last.link = head
        del current
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del current
            return

    node = Node()
    node.data = insertData
    current.link = node
    node.link = head


memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
    printNodes(head)

    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)

    deleteNode("지효")
    printNodes(head)

    deleteNode("재남")
    printNodes(head)
