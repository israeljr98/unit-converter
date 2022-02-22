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
    "Kilometer",
    "Meter",
    "Centimeter",
    "Millimeter",
    "Mile",
    "Yard",
    "Foot",
    "Inch"
}

# Temperature units
tempUnits = {
    "Celsius",
    "Farenheit",
    "Kelvin"
}

# Types of units
categories = {
    "Mass": massUnits,
    "Length": lengthUnits,
    "Temperature": tempUnits
}

def convertUnits(val, unit0, unit1, category):
    units = categories[category]
    return val*units[unit0]/units[unit1]
