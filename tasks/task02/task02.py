import math

msg1 = "Enter base and height:"
msg2 = "Enter 2 sides and angle(degrees) between them:"
msg3 = "Goodbye!"


def run_menu():
    print("Welcome to the triangle area calculation tool.")
    while True:
        print("\n Menu:", "1. Calculate triangle area by base and height",
              "2. Calculate triangle area by 2 sides and angle between them",
              "3. Exit", sep="\n")
        user_string = input("Enter menu item number:")
        if user_string.count == 0:
            continue
        if user_string == '1':
            print(msg1)
            calculate_area_by_height(input())
            continue
        if user_string == '2':
            print(msg2)
            calculate_area_by_angle(input())
            continue
        if user_string == '3':
            print(msg3)
            break
        continue


def calculate_area_by_height(userString):
    values = userString.split(" ")
    if values.__len__() != 2:
        print("incorrect values or amount of them")
        return
    base, height = values
    base = int(base)
    height = int(height)
    area = (base*height)/2
    print(f'Area is: {area: .2f}')


def calculate_area_by_angle(userString):
    values = userString.split(" ")
    if values.__len__() != 3:
        print('incorrect values or amount of them')
        return
    side1, side2, angle = values
    side1 = int(side1)
    side2 = int(side2)
    angle = int(angle)
    radians = math.radians(angle)
    area = math.sin(radians)*(side1*side2)/2
    print(f'Area is: {area: .3f}')


run_menu()
