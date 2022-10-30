from environment import *
from random import choice, randint
from json import dumps

POSSIBLEMETHODS = ["dirtFirst", "cyclicMovement", "random"]

class robot:
    def __init__(self, environment):
        self.env = environment
        self.totalMoves = 0
        self.moveCounters = {
            "Up" : 0,
            "Right" : 0,
            "Down" : 0,
            "Left" :0
        }
        self.moveList = []
        self.selectedMethod = choice(POSSIBLEMETHODS)

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

    # Method of cleaning such that the robot will clean first up then right then
    # down then left
    def cyclicMovement(self):
        pass

    def random(self):
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