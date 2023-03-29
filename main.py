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


def check_different(file1, file2):
    return set(file1).symmetric_difference(file2)


def main():
    file1 = open_file("inputFile1.txt")
    file2 = open_file("inputFile2.txt")
    similar_lines = check_similar(file1, file2)
    different_lines = check_different(file1, file2)
    print(similar_lines)
    print(different_lines)


if __name__ == "__main__":
    main()
