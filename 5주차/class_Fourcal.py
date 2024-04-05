class Fourcal:

  def setdata(self, first, second):
    self.first = first
    self.second = second

  def add(self):
    result = self.first + self.second
    return result

  def mul(self):
    result = self.first * self.second
    return result

  def sub(self):
    result = self.first - self.second
    return result

  def div(self):
    result = self.first / self.second
    return result


a = Fourcal()
b = Fourcal()

a.setdata(4, 2)
b.setdata(3, 8)

print("a.add(), a.mul(), a.sub(), a.div() = ", a.add(), a.mul(), a.sub(),
      a.div())
print("b.add(), b.mul(), b.sub(), b.div() = ", b.add(), b.mul(), b.sub(),
      b.div())
