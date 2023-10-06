# maths module


# to calculete the square root
def squareroot(a):
    b = a**0.5
    return b

# to compute the power
def power(a,b):
    c = a**b
    return c

# to compute the mean
def mean(a):
    b = len(a)
    c = 0
    for i in range(0,b):
        c = c+a[i]
    m = c/b
    return m

# to calculate the median
def median (a):
    a.sort()
    l = len(a)
    if ((l%2)==0):
        return((a[int(l/2)-1] + a[int(l/2)])/2)
    else:
        return(a[int((l+1)/2) -1])

# to calculate factorial
def factorial(a):
    c = 1
    if (a > 0):
        for i in range (1,a+1):
            c = c*i
        return c
    else :
        return c
    
# to find hcf
def hcfint(a,b):
    c=1
    if (a >= b):
        for i in range(1, a+1):
            if ((a%i)==0 and (b%i)==0):
                c = i
    else:
        for i in range(1, b+1):
            if ((a%i)==0 and (b%i)==0):
                c = i
    return c

# to calculate lcm
def lcmint(a,b):
    c = 1
    if (a>=b):
        for i in range(a,100000000000000000000000000000000000000000000000000):
            if ((i%a)==0 and (i%b)==0):
                c = i
                break
    else:
        for i in range(b,100000000000000000000000000000000000000000000000000):
            if ((i%a)==0 and (i%b)==0):
                c = i
                break
    return c

# to calculate the hcf of decimal values
def hcfdecimal(a , b):
    c = hcfint(a[0], b[0])
    d = lcmint(a[1], b[1])
    hcf = c/d
    return hcf

# to calculate the lcm of decimal values
def lcmdecimal(a , b):
    c = lcmint(a[0], b[0])
    d = hcfint(a[1], b[1])
    lcm = c/d
    return lcm
