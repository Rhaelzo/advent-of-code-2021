'''

--- Day 3: Binary Diagnostic ---

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

'''

import sys
from io import TextIOWrapper

def getFile(fileName = "testfile.txt") -> TextIOWrapper:
    loadedFile = open(fileName, "r")
    return loadedFile

def closeFile(loadedFile: TextIOWrapper) -> None:
    loadedFile.close()

def convertFileToList(loadedFile: TextIOWrapper) -> list:
    return [line.strip() for line in loadedFile]

def saveInListByColumn(listOfBits: list) -> list:
    listOfBitsByColumn = []
    for i in range(len(listOfBits[0])):
        for otherNode in listOfBits:
            if len(listOfBitsByColumn) < i + 1:
                listOfBitsByColumn.append("")
            listOfBitsByColumn[i] += otherNode[i]
    return listOfBitsByColumn

def getRates(convertedList: list) -> tuple:
    gammaRate = getGammaRate(convertedList)
    epsilonRate = inverseBitString(gammaRate)
    return (int(gammaRate, 2), int(epsilonRate, 2))

def inverseBitString(gammaRate: str) -> str:
    inverseBitDic = {"0": "1", "1": "0"}
    epsilonRate = ""
    for character in gammaRate:
        epsilonRate += inverseBitDic[character]
    return epsilonRate

def getGammaRate(convertedList: list) -> str:
    gammaRateBinaryString = ""
    for bitString in convertedList:
        amountOfOnes = bitString.count("1")
        if(amountOfOnes > len(bitString) / 2):
            gammaRateBinaryString += "1"
        else:
            gammaRateBinaryString += "0"
    return gammaRateBinaryString

def main() -> int:
    loadedFile = getFile("input")
    convertedList = saveInListByColumn(convertFileToList(loadedFile))
    rates = getRates(convertedList)
    print(rates[0] * rates[1])
    closeFile(loadedFile)
    return 0

if __name__ == "__main__":
    sys.exit(main())