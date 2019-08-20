#!/usr/bin/python3

while True:
    try:
        print('Lets div x by y!')

        x = int(input('What is the value of x? '))
        y = int(input('What is the value of y? '))

        print('The value of x/y is:', x/y)
    except ZeroDivisionError:
        print('Something went wrong with those maths... restarting')
    except ValueError:
        print("You seem to be giving us a non numeric value. Try again.")
    except Exception as err:
        print(err)
