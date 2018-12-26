import sys

def main(argv):
    print readVal(argv)

def readVal(argv):
    f = open(argv[0], "r")
    total = 0;
    resultFreqs = {};

    lines = f.readlines()
    while(True):
        for line in lines:
            if(line[0] == '-'):
                total-= int(line[1:])
            elif(line[0] == '+'):
                total += int(line[1:])

            if(resultFreqs.get(total) == 1):
                return total
            else:
                resultFreqs.update({total : 1})

    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
