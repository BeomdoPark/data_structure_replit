from itertools import product

N, K_count = map(int, input().split())
K = list(map(int, input().split()))

combinations = list(product(K, repeat=K_count))
valid_combinations = [c for c in combinations if int("".join(map(str, c))) <= N]

if valid_combinations:
    max_number = max(valid_combinations, key=lambda x: int("".join(map(str, x))))
    print("".join(map(str, max_number)))
else:
    print(-1)
