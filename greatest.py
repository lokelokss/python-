number1 = 1
number2 = 2
number3 = 3
if (number1 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3
print(largest)
