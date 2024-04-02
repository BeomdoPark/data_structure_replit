#특수 다항식의 선형 리스트 표현과 계산 프로그램
#tx라는 차수 배열을 추가함


## 함수 선언 부분 ##
def printPoly(t_x, p_x):
  polyStr = "P(x) = "  #다항식 표현을 담는 문자열

  for i in range(len(p_x)):
    term = t_x[i]  # 항의 차수
    coef = p_x[i]  # 계수

    if coef >= 0:
      polyStr += "+"
    polyStr += str(coef) + "x^" + str(term) + " "

  return polyStr


def calcPoly(xVal, t_x, p_x):
  retValue = 0

  for i in range(len(px)):
    term = t_x[i]
    coef = p_x[i]
    retValue += coef * xVal**term  #계수 * x값 ** x의 차수

  return retValue


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
px = [7, -4, 5]

## 메인 코드 부분 ##
if __name__ == "__main__":
  pStr = printPoly(tx, px)
  print(pStr)

  xValue = int(input("X값 --> "))

  pxValue = calcPoly(xValue, tx, px)
  print(pxValue)
