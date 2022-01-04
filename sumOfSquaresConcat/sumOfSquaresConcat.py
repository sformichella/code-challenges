# When is x^2 + y^2 equal to x concatted with y?
from math import sqrt, floor
from functools import reduce

def check(n):
  # n is the number of digits of y
  valuesOfy = []
  offset = (10**n)/2
  for i in range(10**(n-1), 10**n):
    test = -i**2 + i + offset**2
    if test < 0: continue
    if sqrt(test).is_integer(): valuesOfy.append(i)
  valuesOfx = []
  for y in valuesOfy:
    num = -y**2 + y + offset**2
    one = sqrt(num) + offset
    two = -sqrt(num) + offset
    solutions = [int(one)]
    if two > 0: solutions.append(int(two))
    valuesOfx.append(solutions)
  return {
    "y": valuesOfy,
    "x": valuesOfx
  }

def prettyPrint(n):
  solutions = check(n)
  def makeStr(x, y):
    return "{}^2 + {}^2 = {}{}\n".format(x,y,x,y)
  def reduceYs(enum):
    index = enum[0]
    y = enum[1]
    return reduce(lambda w, z: w + makeStr(z, y), solutions["x"][index], "")
  return reduce(lambda x, y: x + reduceYs(y), enumerate(solutions["y"]), "")


print(
  prettyPrint(4)
)
    