# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added together
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)
print(number1 + ' + ' + number2 + ' = ' + str(sum))