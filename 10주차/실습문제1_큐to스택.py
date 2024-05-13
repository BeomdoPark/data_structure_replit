class myStack():

    def __init__(self):
        self.main_queue = queue()
        self.sub_queue = queue()

    def empty(self):
        return self.main_queue.empty()

    def top(self):
        pass

    #메인큐에 들어온 순서대로 넣기
    def push(self, data):
        self.main_queue.enqueue(data)

    def pop(self):
        #main_queue가 한개 남을 때까지 뽑기.
        while (self.main_queue.front + 1 == self.main_queue.rear):
            data = self.main_queue.dequeue()
            #뽑은값은 sub_queue에 넣기
            self.sub_queue.enqueue(data)
        #하나 남은 값이 pop하려는 데이터임.
        pop_data = self.main_queue.dequeue()
        #sub_queue에 있는 값들을 다시 main_queue에 넣기
        while (not self.sub_queue.empty()):
            data = self.sub_queue.dequeue()
            self.main_queue.enqueue(data)
        return pop_data


class queue():

    def __init__(self):
        self.SIZE = 6
        self.queue = [None for _ in range(self.SIZE)]
        self.front = self.rear = -1

    def empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if (self.rear == self.SIZE - 1):
            print("큐가 꽉 찼습니다.")
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        # if (self.front == self.rear):  #isQueueEmpty()
        #     print("큐가 비었습니다.")
        #     return None
        self.front += 1
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data


if __name__ == '__main__':
    my_stack = myStack()
    return_list = []
    return_list.append(my_stack.push(1))
    return_list.append(my_stack.push(2))
    # return_list.append(my_stack.top())
    return_list.append(my_stack.pop())
    return_list.append(my_stack.empty())
    print(return_list)
