import random

DIRECTIONS = {
    "Up" : (-1, 0),
    "Right" : (0, 1),
    "Down" : (1, 0),
    "Left" : (0, -1)
}

POSSIBLEFINDS = ["Empty", "Robot", "Dirt", "Blocked"]

class environment:
    def __init__(self, numRows, numCols, robotLocation, cleanLocations=[], 
                blockedLocations=[]):
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
        for locRow, locCol in blockedLocations:
            self.env[locRow][locCol] = "Blocked"

        # If the robot is blocked randomly move it.
        # If you fail to move the robot 10 times then give an error asking the
        # user to please try and enter a better starting location
        if self.env[self.robotLocation[0]][self.robotLocation[1]] == "Blocked":
            randRow = random.randint(0, numRows - 1)
            randCol = random.randint(0, numCols - 1)
            unluckyRobot = 0
            while self.env[randRow][randCol] == "Blocked" and unluckyRobot < 10:
                unluckyRobot += 1
                randRow = random.randint(0, numRows - 1)
                randCol = random.randint(0, numCols - 1)
            if unluckyRobot >= 10:
                raise ValueError("Please Pick A Valid Robot Starting Location!")
            self.env[randRow][randCol] = "Robot"

    def setLocation(self, location, find):
        self.env[location[0]][location[1]] = find

    # Given a location check to see if that location is in bounds of the env
    # True means that it is, False means that it is not
    def inBounds(self, location):
        row, col = location
        if row <= 0 and col <= 0:
            return False
        if row >= self.numRows and col >= self.numCols:
            return False
        return True

    def moveRobot(self, direction):
        pass