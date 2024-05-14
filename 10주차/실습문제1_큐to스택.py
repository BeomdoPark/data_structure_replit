#queue 2개를 이용한 Stack 구현
class myStack():

    def __init__(self):
        self.main_queue = queue()
        self.sub_queue = queue()

    def empty(self):
        return self.main_queue.empty()

    def top(self):
        #main_queue가 한개 남을 때까지 뽑기.
        while (self.main_queue.front + 1 != self.main_queue.rear):
            data = self.main_queue.dequeue()
            #뽑은값은 sub_queue에 넣기
            self.sub_queue.enqueue(data)
        #하나 남은 값을 top_data에 저장 후 서브 큐에 넣기
        top_data = self.main_queue.peek()
        data = self.main_queue.dequeue()
        self.sub_queue.enqueue(data)

        #sub_queue에 있는 값들을 다시 main_queue에 넣기
        while (not self.sub_queue.empty()):
            data = self.sub_queue.dequeue()
            self.main_queue.enqueue(data)
        return top_data

    #메인큐에 들어온 순서대로 넣기
    def push(self, data):
        self.main_queue.enqueue(data)

    def pop(self):
        #main_queue가 한개 남을 때까지 뽑기.
        while (self.main_queue.front + 1 != self.main_queue.rear):
            data = self.main_queue.dequeue()
            #뽑은값은 sub_queue에 넣기
            self.sub_queue.enqueue(data)

        #하나 남은 값을 pop_data에 저장 후 버리기
        pop_data = self.main_queue.peek()
        self.main_queue.dequeue()

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

    def isQueueFull(self):
        if (self.rear != self.SIZE - 1):
            return False
        elif (self.rear == self.SIZE - 1) and (self.front == -1):
            return True
        else:
            for i in range(self.front + 1, self.SIZE):
                self.queue[i - 1] = self.queue[i]
                self.queue[i] = None
            self.front -= 1
            self.rear -= 1
            return False

    def peek(self):
        return self.queue[self.front + 1]

    def empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if (self.isQueueFull()):
            print("* 큐가 꽉 찼습니다. *")
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        # if (self.front == self.rear):  #isQueueEmpty()
        #     print("큐가 비었습니다.")
        #     return False
        self.front += 1
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data


if __name__ == '__main__':
    my_stack = myStack()
    result_list = []
    select = input("push(1) / pop(2) / top(3) / empty(4) / exit(X) :")
    while (select.lower() != 'x'):
        if (select == '1'):
            data = input("push할 데이터 입력 : ")
            result_list.append(my_stack.push(data))
        elif (select == '2'):
            if (my_stack.empty()):
                print("큐가 비어있습니다.")
            else:
                result_list.append(my_stack.pop())
        elif (select == '3'):
            if (my_stack.empty()):
                print("큐가 비어있습니다.")
            else:
                result_list.append(my_stack.top())
        elif (select == '4'):
            result_list.append(my_stack.empty())
        else:
            print("* 잘못된 입력입니다. *")

        print("현재 queue = ", my_stack.main_queue.queue)
        print("현재 출력 = ", result_list, end="\n\n")
        select = input("push(1) / pop(2) / top(3) / empty(4) / exit(X) :")

    # result_list.append(my_stack.push(1))
    # result_list.append(my_stack.push(2))
    # result_list.append(my_stack.top())
    # result_list.append(my_stack.pop())
    # result_list.append(my_stack.empty())
    print("최종 출력 = ", result_list)
