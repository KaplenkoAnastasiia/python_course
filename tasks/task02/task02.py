import math

msg1 = "Enter base and height:"
msg2 = "Enter 2 sides and angle(degrees) between them:"
msg3 = "Goodbye!"
welcomeMsg = "Welcome to the triangle area calculation tool."
menuItems=  f"""\nMenu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit"""

def run_menu():
    print(welcomeMsg)
    user_string = 0
    while user_string != '3':
        print(menuItems, sep="\n")
        user_string = input("Enter menu item number:")
        if user_string == '1':
            print(msg1)
            calculate_area_by_height(input())
            continue
        if user_string == '2':
            print(msg2)
            calculate_area_by_angle(input())
            continue
        continue


def calculate_area_by_height(user_string):
    values = user_string.split(" ")
    if len(values) != 2 or invalid_numbers(values):
        print("incorrect values or amount of them")
        return
    base, height = values
    base = int(base)
    height = int(height)
    area = (base*height)/2
    print(f'Area is: {area: .2f}')


def calculate_area_by_angle(userString):
    values = userString.split(" ")
    if len(values) != 3 or invalid_numbers(values):
        print('incorrect values or amount of them')
        return
    side1, side2, angle = values
    side1 = int(side1)
    side2 = int(side2)
    angle = int(angle)
    radians = math.radians(angle)
    area = math.sin(radians)*(side1*side2)/2
    print(f'Area is: {area: .3f}')

def invalid_numbers(values):
  for num in values:
    if(not type(int) or not math.isnan(int(num)) or int(num) <= 0):
      return True
  return False

run_menu()