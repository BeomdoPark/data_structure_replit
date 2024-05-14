#**********함수 선언부**********
def enqueue(data):
    global QUEUE_SIZE, queue, front, rear
    rear += 1
    queue[rear] = data


def dequeue():
    global QUEUE_SIZE, queue, front, rear
    front += 1
    data = queue[front]
    queue[front] = 0
    return data


#**********전역변수 선언부**********
#input()
PEOPLE_SIZE = int(input())
number_of_candy = list(map(int, input().split()))

#queue 생성
QUEUE_SIZE = sum(number_of_candy)
queue = [0 for _ in range(QUEUE_SIZE)]
front = rear = -1

#결과리스트
result_list = [0 for _ in range(PEOPLE_SIZE)]

#**********메인 함수 부분**********
if __name__ == '__main__':
    #number_of_candy가 빌 때까지 enqueue
    while (number_of_candy != [0 for _ in range(PEOPLE_SIZE)]):
        for idx in range(PEOPLE_SIZE):
            if number_of_candy[idx] != 0:
                enqueue(idx)
                number_of_candy[idx] -= 1
    #queue 가 빌 때까지 dequeue
    while (queue != [0 for _ in range(QUEUE_SIZE)]):
        for queue_idx in range(QUEUE_SIZE):
            #queue = [0,1,2,3,1,3,1,3,3]
            #queue_idx is iter in [0,1,2,3,4,5,6,7,8] => wating_time-1
            result_list[dequeue()] = queue_idx + 1
    print(result_list)
