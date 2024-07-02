print("Present Sir")
a = int(input("enter first number\n"))
b = int(input("enter second number\n"))
c = int(input(
  "Enter 1 for addition\nEnter 2 for subtration\nEnter 3 for multiplication\nEnter 4 for division\nEnter 5 for exponential\nEnter 6 for Floor division\n"))
if c == 1:
  print(a + b)
elif c == 2:
  print(a - b)
elif c == 3:
  print(a * b)
elif c == 4:
  print(a / b)
elif c == 5:
  print(a - b)
elif c == 6:
  print(a // b)
else:
  print("wrong choice")