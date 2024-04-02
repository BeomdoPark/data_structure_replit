#데이터 삭제 함수

katok = ['다현', '정연', '쯔위', '사나', '지효']


def delete_data(position):
  if position < 0 or position > len(katok):
    print('데이터를 삽입할 범위를 벗어났습니다.')
    return

  kLen = len(katok)
  katok[position] = None

  for i in range(position + 1, kLen):
    katok[i] = None

  for i in range(kLen - 1, position - 1, -1):
    del (katok[i])


delete_data(1)
print(katok)
delete_data(3)
print(katok)
