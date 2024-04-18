class Node(self):
    self.data = None
    self.link = None


def print_nodes():
    pass


memory = []  # linked list의 data를 저장할 공간
head, pre, current = None, None, None
data_array = [1, 2, 3, 4]  # 유저에게 받는 data


if __name__ == "__main__":

    if len(memory) == 0:
        node = Node()
        node.data = data_array[0]
        head = node
        memory.append(node)
    else:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
