from queue import Queue


def time_to_get_all_candies(num_children, candies):
    queue = Queue()

    for i in range(num_children):
        queue.put((i, candies[i]))

    time = 0

    # 모든 아이들이 캔디를 받을때까지
    while not queue.empty():
        idx, candy_needed = queue.get()
        time += 1
        candy_needed -= 1

        if candy_needed > 0:
            queue.put((idx, candy_needed))

    return time


num_children = 4
candies = [1, 3, 1, 4]

print(time_to_get_all_candies(num_children, candies))
