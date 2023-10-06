# to print all prime numbers in an interval
from mathsfunctions import squareroot
a = int(input("Enter the lower limit of the interval "))
b = int (input("Enter the upper limit of the interval "))
print("The prime numers are:", end = "\n")
if (a <= 1):
    a = 2
for i in range(a , b+1):
    d = 0
    for j in range(2,(int(float(squareroot(i)))+1)):
        if ((i % j) == 0):
            d = 1
    if (d ==0):
        print (i , end = " ")
b = input()
