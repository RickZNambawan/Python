print("Area or Perimeter Program\n")

length = float(input("Enter Length: "))

if length <= 0:
    print("Invalid Length.")
else:
    width = float(input("Enter Width: "))

    if width <= 0:
        print("Invalid Width.")
    else:
        print("\nSelect an Option:")
        print("[1] Area")
        print("[2] Perimeter")
        option = int(input("Enter your Option: "))

        if option == 1:
            area = length * width
            print("\nThe Area of the Rectangle is {:.2f}".format(area))
        elif option == 2:
            perimeter = (2 * length) + (2 * width)
            print("\nThe Perimeter of the Rectangle is {:.2f}".format(perimeter))
        else:
            print("Invalid Option")
