#. 함수를 이용하여 이름, 나이, 성별(기본값=남성)을 받아 자기소개를 출력하는 프로그램을 작성하자


def intro_myself(name, age, gender=True):
  gender = "남자" if gender else "여자"
  print(f"나의 이름은 {name}입니다.")
  print(f"나이는 {age}살입니다.")
  print(f"{gender}입니다.")


intro_myself("박범도", 25, True)
intro_myself("홍길동", 20, False)
