import random


def selcetNum():
  return random.sample(range(1, 46), 6)


print("** 로또 번호 생성을 시작합니다. **")
user = int(input("몇 번을 뽑을까요?"))
for _ in range(user):
  print("자동번호--> ", *selcetNum())
