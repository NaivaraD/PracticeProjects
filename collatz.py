import time, sys

try:

    numIn = int(input("Give me a number please: "))

    print('▉' * numIn, end=' - ')
    print(numIn)

    while numIn != 1:
        if numIn % 2 == 0:
            numIn = numIn // 2
            print('▉' * numIn, end=' - ')
            print(numIn)
            time.sleep(0.1)
        
        elif numIn % 2 == 1:
            numIn = 3 * numIn + 1
            print('▉' * numIn, end=' - ')
            print(numIn)
            time.sleep(0.1)

        else:
            print('wat?')

except KeyboardInterrupt:
    sys.exit()

except ValueError:
    print("That was not a number, goodbye")
    time.sleep(0.5)
    sys.exit