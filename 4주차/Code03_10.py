#특수 다항식의 선형 리스트 표현과 계산 프로그램
#tx라는 차수 배열을 선언함 -> 이차원 배열로 txpx 구현


## 함수 선언 부분 ##
def printPoly(t_x_p_x):
  polyStr = "P(x) = "  #다항식 표현을 담는 문자열

  for i in range(3):
    term = t_x_p_x[0][i]  # 항의 차수
    coef = t_x_p_x[1][i]  # 계수

    if coef >= 0:
      polyStr += "+"
    polyStr += str(coef) + "x^" + str(term) + " "

  return polyStr


def calcPoly(xVal, t_x_p_x):
  retValue = 0

  for i in range(3):
    term = t_x_p_x[0][i]  # 항의 차수
    coef = t_x_p_x[1][i]  # 계수
    retValue += coef * xVal**term  #계수 * x값 ** x의 차수

  return retValue


## 전역 변수 선언 부분 ##
tx_px = [[300, 20, 0], [7, -4, 5]]

## 메인 코드 부분 ##
if __name__ == "__main__":
  pStr = printPoly(tx_px)
  print(pStr)

  xValue = int(input("X값 --> "))

  pxValue = calcPoly(xValue, tx_px)
  print(pxValue)
