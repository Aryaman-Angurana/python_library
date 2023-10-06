""" basic functions"""
from randomnumber import shuffle
from mathsfunctions import factorial
from listfunctions import sortlistalnumasc
# to make list free from repetitions
def freefromrepetitions(a):
    for i in range(0,len(a)):
        if (i<len(a)-1):
            j = i+1
            while (j <= len(a)-1):
                while True:
                    if (type(a[i]) is list):
                        a[i] = sortlistalnumasc(a[i])
                    if (type(a[j]) is list):
                        a[j] = sortlistalnumasc(a[j])
                    if (a[i] == a[j] and i != j):
                        c = a.pop(j)
                    if (j >= len(a)):
                        break
                    if (a[i]!=a[j]):
                        break
                j = j+1
                
    return a

#to make concatinated list free from inner list containing repeated elements
def freefrominnerrepetitions(a):
    b = list()
    for i in range(0,len(a)):
        d = 0
        for j in range(0,len(a[i])-1):
            for k in range (j+1,len(a[i])):
                if (a[i][j] == a[i][k]):
                    d = 1
        if(d == 0):
            b = b + [a[i]]
    return b


# to make all possible permutations with repetitions
def permutationwithrepetition(a,b):
    c = list()
    a = freefromrepetitions(a)
    l = len(a)
    comb = l**b
    j = 0
    for i in range(0,comb):
        d = list()
        for k in range(0,b):
            d = d + [a[(j//(l**k))%l]]
        c = c + [d]
        j = j+1
    return c

# to make all possible permutations without repetitions
def permutationwithoutrepetition(a,b):
    c = freefrominnerrepetititons(permutationwithrepetition(a,b))
    return c

# to make all combinations 
def combinations(a,b):
    c = freefromrepetitions(permutationwithoutrepetition(a,b))
    return c
