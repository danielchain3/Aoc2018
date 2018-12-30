import sys

def main(argv):
    print readVal(argv)

def readVal(argv):
    f = open(argv[0], "r")
    charFreq = {}
    freq = {}

    lines = f.readlines()
    for line in lines:
        for word in line[:-1]:
            if (charFreq.get(word) >= 0):
                charFreq.update({word : charFreq.get(word) + 1})
            else:
                charFreq.update({word : 1})
        occurances = calcFreq(charFreq)
        charFreq = {}
        print occurances

        for val in occurances:
            if (val > 1):
                if(freq.get(val) > 0):
                    freq.update({val : freq.get(val) + 1})
                else:
                    freq.update({val : 1})

    f.close()
    return freq

def calcFreq(chars):
    count = {}
    values = chars.values()
    values.sort()
    for val in values:
        if (count.get(val) >= 1):
            count.update({val : count.get(val) + 1})
        else:
            count.update({val : 1})
    return count


if __name__ == "__main__":
    main(sys.argv[1:])
