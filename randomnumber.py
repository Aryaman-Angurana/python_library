# to generate a random number
from datetime import datetime

# to give a random fraction
def randomfraction():
    a = (int(str(datetime.now())[-3:-1]))/100
    return a

# random +1 or -1
def randomsign():
    s = str(datetime.now())
    if ((int(s[-3])%2) == 0):
        return (1)
    else:
        return (-1)
# to give a random integer
def randominteger():
    b = randomsign()
    s = str(datetime.now())
    a = b*(int (s[-3:-1]))
    return(a)

# to return an integer in a range
def randomintegerrange(a):
    s = randominteger()
    while True:
        if (s>0):
            if (s>a):
                s = s-a
        else:
            s = s+a
        if (s<=a and s>0):
            break
    return s

# to shuffle a collection
def shuffle(a):
    l = len(a)
    b = []
    for i in range(1,l+1):
        if(len(a)>1):
            s = randomintegerrange(l - i)
            b = b + a[s:s+1]
            c= a.pop(s)
        else:
            b = b + a
    return b
