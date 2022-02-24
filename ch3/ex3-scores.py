# program to evaluate scores

try:
  score = float(input("Please enter a score between 0.0 and 1.0\n"))
  if score<0 or score>1:
      raise Exception()
  elif score >= 0.9:
      grade = 'A'
  elif score >= 0.8:
      grade = 'B'
  elif score >= 0.7:
      grade = 'C'
  elif score >= 0.6:
      grade = 'D'
  elif score <0.6:
      grade = 'F'
  print(grade)

except:
  print("your score needs to be greater >= 0 and <= 1.0")

# how to catch and should I catch that value error?
# you can identify numbers by doing:
    # 1
    # if type(myVariable) == int or type(myVariable) == float:
    # 2
    # using the numbers.Number module
    # import Numbers
    # variable = 5
    # print(isinstance(5, numbers.Number))
    # * this approach can behave unexpectedly with numeric type outside core Python
    # 3
    # try:
    #  tmp = int(myVariable)
    #  print('The variable is a number')
    # except:
    #  print('The variable is not a number')