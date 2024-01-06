REDLIMIT = 12
GREENLIMIT = 13
BLUELIMIT = 14
gameNumberTotal = 0

myString = "Game 1: 4 red, 5 blue, 9 green; 7 green, 7 blue, 3 red; 16 red, 7 blue, 3 green; 11 green, 11 blue, 6 red; 12 red, 14 blue"

myStringSplit = myString.split(maxsplit=2)
gameNumber = myStringSplit[1].rstrip(":")
cubeList = myStringSplit[2].split(";")
for cubes in cubeList:
    coloursSplit = cubes.split(",")
    for i in coloursSplit:
        i.rstrip(",")
        i.strip(" ")
        myColour = i.split()
        print(myColour)
        print("0:", myColour[0], "\n1:", myColour[1])

    '''
            if myColour[1] == "red":
                if int(myColour[0]) <= REDLIMIT:
                    gameNumberTotal += int(gameNumber)
            if myColour[1] == "green":
                if int(myColour[0]) <= GREENLIMIT:
                    gameNumberTotal += int(gameNumber)
            if myColour[1] == "blue":
                if int(myColour[0]) <= BLUELIMIT:
                    gameNumberTotal += int(gameNumber)
            else:
                print("ERROR")
'''

print("Game Number Total is:", gameNumberTotal)