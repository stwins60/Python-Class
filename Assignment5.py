# Declaring a variable
options = ''  # declariing an empty string

# Display the options
while options != "Q":

    # Ask user for options
    options = input("Enter the options [P, C, F, M, KM, In, CM, Q]? ")
    print()

    if options == "P":
        print("[P] Print Options")
        print("[C] Convert from Celsius")
        print("[F] Convert from Fahrenheit")
        print("[M] Convert from Miles")
        print("[KM] Convert from Kilometers")
        print("[In] Convert from Inches")
        print("[CM] Convert from Centimeters")
        print("[Q] Quit")

        print()
    elif options == "C":
        # Convert from celsius to fahrenheit
        celsius = int(input("Celsius temperature: "))
        temp = (celsius * 1.8) + 32
        print('Fahrenheit: ' + str(temp))
        print()
    elif options == "F":
        # Convert from fahrenheit to celsius
        fahrenheit = int(input("Fahrenheit temperature: "))
        temp = (fahrenheit - 32) * 0.55
        print('Celsius: ' + str(temp))
        print()
    elif options == "M":
        # Convert Miles to kilometers
        miles = float(input("Miles: "))
        kilometer = miles * 1.609344
        print("Kilometers: " + str(kilometer))
        print()
    elif options == "KM":
        # Convert kilometers to Miles
        kilometers = float(input("Kilometers: "))
        miles = (kilometers * 0.621371)
        print("Miles: " + str(miles))
        print()
    elif options == "In":
        # Convert Inches to Centimeters
        inches = float(input("Inches: "))
        centimeters = inches * 2.54
        print("Centimeters: " + str(centimeters))
        print()
    elif options == "CM":
        # Convert Centimeters to Inches
        centimeters = float(input("Centimeters: "))
        inches = centimeters / 2.54
        print("Inches: " + str(inches))
        print()
    else:
        print("Invalid input!!!")
        print()
