from typing import List, Any
import copy
#import threading

mass = []
from src import errors

n = int(input("Enter y size: "))
m = int(input("Enter x size: "))
for i in range(n):
    text = list(map(int,input("Enter the numbers : ").strip().split()))[:m]
    mass.append(text)
format = list(map(int,input("Enter format : ").strip().split()))[:m]
equality = list(map(int,input("Enter equality : ").strip().split()))[:m]
#n = 2
#m = 4
#mass = [[0,3,1,1],[1,-3,-2,0]]
#format = [3,4,3,0]
#equality = [5,7]
#n = 3
#m = 6
#mass = [[1,1,1,0,0,0],[0,2,0,0,1,1],[0,2,1,1,0,0]]
#format = [-2,-1,0,0,0,0]
#equality = [2,5,1]
#n = 2
#m = 4
#mass = [[0,3,1,1],[1,-3,-2,0]]
#format = [3,0,3,0]
#equality = [5,7]
#n = 2
#m = 5
#mass = [[1,2,0,-1,1],[2,1,1,3,0]]
#format = [-3,-2,-4,-1,-2]
#equality = [5,5]

based = []
notbased = []
if(len(mass[0]) != len(format)):
    raise errors.InputError("Error input, this is size: " + str(len(mass[0])))


def check(y:int, x: int) -> bool:
    global mass
    for Y in range(n):
        if (Y!=y and mass[Y][x] != 0):
            return False
    return True

for y in range(n):
    for x in range(m):
        if(mass[y][x] == 1 and check(y,x) and len(based) == y):
            #based.insert(0,x)
            based.append(x)
        if( len(based) == y or (mass[y][x] != 1 and not(check(y,x))) ):
            notbased.append(x)

notbased = list(set( [x for x in notbased if x not in based] ))
#print("mass",mass)
#print("based =",based, "not based =", notbased)

itermatrix: list[Any] = []
#
for y in range(n):  # make start matrix
    itermatrix.append(list([]))
    for x in range(m): # use Python methods!
        if(not(x in based)):
            itermatrix[y].append(mass[y][x])
            #summ[y] += mass[y][x] * format[based[y]]
    itermatrix[y].append(equality[y])
#print("itermatrix =", itermatrix)

def summ() -> list[Any]:
    summ = [0]*(len(notbased)+1)   # for F in end of matrix
    for x in range(len(summ)):
        for y in range(len(itermatrix)):
            summ[x] += itermatrix[y][x] * format[based[y]]
            #print(summ[x])
    return summ


#for i in notbased:
itermatrix.append( list(map(lambda a,b: a-b, summ(),  [format[x] for x in notbased] + [0] ) ) )
#map(lambda a,b: a-b, summ, format[based[y]] )
print("start = " + str(itermatrix))


old = itermatrix
new = [[ -1 for _ in range(len(itermatrix[0]))] for _ in range(len(itermatrix))]

#new = [[-1]*len(itermatrix[0])] * len(itermatrix)



def changeBest():
    global bestIndexX, bestIndexY, new
    nig_mass = list(map(lambda a: abs(a), [x for x in old[-1][:-1] if x < 0]))  # all abs of negative values
    value = nig_mass.count(max(nig_mass))
    if (value > 1):  # if some values in the F
        listing: list[dict] = []

        def func(index: int) -> None:
            global listing
            bestIndY = 0
            val = 9999999
            for i in range(len(based)):
                try:
                    if (val >= old[i][len(notbased)] / old[i][index] and old[i][index] > 0):
                        val = old[i][len(notbased)] / old[i][index]
                        bestIndY = i
                except Exception:
                    pass
            listing.append(dict({'X': index, 'Y': bestIndY, 'val': val}))

        # maximus = map( lambda a: a==max(nig_mass) ,  )
        save = 0
        for i in range(value):  # use python methods!
            save = nig_mass.index(max(nig_mass), save)
            func(save)
        element = min(listing, key=lambda x: x['val'])
        bestIndexX = element['X']
        bestIndexX = element['Y']
        pass
    else:
        bestIndexX = old[-1].index(max(nig_mass) * -1)
        val = 9999999
        for i in range(len(based)):
            try:
                if (val >= old[i][len(notbased)] / old[i][bestIndexX] and old[i][bestIndexX] > 0):
                    val = old[i][len(notbased)] / old[i][bestIndexX]
                    bestIndexY = i
            except Exception:
                pass
    print('best coords (x y):', bestIndexX, bestIndexY)

test = 0
### ========================================ITERATION========================================
while(not(all(map(lambda x: x >= 0, new[-1][:-1])))):
#while(test < 2):
    #maximus = max( abs(list(map(lambda a: a <0 , old[-1]))) )
    new = [[ 0 for _ in range(len(itermatrix[0]))] for _ in range(len(itermatrix))]
    maxInd = 0
    val = 0
    bestIndexX = 0
    bestIndexY = 0
    changeBest()
    new[bestIndexY][bestIndexX] = float(1 / old[bestIndexY][bestIndexX])

    # заебали эти вумные методы, я в тупую
    for y in range(len(new)):
        if y != bestIndexY:
            new[y][bestIndexX] = old[y][bestIndexX] * new[bestIndexY][bestIndexX] * (-1)
    for x in range(len(notbased)+1):
        if x != bestIndexX:
            new[bestIndexY][x] = float(old[bestIndexY][x] * new[bestIndexY][bestIndexX])

    for y in range(len(new)):
        for x in range(len(new[y])):
            if(y != bestIndexY and x != bestIndexX):
                new[y][x] = (old[y][x] * old[bestIndexY][bestIndexX] - old[bestIndexY][x] * old[y][bestIndexX] ) / old[bestIndexY][bestIndexX]

    old = copy.copy(new)
    print(new)
    #test +=1
    pass

