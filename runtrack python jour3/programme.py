for program in range(1, 101):
  if program % 3 == 0 and program % 5 == 0:
    print("FizzBuzz")
  elif program % 3 == 0:
    print("Fizz")
  elif program % 5 == 0:
    print("Buzz")
  else:
    print(program)