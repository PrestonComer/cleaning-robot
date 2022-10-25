from random import randint

DIRECTIONS = {
    "Up" : (-1, 0),
    "Right" : (0, 1),
    "Down" : (1, 0),
    "Left" : (0, -1)
}

POSSIBLEFINDS = ["Clean", "Robot", "Dirt", "Object"]

class environment:
    def __init__(self, numRows, numCols, robotLocation=(0,0), cleanLocations=[], 
                objectLocations=[]):
        self.numRows = numRows
        self.numCols = numCols
        self.robotLocation = robotLocation

        # Setup the environment where it is all dirty
        self.env = []
        for r in range(self.numRows):
            row = []
            for c in range(self.numCols):
                row.append("Dirt")
            self.env.append(row)

        # Remove the spots designated as not dirty
        for locRow, locCol in cleanLocations:
            self.env[locRow][locCol] = "Clean"
        for locRow, locCol in objectLocations:
            self.env[locRow][locCol] = "Object"

        # If the robot finds an Object randomly move it.
        # If you fail to move the robot 10 times then give an error asking the
        # user to please try and enter a better starting location
        if self.env[self.robotLocation[0]][self.robotLocation[1]] == "Object":
            randRow = randint(0, numRows - 1)
            randCol = randint(0, numCols - 1)
            unluckyRobot = 0
            while self.env[randRow][randCol] == "Object" and unluckyRobot < 10:
                unluckyRobot += 1
                randRow = randint(0, numRows - 1)
                randCol = randint(0, numCols - 1)
            if unluckyRobot >= 10:
                raise ValueError("Please Pick A Valid Robot Starting Location!")
            self.env[randRow][randCol] = "Robot"
        else:
            self.env[robotLocation[0]][robotLocation[1]] = "Robot"

    def setLocation(self, location, find):
        self.env[location[0]][location[1]] = find

    # Given a location check to see if that location is in bounds of the env
    # True means that it is, False means that it is not
    def inBounds(self, location):
        row, col = location
        if row < 0 or col < 0:
            return False
        if row >= self.numRows or col >= self.numCols:
            return False
        return True

    # Given a location check to see what is at that location. Assumes that the 
    # location given is in bounds of the environment
    def checkLocation(self, location):
        return self.env[location[0]][location[1]]

    # Print the environment where (0, 0) is in the top left
    def displayEnvironment(self):
        print()
        for row in self.env:
            print(row)

    def allClean(self):
        for row in self.env:
            if row.count("Dirt") != 0:
                return False
        return True

    def moveRobot(self, direction):
        if not direction in DIRECTIONS:
            raise ValueError("Improper Direction Entered")

        (robotLocRow, robotLocCol) = self.robotLocation
        (movementRow, movementCol) = DIRECTIONS[direction]
        newLocation = (robotLocRow + movementRow, robotLocCol + movementCol)

        # the place the robot is moving has to be inbounds and not blocked
        if not self.inBounds(newLocation):
            return
        if self.checkLocation(newLocation) == "Object":
            return

        self.env[self.robotLocation[0]][self.robotLocation[1]] = "Clean"
        self.robotLocation = newLocation
        self.env[newLocation[0]][newLocation[1]] = "Robot"