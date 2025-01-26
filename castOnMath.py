import sys

while True:
    multiple = int(input("What is your multiple: "))
    nMultRepeat = int(input("What is your buffer number: "))
    border = int(input("How many total stitches in your border: "))
    repeats = int(input("How many repeats might you want: "))
    increase = multiple

    for i in range(repeats-1):
        multiple = multiple+increase

    print("You want to cast on/chain " + str(multiple+nMultRepeat+border) + " stitches!")

    response = input("Would you like exit? Y/N: ").upper()

    if response == "Y":
        sys.exit()