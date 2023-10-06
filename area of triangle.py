# to calculate the area of a triangle
print ("press 1 for coordinates, 2 for side lengths, 3 for height and base" , end = " ")
from mathsfunctions import squareroot
ch = ""
a = 0
while (ch != "y"):
    a = int (input ())
    print ("Are you sure? Type y for yes and n for no ", end = "")
    ch = input()
if (a == 1):
    a1 = int (input ("Enter the x of first point "))
    a2 = int (input ("Enter the y of first point "))
    b1 = int (input ("Enter the x of second point "))
    b2 = int (input ("Enter the y of second point "))
    c1 = int (input ("Enter the x of third point "))
    c2 = int (input ("Enter the y of third point "))
    d = 0.5*(a1*b2 - a2*b1 - b2*c1 + c2*b1 + c1*a2 - c2*a1)
    print ("area = " , d)
    b = input()
elif(a == 2):
    a = int(input ("Enter the first side "))
    b = int (input ("Enter the second side "))
    c = int (input("Enter the third side "))
    s = (a+b+c)/2
    d = squareroot(s*(s-a)*(s-b)*(s-c))
    print ("area = ", d)
    b = input()
elif (a == 3):
    b = int (input("Enter the base "))
    h = int (input ("Enter the height "))
    d = (h*b)/2
    print ("area = ", d)
    b = input()
else:
    print ("wrong choice")
    b = input()
