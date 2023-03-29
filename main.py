import os
import re


def open_file(name):
    inputFile = open(name, "r")
    linesInFile = []
    for line in inputFile:
        linesInFile.append(line.replace('\n', ''))
    return linesInFile

def main():
    file1 = open_file("inputFile1.txt")
    file2 = open_file("inputFile2.txt")
    print(file1)
    print(file2)


if __name__ == "__main__":
    main()
