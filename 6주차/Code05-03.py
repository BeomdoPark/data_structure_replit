class Node():

    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = "다현"
node1.link = node1

node2 = Node()
node2.data = "정연"
node2.link = node1

node3 = Node()
node3.data = "쯔위"
node3.link = node1

node4 = Node()
node4.data = "사나"
node4.link = node1

node5 = Node()
node5.data = "지효"
node5.link = node1

node2.link = node3.link
del (node3)

current = node1
print(current.data, end=" ")
while current.link != node1:
    current = current.link
    print(current.data, end=" ")
