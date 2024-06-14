def findJudge(N, trust):
    # 초기화
    trust_count = [0] * (N + 1)
    trusted_by = [0] * (N + 1)

    # 신뢰 관계를 이용하여 trust_count와 trusted_by 배열 업데이트
    for a, b in trust:
        trust_count[b] += 1
        trusted_by[a] += 1

    # 판사를 찾기
    for i in range(1, N + 1):
        if trust_count[i] == N - 1 and trusted_by[i] == 0:
            return i

    return -1


# 테스트 입력
N = 3
trust = [[1, 3], [2, 3]]

# 출력 판사 번호
print(findJudge(N, trust))  # 출력: 3
