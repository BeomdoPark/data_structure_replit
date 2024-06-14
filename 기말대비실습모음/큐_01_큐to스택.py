from queue import Queue

# queue.put(data)
# queue.get()
# queue.qsize()
# queue.empty()
# queue.full()


class Stack:
    def __init__(self):
        self.main_queue = Queue()
        self.sub_queue = Queue()

    def push(self, date) -> None:
        if self.main_queue.qsize() == 1:
            self.sub_queue.put(self.main_queue.get())
        self.main_queue.put(date)

    def pop(self) -> int:
        if not self.main_queue.empty():
            self.sub_queue.put(self.main_queue.get())
        # swap으로 원래대로 돌리기
        self.main_queue, self.sub_queue = self.sub_queue, self.main_queue

    def pop(self):
        return self.main_queue.get()

    def top(self):
        top_elem = self.main_queue.get()
        self.main_queue.put(top_elem)
        while not self.main_queue.empty():
            self.sub_queue.put(self.main_queue.get())
        self.main_queue, self.sub_queue = self.sub_queue, self.main_queue
        return top_elem

    def empty(self):
        return self.main_queue.empty()


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())
print(stack.pop())
print(stack.empty())
print(stack.pop())
print(stack.pop())
print(stack.empty())
