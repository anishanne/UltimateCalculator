
import os
import sys
from math import pi

ValueErrorMSG = "Input value can only be an Integer or a Float!"


def square_area():
    try:
        r = float(input("Radius: "))
        calc_value = r ** 2 * pi
        print("Output:", calc_value)
    except ValueError:
        print(ValueErrorMSG)


def circle_area():
    try:
        w = float(input("Width: "))
        h = float(input("Height: "))
        calc_value = w * h / 2
        print("Output:", calc_value)
    except ValueError:
        print(ValueErrorMSG)


def triangle_area():
    try:
        w = float(input("Width: "))
        h = float(input("Height: "))
        calc_value = w * h
        print("Output:", calc_value)
    except ValueError:
        print(ValueErrorMSG)


def rectangle_area():
    try:
        s = float(input("Sides: "))
        calc_value = s * s * s * s
        print("Output:", calc_value)
    except ValueError:
        print(ValueErrorMSG)


def celsius_fahrenheit():
    try:
        C = float(input("Celsius: "))
        calc_value = C * 9 / 5 + 32
        print("Output:", calc_value)
    except ValueError:
        print(ValueErrorMSG)


def fahrenheit_celsius():
    try:
        E = float(input("Fahrenheit: "))
        f = (E - 32) * 5 / 9
        print("Output:", f)
    except ValueError:
        print(ValueErrorMSG)


def exec_menu(choice):
    menu_actions = {
        '1': square_area,
        '2': circle_area,
        '3': triangle_area,
        '4': rectangle_area,
        '5': celsius_fahrenheit,
        '6': fahrenheit_celsius
    }
    os.system('clear')
    if choice == '':
        return
    else:
        try:
            menu_actions[choice]()
            input("Press `Enter Key` to continue...")
        except KeyError:
            print("Invalid selection for '" + choice + "', please try again.\n")
            input("Press `Enter Key` to continue...")
            return


def main_menu():
    running = True
    while (running==True):
        os.system('clear')
        print("Please choose the type of calculation you want to start:")
        print("1) Square Area Calculator")
        print("2) Circle Area Calculator")
        print("3) Triangle Area Calculator")
        print("4) Rectangle Area Calculator")
        print("5) Celsius to Fahrenheit Calculator")
        print("6) Fahrenheit to Celsius Calculator")
        print("\n0. Quit")

        choice = input("What type of calculator do you want to use?: ")

        if choice == "0":
            running = False;
        else:
            exec_menu(choice)

    print("Exiting...")
    sys.exit()


if __name__ == "__main__":
    main_menu()
