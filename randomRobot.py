from environment import *
from random import choice
from json import dumps

class randomRobot:
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

    def moveInformation(self, shouldPrint=False):
        if shouldPrint:
            print(f"\nTotal Moves: {self.totalMoves}")
            print(f"Moves Up: {self.moveCounters['Up']}")
            print(f"Moves Right: {self.moveCounters['Right']}")
            print(f"Moves Down: {self.moveCounters['Down']}")
            print(f"Moves Left: {self.moveCounters['Left']}")
        return (self.totalMoves, self.moveCounters)

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