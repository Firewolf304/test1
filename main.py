from typing import List, Any

mass = []
from src import errors

"""n = int(input("Enter y size: "))
m = int(input("Enter x size: "))
for i in range(n):
    text = list(map(int,input("Enter the numbers : ").strip().split()))[:m]
    mass.append(text)"""
#n = 2
#m = 4
#mass = [[0,3,1,1],[1,-3,-2,0]]
#format = [3,4,3,0]
#equality = [5,7]
n = 3
m = 6
mass = [[1,1,1,0,0,0],[0,2,0,0,1,1],[0,2,1,1,0,0]]
format = [-2,-1,0,0,0,0]
equality = [2,5,1]
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
new = [[-1]*len(itermatrix[0])] * len(itermatrix)
### ITERATION
while(not(all(map(lambda x: x >= 0, new[-1])))):
    #maximus = max( abs(list(map(lambda a: a <0 , old[-1]))) )
    new = [[0]*len(itermatrix[0])] * len(itermatrix)
    maxInd = 0
    val = 0
    recursive_check = False                         # if some values in the F
    for i in range(len(notbased)):
        if old[-1][i] < 0 and abs(old[-1][i]) > val:
            val = abs(old[-1][i])
            maxInd = i
        elif
    nextCheck = []
    for y in range(len(based)):
        nextCheck.append( old[y][len(notbased)]/old[y][maxInd])


    #itermatrix[-1].index(maximus*(-1))
    pass

