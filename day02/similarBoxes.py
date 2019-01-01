import sys

def main(argv):
    print readVal(argv)

def readVal(argv):
    f = open(argv[0], "r")
    charFreq = {}
    freq = {}
    diff = []

    lines = f.readlines()
    lines = map(lambda x : x[:-1], lines)   #removes newline chars
    for line in lines:
        for line2 in lines:
            diff = checkDiff(line, line2)
            if(len(diff) == len(line) - 1): 
                return diff
            diff = ""

def checkDiff(line1, line2):
    diff = ""
    for index in range(0,len(line1)):
        if(line1[index] == line2[index]):
            diff += line1[index]
    return diff

if __name__ == "__main__":
    main(sys.argv[1:])
