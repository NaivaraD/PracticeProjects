import tkinter as tk
from tkinter import ttk
import os.path

image = 'yarrrn.ico'
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, image)

# Functions
def theMath(multiple, nMultRepeat, border, repeats):
    increase = multiple

    for i in range(repeats-1):
        multiple = multiple+increase

    return(multiple+nMultRepeat+border)

# Build the window
window = tk.Tk()
window.title('Cast On Math')
window.iconbitmap(default = path)
window_width = 450
window_height = 200
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')
window.minsize(450, 200)

# Title Label
title = ttk.Label(
    window,
    text = 'Cast On Math',
    font = 'Calibri 24'
    )
title.pack()

# Multiples
multipleInt = tk.IntVar(value = 1)
multipleFrame = ttk.Frame(window)
multipleLabel = ttk.Label(
    multipleFrame,
    text = 'What is your multiple?',
    font = 'Calibri 12'
    )
multiplespin = ttk.Spinbox(
    multipleFrame,
    from_ = 1,
    to = 50,
    textvariable = multipleInt
    )
multipleLabel.pack(side = 'left', padx = 5)
multiplespin.pack(side = 'left', padx = 5)
multipleFrame.pack()

# Non-Multiple Repeats
nMultInt = tk.IntVar(value = 1)
nMultFrame = ttk.Frame(window)
nMultLabel = ttk.Label(
    nMultFrame,
    text = 'What is your buffer number/turning chain?',
    font = 'Calibri 12'
    )
nMultspin = ttk.Spinbox(
    nMultFrame,
    from_ = 1,
    to = 50,
    textvariable = nMultInt
    )
nMultLabel.pack(side = 'left', padx = 5)
nMultspin.pack(side = 'left', padx = 5)
nMultFrame.pack()

# Border
borderInt = tk.IntVar(value = 1)
borderFrame = ttk.Frame(window)
borderLabel = ttk.Label(
    borderFrame,
    text = 'How many total stitches in your border?',
    font = 'Calibri 12'
    )
borderspin = ttk.Spinbox(
    borderFrame,
    from_ = 1,
    to = 50,
    textvariable = borderInt
    )
borderLabel.pack(side = 'left', padx = 5)
borderspin.pack(side = 'left', padx = 5)
borderFrame.pack()

# Repeats
repeatInt = tk.IntVar(value = 1)
repeatFrame = ttk.Frame(window)
repeatLabel = ttk.Label(
    repeatFrame,
    text = 'How many repeats might you want?',
    font = 'Calibri 12'
    )
repeatspin = ttk.Spinbox(
    repeatFrame,
    from_ = 1,
    to = 100,
    textvariable = repeatInt
    )
repeatLabel.pack(side = 'left', padx = 5)
repeatspin.pack(side = 'left', padx = 5)
repeatFrame.pack()

# General Output
mathButton = ttk.Button(
    window,
    text = 'Do the Math!',
    command = lambda: outputLabel.configure(text = f'You want to cast on/chain {theMath(multipleInt.get(), nMultInt.get(), borderInt.get(), repeatInt.get())}')
    )
mathButton.pack()
#outputFrame = ttk.Frame(window, relief = GROOVE)
outputLabel = ttk.Label(window, text = 'Change the Numbers and Press the Button!', font = 'Calibri 17', relief = tk.GROOVE)
outputLabel.pack()
#outputFrame.pack()

window.mainloop()