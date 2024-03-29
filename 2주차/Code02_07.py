def can_you_eat_coffee(money):
  canEat = False
  if money >= 300:
    canEat = True
    charge = money - 300
    global coffee_count
    coffee_count -= 1
    return [canEat, charge]

  else:
    return [canEat, money]


coffee_count = 10

while coffee_count > 0:
  user_money = int(input("돈을 넣어 주세요: "))
  lst = can_you_eat_coffee(user_money)

  if lst[0]:  #300원 이상을 냈을 때
    if lst[1]:  # 거스름돈이 있으면
      print(f"거스름돈 {lst[1]}을 주고 커피를 줍니다.")
    else:  # 거스름돈이 없으면
      print("커피를 줍니다.")
  else:  # 300원보다 적게 냈을 때
    print("돈을 다시 돌려주고 커피를 주지 않습니다.")

  print(f"남은 커피의 양은 {coffee_count}개입니다.")
print("종료합니다.")
