p = [1,2,3,5,7]
#p = [1,2,3,5,7]
n = 3
total = 8
limit = 0
n_val = [0 for i in range(n)]

exportedSol =[]
pepsi = 2
shell = 1
#hard coded max
max = 7


count = 0
while(1):
    sum = 0
    atLimit = False
    count +=1

    #sum is equal to the sum of p values represented from the n_val array
    for j in range(n):
        #check if any column is at its max
        #if yes atLimit = true, shell records the position and breaks
        # This takes the first position from the left
        if p[n_val[j]] == max:
            atLimit = True
            shell = j
            break


    #if
    if atLimit:
        print("old nval", n_val)
        n_val[shell - 1] += 1
        iters = n-shell
        print("iters:",iters)
        for j in range(1, iters+1):
            print( n_val[shell-1])
            n_val[-j] = n_val[shell-1]
        atLimit = False

        #if all iterations have been completed
        if n_val[0] == len(p)-1:
            print("we done")
            print("new nval", n_val)
            break
        print("new nval", n_val)

    for j in range(n):
        if p[n_val[j]] == max:
            atLimit = True
            shell = j

    if atLimit == False:
        for j in range(n):
            print("p value ",j,":", p[n_val[j]])
            sum += p[n_val[j]]
        # find the range for the next possible value
        limit = total - sum
        current_val = p[n_val[-1]]
        next_val = p[n_val[-1]+1]
        diff = next_val - current_val

        #if soloution
        if limit == 0:
            tempSol = []
            for x in range(n):
                tempSol.append(p[n_val[x]])
            print("soloution found", tempSol)
            exportedSol.append(tempSol)
            n_val[-2] += 1
            n_val[-1] = n_val[-2]
        #if jump in sum is bigger than the remainder needed -> roll back a value and increase
        elif diff > limit:
            print("next value doesnt work")
            n_val[-2] += 1
            n_val[-1] = n_val[-2]
        else:
            n_val[-1] += 1
        print("Sum: ", sum, " limit: ", limit, "Diff: ", diff)
        print("------- iteration: ",count+1, "-------" )

print(exportedSol)
