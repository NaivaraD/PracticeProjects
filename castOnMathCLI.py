import sys

def chains():
    multiple = int(input("What is the multiple of your pattern: "))
    nMultRepeat = int(input("What is your turning chain: "))
    border = int(input("How many total stitches in your border: "))
    repeats = int(input("How many repeats might you want: "))
    
    test = (multiple*repeats)+nMultRepeat+border
    
    print(f"You want to chain {test} stitches!")

def castOn():
    multiple = int(input("What is the multiple of your pattern: "))
    nMultRepeat = int(input("What is your buffer number: "))
    border = int(input("How many total stitches in your border: "))
    repeats = int(input("How many repeats might you want: "))

    test = (multiple*repeats)+nMultRepeat+border

    print(f"You want to cast on {test} stitches!")

def yardage():
    bundleSize = int(input("How many strands in your bundles: "))
    bundles = int(input("How many full bundles: "))
    bonusBundle = int(input("How many strands in your spare bundle: "))
    yards = int(input("How many yards is your niddy noddy set to: "))

    test = ((bundleSize*bundles)+bonusBundle)*yards

    print(f"You have ~{test} yards!")

choice = input('''Welcome to Navi's Fiber Calculator!
I presently have three calculators made, those being:
[Crochet]: To calculate how many chains when making an item from a repeating stitch.
[Knit]: Same as crochet, but for casting on.
[Spinning]: To calculate the yardage you have on your niddy noddy.
Please pick C/K/S and enjoy not doing as much math!
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

    response = input("Would you like exit? Y/N: ").upper()

    if response == "Y":
        sys.exit()

    choice = input("c/k/s/e: ").lower()