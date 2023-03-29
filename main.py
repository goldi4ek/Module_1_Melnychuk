import os
import re


def open_file(name):
    inputFile = open(name, "r")
    linesInFile = []
    for line in inputFile:
        linesInFile.append(line.replace('\n', ''))
    return linesInFile


def check_similar(file1, file2):
    return set(file1).intersection(file2)



def main():
    file1 = open_file("inputFile1.txt")
    file2 = open_file("inputFile2.txt")
    print(file1)
    print(file2)
    similar_lines = check_similar(file1, file2)


if __name__ == "__main__":
    main()
