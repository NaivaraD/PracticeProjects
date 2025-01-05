# import hesitation and death
import time, sys

# error handling, see exceptions
try:

    # receive a number (hopefully)
    numIn = int(input("Give me a number please: "))

    # print the first number with an amount of blocks equal to it
    print(numIn, end=' - ')
    print('▉' * numIn)

    # check if number is 1
    while numIn != 1:
        # check if number is even
        if numIn % 2 == 0:
            # floor divide in half
            numIn = numIn // 2
            # print number with an amount of blocks equal to it then pause for 1/10 of a second
            print(numIn, end=' - ')
            print('▉' * numIn)
            time.sleep(0.1)
        
        # check if number is odd (just for fun)
        elif numIn % 2 == 1:
            # multiply number by 3, then add 1
            numIn = 3 * numIn + 1
            # print number with an amount of blocks equal to it then pause for 1/10 of a second
            print(numIn, end=' - ')
            print('▉' * numIn)
            time.sleep(0.1)

        # should be impossible, but otherwise say what?
        else:
            print('wat?')

# emergency terminate if the program is going too long (ctrl+c)
except KeyboardInterrupt:
    sys.exit()

# terminate if user did not enter a numeric number
except ValueError:
    print("That was not a number, goodbye")
    time.sleep(0.5)
    sys.exit()