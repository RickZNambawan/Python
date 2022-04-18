print("Temperature Conversion Program")

print("Choose what you want to convert:")
print("[1] Kelvin to Fahrenheit")
print("[2] Fahrenheit to Kelvin")
print("[3] Kelvin to Celsius")
print("[4] Celsius to Kelvin")
print("[5] Fahrenheit to Celsius")
print("[6] Celsius to Fahrenheit")

option = int(input("\nEnter your Option: "))

# Kelvin to Fahrenheit
if option == 1:
    kelvin = float(input("\nEnter a Kelvin: "))
    fahrenheit = 1.8 * (kelvin - 273) + 32
    print("The Conversion of your Kelvin to Fahrenheit is {:.2f}".format(fahrenheit))

# Fahrenheit to Kelvin
elif option == 2:
    fahrenheit = float(input("\nEnter a Fahrenheit: "))
    kelvin = (fahrenheit + 459.67) * (5/9)
    print("The Conversion of your Fahrenheit to Kelvin is {:.2f}".format(kelvin))

# Kelvin to Celsius
elif option == 3:
    kelvin = float(input("\nEnter a Kelvin: "))
    celsius = kelvin - 273
    print("The Conversion of your Kelvin to Celsius is {:.2f}".format(celsius))

# Celsius to Kelvin
elif option == 4:
    celsius = float(input("\nEnter a Celsius: "))
    kelvin = celsius + 273
    print("The Conversion of your Celsius to Kelvin is {:.2f}".format(kelvin))

# Fahrenheit to Celsius
elif option == 5:
    fahrenheit = float(input("\nEnter a Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5/9)
    print("The Conversion of your Fahrenheit to Celsius is {:.2f}".format(celsius))

# Celsius to Fahrenheit
elif option == 6:
    celsius = float(input("\nEnter a Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("The Conversion of your Celsius to Fahrenheit is {:.2f}".format(fahrenheit))
else:
    print("\nInvalid Option.")