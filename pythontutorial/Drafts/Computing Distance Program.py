listOfCity = ["Disneyland", "Enchanted Kingdom", "Cloud9", "Araneta Coliseum"]

distanceBetween = [[25, 50, 75, 100], [50, 75, 100, 25], [75, 100, 25, 50], [100, 25, 50, 75]]


cityMenu1 = int(input("""
Please choose a city by typing a number:
0.) Disneyland
1.) Enchanted Kingdom
2.) Cloud9
3.) Araneta Coliseum
"""))

cityMenu2 = int(input("""
Choose another city:
0.) Disneyland
1.) Enchanted Kingdom
2.) Cloud9
3.) Araneta Coliseum
"""))

def main():
    fromCity = cityMenu1
    toCity = cityMenu2
    result = distanceBetween[fromCity][toCity]

    print("The distance between " + listOfCity[fromCity] + " and " + listOfCity[toCity])
    print("is ", result, " miles motherfucker!")

main()
