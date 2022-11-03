from environment import *
from random import choice, randint
from json import dumps

POSSIBLEMETHODS = ["dirtFirst", "percentageMove"]

class robot:
    def __init__(self, environment, cleaningMethod):
        self.env = environment
        self.method = cleaningMethod
        self.movementChances = {
            "Up" : randint(1,25),
            "Right" : randint(1,25),
            "Down" : randint(1,25),
            "Left" : randint(1,25)
        }

        self.totalMoves = 0
        self.moveCounters = {
            "Up" : 0,
            "Right" : 0,
            "Down" : 0,
            "Left" :0
        }
        self.moveList = []

    def mutateMovementChances(self):
        chanceLeft = 100
        newChance = [0,0,0,0]
        indexToChange = 0

        while chanceLeft > 0:
            indexToChange = indexToChange % 4
            randomChance = randint(0, chanceLeft)
            chanceLeft -= randomChance
            newChance[indexToChange] += randomChance
            indexToChange += 1

        self.movementChances = {
            "Up" : newChance[0],
            "Right" : newChance[1],
            "Down" : newChance[2],
            "Left" : newChance[3]
        }

    # Method of cleaning such that the robot will look in the possible directions
    # and upon finding a piece of dirt it will move there updating records along the way
    def dirtFirst(self):
        while not self.env.allClean():
            # Create static list that is possible to reduce per move
            choicesLeft = list(DIRECTIONS)

            while True:
                # Grab one of the directions that can be moved
                moveChoice = choice(choicesLeft)

                # The location is valid but not dirty
                possibleRandomMoves = []

                # Calculate the location if the robot was to move in chosen direction
                (robotLocRow, robotLocCol) = self.env.robotLocation
                (movementRow, movementCol) = moveChoice
                newLocation = (robotLocRow + movementRow, robotLocCol + movementCol)

                # remove the chosen direction from the list
                choicesLeft.remove(moveChoice)

                # make sure that the move is inBounds
                if self.env.inBounds(newLocation):
                    # whenever we see dirt the robot will clean it
                    if self.env.checkLocation(newLocation) == "Dirt":
                        self.env.moveRobot(moveChoice)
                        self.totalMoves += 1
                        self.moveCounters[moveChoice] += 1
                        break
                    # if the robot sees a clean spot it remembers that it can 
                    # move there and then looks for more dirt
                    if self.env.checkLocation(newLocation) == "Clean":
                        possibleRandomMoves.append(moveChoice)
                # none of the spaces were dirty so randomly move to one of the clean ones
                if len(choicesLeft) == 0:
                    moveChoice = choice(possibleRandomMoves)
                    self.env.moveRobot(moveChoice)
                    self.totalMoves += 1
                    self.moveCounters[moveChoice] += 1
                    break

    def percentageMove(self):
        pass

    def cleanEnvironment(self):
        # print("\nStarting Environment:", end="")
        # self.env.displayEnvironment()

        while not self.env.allClean():
            moveChoice = choice(list(DIRECTIONS))

            self.moveCounters[moveChoice] += 1
            self.totalMoves += 1

            self.env.moveRobot(moveChoice)
            # print("\nMove " + str(self.totalMoves) + " - " + moveChoice + ":", end="")
            # self.env.displayEnvironment()

            self.moveList.append(moveChoice)

        # print("\nEnvironment All Clean!", end="")
        # self.env.displayEnvironment()
        # self.moveInformation(True)