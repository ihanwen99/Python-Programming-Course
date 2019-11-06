num = input("Please input a 4-bits number: ")

num3 = (num % 10 + 9) % 10
num /= 10
num2 = (num % 10 + 9) % 10
num /= 10
num1 = (num % 10 + 9) % 10
num /= 10
num0 = (num % 10 + 9) % 10

s = str(num2) + str(num3) + str(num0) + str(num1)

print "Result is", s
