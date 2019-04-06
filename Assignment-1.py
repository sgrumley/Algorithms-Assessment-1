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
        print("p value ",j,":", p[n_val[j]])
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
            if summedValues(p, n_val) == total:
                tempSol = []
                for x in range(n):
                    tempSol.append(p[n_val[x]])
                exportedSol.append(tempSol)
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
            print(total, "-", sum)
            #next value - current value
            diff = p[n_val[-1]+1] - p[n_val[-1]]

            """Check if goal state and/or increment"""
            if limit == 0:
                tempSol = []
                for x in range(n):
                    tempSol.append(p[n_val[x]])
                exportedSol.append(tempSol)
                n_val[-2] += 1
                n_val[-1] = n_val[-2]
            #if jump in sum is bigger than the remainder needed -> roll back a value and increase
            elif diff > limit:
                n_val[-2] += 1
                n_val[-1] = n_val[-2]
            #else keep incrementing the right most column
            else:
                n_val[-1] += 1
            print("Sum: ", sum, " limit: ", limit, "Diff: ", diff)
            print("------- iteration: ",count+1, "-------" )

    print("results:",exportedSol)
    print(p)
    print("Total times sum ran:", sumcount)

n = 2
total = 8
p = getPrimeNums(total)
print(p)
limit = 0
n_val = [0 for i in range(n)]
exportedSol =[]
algorithm(n, total, p, n_val)

""" total = 16, n=3 """
print()
print()
print()
print()
n = 3
total = 16
p = getPrimeNums(total)


primeGap = total - p[-1]
primeGapList = []
n_val1 = [0 for i in range(n-1)]

for i in range(len(p)):
    if p[i] > primeGap:
        break
    primeGapList.append(p[i])

algorithm(n-1, primeGap, primeGapList, n_val1)

print("prime gap list: ", primeGapList)
print("prime gap", total, primeGap)
