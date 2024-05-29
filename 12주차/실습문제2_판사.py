def findJudge(N, trust):
    if N == 1:
        return 1
    # 신뢰 횟수를 저장하기 위한 리스트 초기화 (0으로 초기화, 인덱스 0은 사용하지 않음)
    count = [0 for _ in range(N + 1)]
    answer = -1

    # trust 리스트를 순회하며 신뢰 정보를 count 리스트에 반영
    for i in range(len(trust)):
        count[trust[i][1]] += 1  # 신뢰를 받는 사람의 카운트를 증가시킴
        # 만약 어떤 사람이 (N-1)번 이상 신뢰를 받으면 잠정적인 판사로 설정
        if count[trust[i][1]] >= N - 1:
            answer = trust[i][1]
            break  # 잠정적인 판사를 찾으면 루프 종료

    # 잠정적인 판사가 실제로 다른 사람을 신뢰하지 않는지 확인
    for i in range(len(trust)):
        if trust[i][0] == answer:  # 잠정적인 판사가 다른 사람을 신뢰하면
            answer = -1  # 판사 자격 박탈
            break

    return answer  # 판사가 있으면 그 사람의 번호, 없으면 -1 반환


# 테스트 예제
print(findJudge(2, [[1, 2]]))  # 출력: 2
print(findJudge(3, [[1, 3], [2, 3]]))  # 출력: 3
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))  # 출력: -1
