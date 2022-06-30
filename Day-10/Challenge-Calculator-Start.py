from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 / n2


def divide(n1, n2):
  if n2 != 0:
    return n1 / n2
  else:
    print("Invalid, cannot be divided by 0")

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

def calculator():
  num1 = float(input('Enter the number: '))

  for operation in operations:
      print(operation)

  should_continue = True

  while should_continue: 
    choose_operation = input('Choose which operation you want to perform: ')

    num2 = float(input('Enter the next number: '))

    operate_calculate = operations[choose_operation]
    result = operate_calculate(num1, num2)

    print(f"{num1} {choose_operation} {num2} = {result}")

    get_continue = input(f"Type 'y' to continue calculate with {result} Type 'y' or 'n' to start a new calculation: ")
    if get_continue == 'y':
      num1 = result
    else:
      should_continue = False
      calculator()

calculator()
