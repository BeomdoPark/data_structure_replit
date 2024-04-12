import random


class Node():

    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return
    while current.link != start:
        current = current.link
        print(current.data[0], " 편의점, 거리 : ", current.data[1])


def calcMeter(dataArray):
    meter = []
    for i in range(10):
        x = dataArray[i][1]
        y = dataArray[i][2]
        meter.append((x**2 + y**2)**0.5)
    return meter


memory = []
head, current, pre = None, None, None
dataArray = []
for i in range(10):
    dataArray.append(
        (f"{chr(65+i)}", random.randint(1, 100), random.randint(1, 100)))

if __name__ == "__main__":

    meter_lst = calcMeter(dataArray)
    meter_idx = sorted(range(len(meter_lst)), key=lambda k: meter_lst[k])

    node = Node()
    node.data = dataArray[meter_idx.index(0)]
    head = node
    node.link = head
    memory.append(node)

    for idx in meter_idx:
        pre = node
        node = Node()
        node.data = [dataArray[idx][0], meter_lst[idx]]
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)
