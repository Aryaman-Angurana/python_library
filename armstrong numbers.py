# to find armstrong numbers in an interval
from mathsfunctions import power
m = int(input("Enter the lower limit "))
n = int(input("Enter the upper limit "))
for i in range (m , n+1):
    a = i
    b = 0
    while (a != 0):
        d = a%10
        b = b + power(d,3)
        a = a//10
    if (i == b):
        print (i)
