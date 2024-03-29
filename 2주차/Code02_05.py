def multi(v1, v2):
  retList = [v1 + v2, v1 - v2, v1 * v2, v1 // v2, v1 % v2, v1**v2]
  return retList


lst = []
lst = multi(100, 20)
print(f"multi()에서 반환한 값 ==> [{lst[0]}, {lst[1]}, {lst[2]}, "
      f"{lst[3]}, {lst[4]}, {lst[5]}]")
