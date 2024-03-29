list = [[] for i in range(4)]
count = 12
sum = 0

for i in range(0, 4):
  for k in range(0, 3):
    list[i].append(count)
    count = count - 1
for i in range(0, 4):
  for k in range(0, 3):
    print("{0:<3}".format(list[i][k]), end=" ")
    sum += list[i][k]
  print("")

print("배열의 합계 ==>", sum)
