katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('미나', 40), ('사나', 30),
         ('지효', 15)]


def update_and_insert_data(friend, val):
  for i in range(len(katok)):
    number = katok[i][1]
    if val >= number:
      katok.append((None, None))
      for j in range(len(katok) - 1, i, -1):
        katok[j] = katok[j - 1]
        katok[j - 1] = (None, None)
      katok[i] = (friend, val)
      return katok


if __name__ == "__main__":
  print(katok)
  while True:
    friend = input("추가할 친구 --> ")
    val = int(input("카톡 횟수 --> "))
    print(update_and_insert_data(friend, val))

    user = input("나가기 : 'Q' 입력" + "\n" + "계속 진행은 아무 키나 입력--> ")
    if user == 'Q' or user == 'q':
      break
