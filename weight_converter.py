import tkinter as tk

# Color palette options
# https://coolors.co/ffc233-2a324b-767b91-c7ccdb-e1e5ee
# https://coolors.co/ffc233-dd614a-ddfff7-f48668-2b3d41

# Mass units 
massUnits = {
    "Kilogram":1000.0,
    "Gram": 1.0,
    "Milligram": 0.001,
    "Pound": 454,
    "Ounce": 28.3495
}

# Length units
lengthUnits = {
    "Kilometer": 1000,
    "Meter": 1.0,
    "Centimeter": .01,
    "Millimeter": .001,
    "Mile": 1609.340,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254
}

# Temperature units
tempUnits = {
    "Celsius":0,
    "Farenheit":1,
    "Kelvin":2
}

# Types of units
categories = {
    "Mass": massUnits,
    "Length": lengthUnits,
    "Temperature": tempUnits
}

def convertTemp(val, u0, u1):
    if u0 == u1:
        return
    if u0 == "Celsius":
        if u1 == "Farenheit":
            return (val * (9/5)) + 32
        if u1 == "Kelvin":
            return val + 273.15
    if u0 == "Farenheit":
        if u1 == "Celsius":
            return (val - 32) * (5/9)
        if u1 == "Kelvin":
            return ((val - 32) * (5/9)) + 273.15
    if u0 == "Kelvin":
        if u1 == "Celsius":
            return val - 273.15
        if u1 == "Farenheit":
            return ((val - 273.15) * (9/5)) + 32


def convertUnits(event=None):
    val = float(value1.get())
    unit0 = chosenUnit1.get()
    unit1 = chosenUnit2.get()
    category = chosenCat.get()
    if category == "Temperature":
        value2.set(str(convertTemp(val, unit0, unit1)))
        return
    units = categories[category]
    convertedVal = val*units.get(unit0)/units.get(unit1)
    value2.set(str(convertedVal))


def selected(event):
    
    new_choices = None
    currentCat = chosenCat.get()
    lst0 = list(categories[currentCat])
    chosenUnit1.set(lst0[0])
    unitMenu1['menu'].delete(0, 'end')

    chosenUnit2.set(lst0[1])
    unitMenu2['menu'].delete(0, 'end')

    new_choices = categories[currentCat]

    for choice in new_choices:
        unitMenu1['menu'].add_command(label=choice, command=lambda c=choice: chosenUnit1.set(c))
        unitMenu2['menu'].add_command(label=choice, command=lambda c=choice: chosenUnit2.set(c))
        
    convertUnits()
    
def switchIfSame(event):
    cat0 = chosenUnit1.get()
    cat1 = chosenUnit2.get()
    if chosenUnit1.get() == cat1:
        chosenUnit1.set(cat1)
        chosenUnit2.set(cat0)
    if chosenUnit2.get() == cat0:
        chosenUnit1.set(cat0)
        chosenUnit2.set(cat1)


# Window setup
mainWindow = tk.Tk()
mainWindow.geometry("300x220")
mainWindow.title("Unit Converter by Iz")
mainWindow.configure(background="#2c4e8a")


mainWindow.bind('<Return>', lambda event: convertUnits())

# Contents of primary dropdown menu
chosenCat = tk.StringVar()
chosenCat.set("Mass")


# Create primary dropdown menu
categoriesMenu = tk.OptionMenu(mainWindow, chosenCat, *categories, command=selected)
categoriesMenu.pack(pady=20)

massU = list(massUnits.keys())
# Contents of unit dropdown menu #1
chosenUnit1 = tk.StringVar()
chosenUnit1.set(massU[0])

# Contents of unit dropdown menu #2
chosenUnit2 = tk.StringVar()
chosenUnit2.set(massU[1])


value1 = tk.StringVar()
value1.set(str(0))
entryBox1 = tk.Entry(mainWindow, textvariable=value1, width=10, bg="white")
entryBox1.pack()
# Create dropdown menu #1 for unit
unitMenu1 = tk.OptionMenu(mainWindow, chosenUnit1, *massUnits, command=convertUnits)
unitMenu1.pack(pady=5)

value2 = tk.StringVar()
value2.set(str(0))

entryBox2 = tk.Entry(mainWindow, textvariable=value2, width=10, bg="white")
entryBox2.pack()

# Create dropdown menu #2 for unit
unitMenu2 = tk.OptionMenu(mainWindow, chosenUnit2, *massUnits, command=convertUnits)
unitMenu2.pack(pady=5)

convertButton = tk.Button(mainWindow, text='Convert', command=convertUnits, width=5)
convertButton.pack()



mainWindow.mainloop()