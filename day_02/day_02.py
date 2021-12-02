'''

--- Day 2: Dive! ---

Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

    forward 5 adds 5 to your horizontal position, a total of 5.
    down 5 adds 5 to your depth, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13.
    up 3 decreases your depth by 3, resulting in a value of 2.
    down 8 adds 8 to your depth, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

'''

from io import TextIOWrapper
import sys
from typing_extensions import final
from vpython.vector import vector

def getFile(fileName = "testfile.txt") -> TextIOWrapper:
    loadedFile = open(fileName, "r")
    return loadedFile

def closeFile(loadedFile: TextIOWrapper) -> None:
    loadedFile.close()

def getPlannedCourse(loadedFile: TextIOWrapper):
    course = []
    for line in loadedFile:
        splitLine = line.split(" ")
        course.append([splitLine[0], int(splitLine[1])])
    return course

def goThroughCourse(possibleMovements: dict, plannedCourse: list):
    finalPosition = vector(0,0,0)
    for courseNode in plannedCourse:
        finalPosition += (possibleMovements[courseNode[0]] * courseNode[1])
    return finalPosition

def main() -> int:
    loadedFile = getFile("input")

    #  -- start Part 1 --
    possibleMovements = {
        "forward": vector(1,0,0),
        "up": vector(0,-1,0),
        "down": vector(0,1,0)
    }
    course = getPlannedCourse(loadedFile)
    finalPosition = goThroughCourse(possibleMovements, course)
    print(str((int)(finalPosition.x * finalPosition.y)))
    # -- end Part 1 --

    closeFile(loadedFile)
    return 0

if __name__ == "__main__":
    sys.exit(main())