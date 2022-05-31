#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str1 = 'Last digit of'
str2 = 'and is greater than'
str3 = 'and is less than'

int_2_str = str(number)
_len = len(int_2_str)
index = _len - 1
last_digit = int(int_2_str[index])

def app():
    if last_digit > 5:
        print(f"{str1} {number} is {last_digit} {str2} 5")
    elif last_digit == 0:
        print(f"{str1} {number} is {last_digit} and is 0")
    elif last_digit < 6 and last_digit != 0:
        print(f"{str1} {number} is {last_digit} {str3} 6 and not 0")
    else:
        app()
        

app()
