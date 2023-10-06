# string functions

# to reverse a string
def reverse(a):
    n = len(a)
    c = ""
    for i in range(n-1,-1,-1):
        c = c+ a[i]
    return c

# to find the length of a string
def lengthstring(a):
    d = 0
    e = 0
    while (e == 0):
        try:
            b = a[d]
            d = d+1
        except:
            e = 1
    return d

# to convert the string to upper case
def strucase(a):
    d = {'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
    b = ''
    for i in range(0,lengthstring(a)):
        try:
            b = b + d[str(a[i])]
        except:
            b = b + a[i]
    return b

# to convert the string into lower case
def strlcase(a):
    d = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
    b = ''
    for i in range(0,lengthstring(a)):
        try:
            b = b + d[str(a[i])]
        except:
            b = b + a[i]
    return b

# to convert the string into title case
def strtcase(a):
    b = ''
    for i in range(0,lengthstring(a)):
        if (i == 0):
            b = b + strucase(a[i])
        elif (a[i-1] == ' '):
            b = b + strucase(a[i])
        else:
            b = b + strlcase(a[i])
    return b
