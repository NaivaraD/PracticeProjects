import sys

def chains():
    while True:
        multiple = int(input("What is the multiple of your pattern: "))
        nMultRepeat = int(input("What is your turning chain: "))
        border = int(input("How many total stitches in your border: "))
        repeats = int(input("How many repeats might you want: "))
        
        test = (multiple*repeats)+nMultRepeat+border
        
        print(f"You want to chain {test} stitches!")

        leave = input('would you like to use this calculator again? Y/N: ').lower()

        if leave == 'n':
            break

def castOn():
    while True:
        multiple = int(input("What is the multiple of your pattern: "))
        nMultRepeat = int(input("What is your buffer number: "))
        border = int(input("How many total stitches in your border: "))
        repeats = int(input("How many repeats might you want: "))

        test = (multiple*repeats)+nMultRepeat+border

        print(f"You want to cast on {test} stitches!")

        leave = input('would you like to use this calculator again? Y/N: ').lower()

        if leave == 'n':
            break

def yardage():
    while True:
        bundleSize = input("How many strands in your bundles (defaults to 25): ")
        bundles = input("How many full bundles: ")
        bonusBundle = input("How many strands in your spare bundle: ")
        yards = input("How many yards is your niddy noddy set to (defaults to 2): ")

        if bundleSize == '':
            bundleSize = 25

        if yards == '':
            yards = 2

        bundleSize = int(bundleSize)
        bundles = int(bundles)
        bonusBundle = int(bonusBundle)
        if '.' in yards:
            yards = float(yards)

        else:
            yards = int(yards)

        test = ((bundleSize*bundles)+bonusBundle)*yards

        print(f"You have ~{test} yards!")

        leave = input('would you like to use this calculator again? Y/N: ').lower()

        if leave == 'n':
            break

choice = input('''Welcome to Navi's Fiber Calculator!
I presently have three calculators made, those being:
[Crochet]: To calculate how many chains when making an item from a repeating stitch.
[Knit]: Same as crochet, but for casting on.
[Spinning]: To calculate the yardage you have on your niddy noddy.
[Exit]: Not a calc, but an easy exit to the program.
Please pick C/K/S/E and enjoy not doing as much math!
=> ''').lower()

while True:
    if choice == 'c' or choice == 'crochet':
        chains()

    if choice == 'k' or choice == 'knit':
        castOn()

    if choice == 's' or choice == 'spinning':
        yardage()

    if choice == 'e' or choice == 'exit':
        sys.exit()

    choice = input("C/K/S/E: ").lower()