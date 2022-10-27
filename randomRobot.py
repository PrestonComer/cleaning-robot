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

# with open("results/randomResults.txt", "a") as f:
#     msg = "The Following Results Are Based On A {environmentSize} Environment With The Random Movement Cleaning Robot Positioned At {robotPosition}, Clean Position(s) At {cleanPositions}, And Object(s) At {blockedPositions}"
    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(0,0)", cleanPositions = "[]", blockedPositions = "[]"))
    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(2,2)", cleanPositions = "[]", blockedPositions = "[]"))
    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(4,4)", cleanPositions = "[]", blockedPositions = "[]"))

    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(0,0)", cleanPositions = "[(1,1)]", blockedPositions = "[]"))
    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(2,2)", cleanPositions = "[(1,1), (2,2)]", blockedPositions = "[]"))
    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(4,4)", cleanPositions = "[(1,1), (2,2), (3,3)]", blockedPositions = "[]"))

    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(0,0)", cleanPositions = "[]", blockedPositions = "[(1,1)]"))
    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(2,2)", cleanPositions = "[]", blockedPositions = "[(1,1), (2,2)]"))
    # f.write(msg.format(environmentSize = "5x5", robotPosition = "(4,4)", cleanPositions = "[]", blockedPositions = "[(1,1), (2,2), (3,3)]"))

    # f.write(msg.format(environmentSize = "10x10", robotPosition = "(0,0)", cleanPositions = "[]", blockedPositions = "[]"))
    # f.write(msg.format(environmentSize = "25x25", robotPosition = "(0,0)", cleanPositions = "[]", blockedPositions = "[]"))
    # f.write(msg.format(environmentSize = "50x50", robotPosition = "(0,0)", cleanPositions = "[]", blockedPositions = "[]"))

# for _ in range(100):
    # e = environment(5, 5, (0,0), [], [])
    # e = environment(5, 5, (2,2), [], [])
    # e = environment(5, 5, (4,4), [], [])

    # e = environment(5, 5, (0,0), [(1,1)], [])
    # e = environment(5, 5, (0,0), [(1,1), (2,2)], [])
    # e = environment(5, 5, (0,0), [(1,1), (2,2), (3,3)], [])

    # e = environment(5, 5, (0,0), [], [(1,1)])
    # e = environment(5, 5, (2,2), [], [(1,1), (2,2)])
    # e = environment(5, 5, (4,4), [], [(1,1), (2,2), (3,3)])

    # e = environment(10, 10, (0,0), [], [])
    # e = environment(25, 25, (0,0), [], [])
    # e = environment(50, 50, (0,0), [], [])

#     rob = randomRobot(e)
#     rob.cleanEnvironment()

#     robotInformation = {
#         "Total Moves" : rob.totalMoves,
#         "Moves Up" : rob.moveCounters["Up"],
#         "Moves Right" : rob.moveCounters["Right"],
#         "Moves Down" : rob.moveCounters["Down"],
#         "Moves Left" : rob.moveCounters["Left"],
#         "Move List" : rob.moveList
#     }

#     with open("results/randomResults.txt", "a") as f:
#         f.write(dumps(robotInformation))
#         f.write("\n")
# with open("results/randomResults.txt", "a") as f:
#     f.write("\n")