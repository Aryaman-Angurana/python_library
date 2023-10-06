# to solve quadratic equation
import mathsfunctions
a = int(input ("Enter the coefficient of x^2 "))
b = int (input ("Enter the coefficient of x "))
c = int(input ("Enter the constant "))
D = b*b - 4*a*c
if (D<0):
    print ("The equation has no roots")
else:
    D = mathsfunctions.squareroot(D)
    e = (-b +D)/(2*a)
    f = (-b -D)/(2*a)
    print("The roots are", e, "and",f)
b = input()
