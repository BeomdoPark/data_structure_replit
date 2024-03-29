## 함수 선언 부분 ##
def printPoly(p_x):
  term = len(p_x) - 1  #최고차항 = 배열길이 -1

  polyStr = "P(x) = "  #다항식 표현을 담는 문자열

  for i in range(len(p_x)):
    coef = p_x[i]  #계수는 px배열의 원소들

    if coef != 0:  # 계수가 0인 항 출력안함
      if i > 0 and coef > 0:  # 첫째항, 음수계수일 때 + 부호 안붙임
        polyStr += "+"
      polyStr += str(coef) + "x^" + str(term) + " "
    term -= 1  #polyStr에 한개 항 추가 하고, 차수를 -1

  return polyStr


def calcPoly(xVal, p_x):
  retValue = 0
  term = len(p_x) - 1
  for i in range(len(px)):
    coef = p_x[i]
    retValue += coef * xVal**term  #계수 * x값 ** x의 차수
    term -= 1

  return retValue


## 전역 변수 선언 부분 ##
px = [7, -4, 0, 5]

## 메인 코드 부분 ##
if __name__ == "__main__":
  pStr = printPoly(px)
  print(pStr)

  xValue = int(input("X값 --> "))

  pxValue = calcPoly(xValue, px)
  print(pxValue)
