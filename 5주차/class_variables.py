class Family:
  lastname = "김"


a = Family()
b = Family()

#"김"으로 모두 초기화
print("Family lastname : ", Family.lastname)
print("a lastname : ", a.lastname)
print("b lastname : ", b.lastname)
print()

#family로 생성된 변수들이 모두 바뀜
Family.lastname = "박"
print("a lastname : ", a.lastname)
print("b lastname : ", b.lastname)
print()

#a변수만 바뀜
a.lastname = "최"
print("Family lastname : ", Family.lastname)
print("a lastname : ", a.lastname)
print("b lastname : ", b.lastname)
print()
