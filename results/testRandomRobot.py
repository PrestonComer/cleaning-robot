import sys
sys.path.append('..')
from randomRobot import *

RESULTSFILE = "randomResults2.txt"

envList = [
    # Test the robot when it starts at different locations
    {
        "env" : "environment(5, 5, (0,0), [], [])",
        "size" : "5x5",
        "start" : "(0,0)",
        "clean" : "[]",
        "obj" : "[]"
    },
    {
        "env" : "environment(5, 5, (2,2), [], [])",
        "size" : "5x5",
        "start" : "(2,2)",
        "clean" : "[]",
        "obj" : "[]"
    },
    {
        "env" : "environment(5, 5, (4,4), [], [])",
        "size" : "5x5",
        "start" : "(4,4)",
        "clean" : "[]",
        "obj" : "[]"
    },
    # Test the robot when there are clean spaces present before it begins
    {
        "env" : "environment(5, 5, (0,0), [(1,1)], [])",
        "size" : "5x5",
        "start" : "(0,0)",
        "clean" : "[(1,1)]", 
        "obj" : "[]"},
    {
        "env" : "environment(5, 5, (0,0), [(1,1), (2,2)], [])",
        "size" : "5x5",
        "start" : "(0,0)",
        "clean" : "[(1,1), (2,2)]",
        "obj" : "[]"},
    {
        "env" : "environment(5, 5, (0,0), [(1,1), (2,2), (3,3)], [])",
        "size" : "5x5",
        "start" : "(0,0)",
        "clean" : "[(1,1), (2,2), (3,3)]",
        "obj" : "[]"
    },
    # Test the robot when there are objects in the way
    {
        "env" : "environment(5, 5, (0,0), [], [(1,1)])",
        "size" : "5x5",
        "start" : "(0,0)",
        "clean" : "[]",
        "obj" : "[(1,1)]"
    },
    {
        "env" : "environment(5, 5, (0,0), [], [(1,1), (2,2)])",
        "size" : "5x5",
        "start" : "(0,0)",
        "clean" : "[]",
        "obj" : "[(1,1), (2,2)]"
    },
    {
        "env" : "environment(5, 5, (0,0), [], [(1,1), (2,2), (3,3)])",
        "size" : "5x5",
        "start" : "(0,0)",
        "clean" : "[]",
        "obj" : "[(1,1), (2,2), (3,3)]"
    },
    # Test the robot when the area to be cleaned is of a larger size
    {
        "env" : "environment(10, 10, (0,0), [], [])",
        "size" : "10x10",
        "start" : "(0,0)",
        "clean" : "[]",
        "obj" : "[]"
    },
    {
        "env" : "environment(25, 25, (0,0), [], [])",
        "size" : "25x25",
        "start" : "(0,0)",
        "clean" : "[]",
        "obj" : "[]"
    },
    {
        "env" : "environment(50, 50, (0,0), [], [])",
        "size" : "50x50",
        "start" : "(0,0)",
        "clean" : "[]",
        "obj" : "[]"
    }
]

with open(RESULTSFILE, "w") as f:
    msg = "The Following Results Are Based On A {} Environment With The Random Movement Cleaning Robot Positioned At {}, Clean Position(s) At {}, And Object(s) At {}\n"

    for env in envList:
        f.write(msg.format(env["size"], env["start"], env["clean"], env["obj"]))

        for _ in range(100):
            rob = randomRobot(eval(env['env']))
            rob.cleanEnvironment()

            f.write(dumps({
                "Total Moves" : rob.totalMoves,
                "Moves Up" : rob.moveCounters["Up"],
                "Moves Right" : rob.moveCounters["Right"],
                "Moves Down" : rob.moveCounters["Down"],
                "Moves Left" : rob.moveCounters["Left"],
                "Move List" : rob.moveList
            }))

            f.write("\n")
        f.write("\n")