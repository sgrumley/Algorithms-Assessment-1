import time
import copy

def readIn():
    with open("input.txt") as f:
        return [line.split() for line in f]


def writeOut(writeData):
    with open("output.txt", "w") as file:
        for i in range(len(writeData)):
            file.write(str(writeData[i]) + "\n")

def colCheck(p, n_val):
    max = p[-1]
    shell = None
    atLimit = False
    for j in range(len(n_val)):
        #check if any column is at its max, record which column
        # This takes the first position from the left
        if p[n_val[j]] == max:
            atLimit = True
            shell = j
            break
    return atLimit, shell

def summedValues(p, n_val):
    sum = 0
    for j in range(len(n_val)):
        sum += p[n_val[j]]
    return sum

def getPrimeNums(total):
    dataSet = [1]
    for i in range (2, total + 1):
        if isPrime(i):
            dataSet.append(i)
    return dataSet

def isPrime(total):
    prime = True
    for j in range(2, total):
        if total % j == 0:
            prime = False
            break
    return prime

def getPrimeGap(total, p):
    primeGap = total - p[-1]
    primeGapList = []

    for i in range(len(p)):
        primeGapList.append(p[i])
        if p[i] > primeGap:
            break
    return primeGap, primeGapList

def appendSoloution(maxPrimeCominations, p):
    for i in range(len(maxPrimeCominations)):
        maxPrimeCominations[i].append(p)
    return maxPrimeCominations

def algorithm(n, total, p, n_val):
    exportedSol = []
    count = 0
    sumcount = 0
    limit = 0
    """while the first value is not maxed out"""
    while(n_val[0] != len(p)-1):
        atLimit = False
        count +=1
        #check if a col is maxed
        atLimit, shell = colCheck(p, n_val)

        """while a col is maxed increment the column before it"""
        while(atLimit == True):
            # if shell == all soloutions checked
            sumcount += 1
            #if summedValues(p, n_val) == total:
                #tempSol = []
                #for x in range(n):
                #    tempSol.append(p[n_val[x]])
                #exportedSol.append(tempSol)
            if shell == 0:
                break
            if atLimit:
                #increment column to the left
                n_val[shell - 1] += 1
                iters = n-shell
                #set everything on the right of the incremented number equal to the incremented number
                for j in range(1, iters+1):
                    n_val[-j] = n_val[shell-1]
                atLimit = False
            #check to make sure no other colums are maxed
            atLimit, shell = colCheck(p, n_val)

        """compute differences between number needed and next number given"""
        if atLimit == False:
            # sum values of comination
            sum = summedValues(p, n_val)
            # find the difference max difference needed to find a soloution
            limit = total - sum
            #next value - current value
            diff = p[n_val[-1]+1] - p[n_val[-1]]

            """Check if goal state and/or increment"""
            if limit == 0:
                tempSol = []
                for x in range(n):
                    tempSol.append(p[n_val[x]])
                exportedSol.append(tempSol)
                try:
                    n_val[-2] += 1
                    n_val[-1] = n_val[-2]
                except:
                    n_val[-1] += 1
                    #pass
            #if jump in sum is bigger than the remainder needed -> roll back a value and increase
            elif diff > limit:
                n_val[-2] += 1
                n_val[-1] = n_val[-2]
            #else keep incrementing the right most column
            else:
                n_val[-1] += 1
            #print("Sum: ", sum, " limit: ", limit, "Diff: ", diff)
            #print("------- iteration: ",count+1, "-------" )

    #print("results:",exportedSol)
    #print(p)
#print("Total times sum ran:", sumcount)
    return exportedSol


def runFunc(n, total):
    p = getPrimeNums(total)
    if n == 1:
        if total == p[-1]:
            return 1
        else:
            return 0

    """ Results for highest prime number """
    n_valgap = [0 for i in range(n-1)]
    primeGap, primeGapList = getPrimeGap(total, p)
    maxPrimeCominations = algorithm(n-1, primeGap, primeGapList, n_valgap)
    maxPrimeCominations = appendSoloution(maxPrimeCominations, p[-1])

    """Results for every other prime number"""
    n_val = [0 for i in range(n)]
    soloutions = algorithm(n, total, p, n_val)

    for i in range(len(maxPrimeCominations)):
        soloutions.append(maxPrimeCominations[i])
    print(n, soloutions)
    length = len(soloutions)
    return length

""" driver """
readValues = readIn()
print("read values",readValues)
printVals = []
for j in range(len(readValues)):
    determineInput = len(readValues[j])
    print()
    print(readValues[j])
    start = time.time()
    if determineInput == 1:
        lengthSum = 0
        total = int(readValues[j][0])
        for i in range(1,total+1):
            length = runFunc(i,total)
            #print("nt=",i)
            lengthSum += length
        printVals.append(lengthSum)
        print(time.time() - start)

    elif determineInput == 2:
        total = int(readValues[j][0])
        n = int(readValues[j][1])
        length = runFunc(n, total)
        printVals.append(length)
        print(time.time() - start)

    elif determineInput == 3:
        timerSum = 0
        lengthSum = 0
        total = int(readValues[j][0])
        nMin = int(readValues[j][1])
        nMax = int(readValues[j][2])
        for i in range(nMin, nMax + 1):
            length = runFunc(i,total)
            lengthSum += length
        printVals.append(lengthSum)
        print(time.time() - start)
print()
print(printVals)
writeOut(printVals)
