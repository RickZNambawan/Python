print("Program: Cigarette Packing")

diameter = int(input("Enter diameter of cigarette: "))

if diameter <= 0 or diameter >= 3:
    print("Invalid Diameter.")
else:
    firstDimension = int(input("Enter Dimension Value 1: "))
    if firstDimension < diameter:
        print("Invalid Dimension 1.")
    else:
        secondDimension = int(input("Enter Dimension Value 2: "))
        if secondDimension < diameter:
            print("Invalid Dimension 2.")
        else:
            maxCigarettes = (firstDimension / diameter) * (secondDimension / diameter)
            print("Maximum Number of Cigarettes packed: {}".format(int(maxCigarettes)))