def enQueue(data):
    global SIZE, queue, front, rear
    rear = (rear + 1) % SIZE
    queue[rear] = data


SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0
time = 0
enQueueList = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]

if __name__ == "__main__":

    print(f"귀하의 대기 예상시간은 {time}분입니다.")
    print("현재 대기 콜", queue, end="\n\n")

    for tup in enQueueList:
        enQueue(tup)
        time += tup[1]
        print(f"귀하의 대기 예상시간은 {time}분입니다.")
        print("현재 대기 콜", queue, end="\n\n")

    print('최종 대기 콜 -> ', queue)
    print('프로그램 종료!')
