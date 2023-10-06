# to print fibonacci series
n = int (input ("Enter the number of elements "))
a = 1
b = 0
for i in range (0,n):
    print(a, end = " ")
    c = a
    a = b+a
    b = c
