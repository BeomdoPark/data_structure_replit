def dedeQueue():
    global SIZE, queue, front, rear
    if (front == rear):  #isQueueEmpty()
        print("식당 영업 종료!")
        return ""
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front + 1, SIZE):
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1

    return data


SIZE = 5
queue = ['정국', '뷔', '지민', '진', '슈가']
front = -1
rear = 4

print("대기 줄 상태 : ", queue)
print(dedeQueue(), "님 식당에 들어감")
print("대기 줄 상태 : ", queue)
print(dedeQueue(), "님 식당에 들어감")
print("대기 줄 상태 : ", queue)
print(dedeQueue(), "님 식당에 들어감")
print("대기 줄 상태 : ", queue)
print(dedeQueue(), "님 식당에 들어감")
print("대기 줄 상태 : ", queue)
print(dedeQueue(), "님 식당에 들어감")
print("대기 줄 상태 : ", queue)
print(dedeQueue())
