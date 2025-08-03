def add(num1, num2):
    return num1  + num2

def substract(num1, num2):
    return num1 - num2

def multiplacation(num1, num2):
    return num1*num2
def divition(num1, num2):
    return num1/num2

while True:
    print("choose an operation: \n\n" \
          "1. add\n" \
          '2. substract\n' \
          '3. multply\n'\
          '4. divide\n'
          "5. Exit\n"
          )
    operation = int(input('please select an option: '))
    if operation  == 1:
        num1 = int(input('please enter the first number: '))
        num2 = int(input('Please Enter the second number: '))
        print("Answer: {} + {} = " .format(num1, num2), add(num1, num2), "\n")

    elif operation  == 2:
        num1 = int(input('please enter the first number: '))
        num2 = int(input('Please Enter the second number: '))
        print("Answer: {} - {} = " .format(num1, num2), substract(num1, num2), "\n")
    elif operation  == 3:
        num1 = int(input('please enter the first number: '))
        num2 = int(input('Please Enter the second number: '))
        print("Answer: {} * {} = " .format(num1, num2), multiplacation(num1, num2), "\n")
    elif  operation  == 4:
        num1 = int(input('please enter the first number: '))
        num2 = int(input('Please Enter the second number: '))
        print("Answer: {} / {} = " .format(num1, num2), divition(num1, num2), "\n")

    elif operation == 5:
        print('Thank you For using our system')  
        break
    else:
        print("Please enter a valid number")

