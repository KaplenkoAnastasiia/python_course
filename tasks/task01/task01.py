print("narcissistic numbers from 1 to 1000")
min_value = 1
max_value = 1000


def count_number_of_digit(number):
    count = 0
    while number:
        number //= 10
        count += 1
    return count


def is_narcissistic(number):
    if number < 0:
        return False

    original = number
    sum = 0
    count = count_number_of_digit(number)
    while number:
        digit = number % 10
        sum += digit**count
        number //= 10
    return sum == original


for n in range(min_value, max_value):
    if is_narcissistic(n):
        print(n, end=' ')
