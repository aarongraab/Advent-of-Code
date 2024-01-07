REDLIMIT = 12
GREENLIMIT = 13
BLUELIMIT = 14
gameBool = True
gameNumberTotal = 0

def doCalc(cubes):
    coloursSplit = cubes.split(",")
    for i in coloursSplit:
        i.rstrip(",")
        i.strip(" ")
        myColour = i.split()
        if myColour[1] == "red":
            if int(myColour[0]) > REDLIMIT:
                return False
        if myColour[1] == "green":
            if int(myColour[0]) > GREENLIMIT:
                return False
        if myColour[1] == "blue":
            if int(myColour[0]) > BLUELIMIT:
                return False
        else:
            return True

with open('input.txt', 'r') as file:
    for line in file:
        myStringSplit = line.split(maxsplit=2)
        gameNumber = myStringSplit[1].rstrip(":")
        cubeList = myStringSplit[2].split(";")
        for cubes in cubeList:
            gameBool = doCalc(cubes)
        if gameBool:
            gameNumberTotal += int(gameNumber)

print("Game Number Total is:", gameNumberTotal)