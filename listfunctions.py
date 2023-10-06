"""List functions"""

# to sort a numeric list
def sortlistnumericdes(a):
    b = a
    i = 0
    while i < len(b):
        d = b[i]
        for j in range (i+1, len(b)):
            if (d < b[j]):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    return b

# to sort a numeric list in ascending order
def sortlistnumericasc(a):
    b = a
    i = 0
    while i < len(b):
        d = b[i]
        for j in range (i+1, len(b)):
            if (d > b[j]):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    return b

# to sort a list containing words in descending order
def sortlistalphades(a):
    b = a
    i = 0
    while i < len(b):
        d = b[i]
        for j in range (i+1, len(b)):
            if (str(d) < str(b[j])):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    return b

# to sort a list containing words in ascending order
def sortlistalphaasc(a):
    b = a
    i = 0
    while i < len(b):
        d = b[i]
        for j in range (i+1, len(b)):
            if (str(d) > str(b[j])):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    return b

# to separate a list from in words and numeric
def separatelist(a):
    c = list()
    d = list()
    for i in range(0,len(a)):
        if (type(a[i]) is int):
            c = c + [a[i]]
        else:
            d = d + [a[i]]
    return (c+d)

# to sort an alphanumeric list in descending order
def sortlistalnumdes(a):
    a = separatelist(a)
    l = -1
    for i in range(0,len(a)):
        if (type(a[i]) is int):
            l = i
    b = a
    i = 0
    while i < l+1:
        d = b[i]
        for j in range (i+1, l+1):
            if (d < b[j]):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    while i < len(b):
        d = b[i]
        for j in range (i+1, len(b)):
            if (str(d) < str(b[j])):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    return b

# to sort an alphanumeric list in ascending order
def sortlistalnumasc(a):
    a = separatelist(a)
    l = -1
    for i in range(0,len(a)):
        if (type(a[i]) is int):
            l = i
    b = a
    i = 0
    while i < l+1:
        d = b[i]
        for j in range (i+1, l+1):
            if (d > b[j]):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    while i < len(b):
        d = b[i]
        for j in range (i+1, len(b)):
            if (str(d) > str(b[j])):
                (b[i] , b[j]) = (b[j] , b[i])
                d = b[i]
        i = i+1
    return b

# to print all the elements of a list
def printlist(a):
    for i in range(0,len(a)):
        print(a[i] , end = ' ')
