#!/usr/bin/env python3


def happy_new_year():
    # code goes here!
    coundown = 10
    while coundown >= 1:
        print(coundown)
        coundown -= 1
        print("Happy New Year!")


def square_integers(numbers):
    # code goes here!
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num**2)
    return squared_numbers


def fizzbuzz():
    # code goes here!
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)
