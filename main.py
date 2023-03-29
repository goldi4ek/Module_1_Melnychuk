

class FileChecker:
    def open_file(self, name):
        inputFile = open(name, "r")
        linesInFile = []
        for line in inputFile:
            linesInFile.append(line.replace('\n', ''))
        print(linesInFile)
        return linesInFile

    def check_similar(self, file1, file2):
        return set(file1).intersection(file2)

    def check_different(self, file1, file2):
        return set(file1).symmetric_difference(file2)

    def wrote_file(self, file, path):
        pathToFile = f"{path}.txt"
        wroteInFile = open(pathToFile, "w")
        for line in file:
            wroteInFile.write(f"{line}\n")


def main():
    fileChecker = FileChecker()
    file1 = fileChecker.open_file("inputFile1.txt")
    file2 = fileChecker.open_file("inputFile2.txt")
    similar_lines = fileChecker.check_similar(file1, file2)
    different_lines = fileChecker.check_different(file1, file2)
    fileChecker.wrote_file(similar_lines, "same")
    fileChecker.wrote_file(different_lines, "diff")


if __name__ == "__main__":
    main()
