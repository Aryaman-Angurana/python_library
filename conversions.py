# to convert from one system to another
# to convert from decimal to binary
from stringfunctions import reverse
from mathsfunctions import power
def dtb(a):
    c = ""
    while(a != 0):
        c = c + str(a%2)
        a = a//2
    c = int(reverse(c))
    return c

# to convert from decimal to octal
def dto(a):
    c = ""
    while(a != 0):
        c = c + str(a%8)
        a = a//8
    c = int(reverse(c))
    return c
# to convert from decimal to hexadecimal
def dth(a):
    c = ""
    while(a != 0):
        f = ["A","B","C","D","E","F"]
        if ((a%16)<=9):
            d = str(a%16)
        else:
            d = f[(a%16)-10]
        c = c + d
        a = a//16
    c = reverse(c)
    return c

# to convert from binary to decimal
def btd(a):
    d=0
    i = 0
    while (a != 0):
        d= d + (a%10)*power(2,i)
        a = a//10
        i = i+1
    return d

# to convert from octal to decimal
def otd(a):
    d=0
    i = 0
    while (a != 0):
        d= d + (a%10)*power(8,i)
        a = a//10
        i = i+1
    return d

# to convert from hexadecimal to decimal
def htd(a):
    d = 0
    c = reverse(a)
    f = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10, "B":11, "C":12 , "D":13 , "E":14 , "F":15}
    for i in range (0,len(a)):
        d = d + f.get(c[i])*power(16,i)
    return d

# to convert from binary to octal
def bto(a):
    a = dto(btd(a))
    return a 

# to convert from binary to hexadecimal
def bth(a):
    a = dth(btd(a))
    return a

# to convert from octal to binary
def otb(a):
    a = dtb(otd(a))
    return a

# to convert from octal to hexadecimal
def oth(a):
    a = dth(otd(a))
    return a

# to convert from hexadecimal to binary
def htb(a):
    a = dtb(htd(a))
    return a

# to convert from hexadecimal to octal
def hto(a):
    a = dto(htd(a))
    return a
