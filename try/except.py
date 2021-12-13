''''
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")

#OR
try:
    value = 10/0
    print(value)

except ZeroDivisionError:
    print("zero error")'''

###############
try:
    value = 20/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")