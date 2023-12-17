# Завдання 3
# Створіть інженерний калькулятор з використанням модуля math, в якому
# передбачене меню. Під час створення дотримуйтесь правил специфікації
# PEP 8.

import math


def addition_nums(a, b):
    """Addition of two arguments"""
    print(f"Addition result = {a + b}")


def subtraction_nums(a, b):
    """Substraction of two arguments"""
    print(f"Substraction result = {a - b}")


def multiplication_nums(a, b):
    """Multiplication of two arguments"""
    print(f"Multiplication result = {a * b}")


def division_nums(a, b):
    """Substraction of two arguments and conditions for 0"""
    if b == 0:
        print("0 is incorect value!")
    else:
        print(f"Division result = {a / b}")


def exponentiation_nums(a, b):
    """Exponentiation of argument a with power b"""
    print(f"Exponentiation result = {a ** b}")


def square_root_nums(a):
    """Square root of one argument"""
    print(f"Square root = {math.sqrt(a)}")


def cube_root_nums(a):
    """Cube root of one argument"""
    print(f"Cube root = {a ** (1 / 3)}")


while True:  # Main loop
    print(
        "\nAccessible mathematical operations: \n\t 1.Addition \n\t "
        "2.Subtraction \n\t 3.Multiplication \n\t 4.Division \n\t "
        "5.Exponentiation \n\t 6.Square root \n\t 7.Cube root\n"
    )  # Varients of math operations

    while True:  # input math operation and check value exceptions
        try:
            math_operation_number = int(input("Select math operation:"))
            if 1 <= math_operation_number <= 7:
                break
            else:
                print("Wrong value!")
        except ValueError:
            print("Wrong value, need a number!")

    a = b = None

    while True:  # input arguments and check value exceptions
        try:
            if 1 <= math_operation_number <= 6:
                if not a:
                    a = int(input("Enter first number:"))
                if not b:
                    b = int(input("Enter second number:"))
            elif 6 < math_operation_number < 8:
                a = int(input("Enter first number:"))
            break
        except ValueError:
            print("Wrong value, need a number!")
            continue

    # compare math input answers and call functions
    if math_operation_number == 1:
        addition_nums(a, b)
    elif math_operation_number == 2:
        subtraction_nums(a, b)
    elif math_operation_number == 3:
        multiplication_nums(a, b)
    elif math_operation_number == 4:
        division_nums(a, b)
    elif math_operation_number == 5:
        exponentiation_nums(a, b)
    elif math_operation_number == 6:
        square_root_nums(a)
    elif math_operation_number == 7:
        cube_root_nums(a)

    # repeat or break the program
    answer = input("\nEnter 'stop' if you wont break or continue:")
    if answer == "stop":
        break

print("---------Programm stop----------")

# Можна було ще закоментувати деякі дії в циклі, однак вони дуже прості.
# Використав калькулятор з завдання 8_3.
# В інженерному калькуляторі більше математичних операцій,
# однак суть від цього не змінюється).
