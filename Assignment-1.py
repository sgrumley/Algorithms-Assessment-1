"""
Sam Grumley
S5048240
Computing Algorithms
2801ICT
Assignment 1
Breif Description: Write a program that can calculate the total number of ways a given amount can be paid using a specified number of coins (Coins are prime numbers)
Run: python Assignment-1.py input.txt
"""
import time
import copy
import sys

""" Reads in Data from file """
def readIn(fileName):
    with open(fileName) as f:
        return [line.split() for line in f]


""" Writes data to output.txt """
def writeOut(writeData):
    with open("output.txt", "w") as file:
        for i in range(len(writeData)):
            file.write(str(writeData[i]) + "\n")


""" Gets an array of differences between each prime number """
def differenceArray(data):
    response = []
    for i in range(len(data) -1):
        response.append(data[i+1] - data[i])
    return(response)


""" Check if column is maxed (in n_val) """
def colCheck(p, n_val):
    max = p[-1]
    maxedColPos = None
    atLimit = False
    for j in range(len(n_val)):
        # This takes the first position from the left
        if p[n_val[j]] == max:
            atLimit = True
            maxedColPos = j
            break
    return atLimit, maxedColPos


""" Sums prime values based off n_val as an index """
def summedValues(p, n_val):
    sum = 0
    for j in range(len(n_val)):
        sum += p[n_val[j]]
    return sum


""" Gets all prime numbers below total """
def getPrimeNums(total):
    dataSet = [1,2]
    for i in range (3, total + 1):
        if isPrime(i):
            dataSet.append(i)
        i += 1
    return dataSet


""" Determines if the passed in value is Prime """
def isPrime(total):
    prime = True
    for j in range(2, total):
        if total % j == 0:
            prime = False
            break
    return prime


""" gets the difference between total and the highest prime number """
def getPrimeGap(total, p):
    primeGap = total - p[-1]
    primeGapList = []

    for i in range(len(p)):
        primeGapList.append(p[i])
        if p[i] > primeGap:
            break
    return primeGap, primeGapList


""" Gets all solutions of p that equal total and have n values"""
def algorithm(n, total, p, difArr):
    numSolutions = 0
    limit = 0
    n_val = [0 for i in range(n)]
    #while the first value is not maxed out
    while(n_val[0] != len(p)-1):
        atLimit = False
        #check if a col is maxed
        atLimit, maxedColPos = colCheck(p, n_val)
        #use sumcount to find out how many times the nested while runs
        sumcount = 0
        #while a col is maxed increment the column before it"""
        while(atLimit == True):
            # if maxedColPos == all solutions checked
            sumcount += 1
            if maxedColPos == 0:
                break
            if atLimit:
                #increment column to the left
                n_val[maxedColPos - 1] += 1
                iters = n-maxedColPos
                #set everything on the right of the incremented number equal to the incremented number
                for j in range(1, iters+1):
                    n_val[-j] = n_val[maxedColPos-1]
                atLimit = False
            #check to make sure no other colums are maxed
            atLimit, maxedColPos = colCheck(p, n_val)

        #compute differences between number needed and next number given
        if atLimit == False:
            # sum values of comination
            sum = summedValues(p, n_val)
            # find the difference max difference needed to find a solution
            limit = total - sum
            #Check if goal state and/or increment
            if limit == 0:
                numSolutions += 1
                try:
                    n_val[-2] += 1
                    n_val[-1] = n_val[-2]
                except:
                    n_val[-1] += 1
            #if jump in sum is bigger than the remainder needed -> roll back a value and increase
            elif difArr[n_val[-1]] > limit:
                try:
                    n_val[-2] += 1
                    n_val[-1] = n_val[-2]
                except:
                    n_val[-1] += 1
            #else keep incrementing the right most column
            else:
                n_val[-1] += 1
    return numSolutions


""" Controlled function to run a complete cycle of n """
def runFunc(n, total):
    p = getPrimeNums(total)
    # Return Gold coin Solution
    if n == 1:
        return 1
    # Results for highest prime number
    primeGap, primeGapList = getPrimeGap(total, p)
    difArr = differenceArray(primeGapList)
    Solutions = algorithm(n-1, primeGap, primeGapList, difArr)
    #Results for every other prime number + highest prime number results
    difArr = differenceArray(p)
    Solutions += algorithm(n, total, p, difArr)
    return Solutions

""" Driver """
fileName = sys.argv[1]
readValues = readIn(fileName)
print("read values",readValues)
printVals = []
#determine how many values are passed in per line read from input
for j in range(len(readValues)):
    determineInput = len(readValues[j])
    start = time.time()
    #Only one input value e.g. 8
    if determineInput == 1:
        lengthSum = 0
        total = int(readValues[j][0])
        for i in range(1,total+1):
            length = runFunc(i,total)
            lengthSum += length
        printVals.append(lengthSum)
        print("Input line: ", j+1, " - ",readValues[j] )
        print("Total solution:", lengthSum)
        print("time: ",time.time() - start)
        print()

    # Two input values e.g. 8 2
    elif determineInput == 2:
        total = int(readValues[j][0])
        n = int(readValues[j][1])
        length = runFunc(n, total)
        printVals.append(length)
        print("Input line: ", j+1, " - ",readValues[j] )
        print("Total solution:", lengthSum)
        print("time: ",time.time() - start)
        print()

    # Two input values e.g. 8 2 5
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
        print("Input line: ", j+1, " - ",readValues[j] )
        print("Total solution:", lengthSum)
        print("time: ",time.time() - start)
        print()
#write output to file
writeOut(printVals)
