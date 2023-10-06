''' Calendar module '''

# to find the day in the year
def dayinyear(year , month , date):
    months = {1:31 , 2 : 28 , 3 : 31 , 4 : 30 , 5 : 31 , 6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31}
    monthsleap = {1:31 , 2 : 29 , 3 : 31 , 4 : 30 , 5 : 31 , 6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31}
    day = 0
    for i in range (1 , month+1):
        if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
            if ( i != month ):
                day = day + monthsleap[i]
            else:
                day = day + date
        else:
             if ( i != month ):
                day = day + months[i]
             else:
                day = day + date
    return day

# to calculate the day in the calendar
def dayincalendar(year , month , date):
    day = 0
    for i in range(0 , year+1):
        if (i != year):
            day = day + dayinyear(i , 12 , 31)
        else:
            day = day + dayinyear(year , month , date)
    return day

# to calculate the day
def day(year , month , date):
    d = dayincalendar(year , month , date)
    d1 = {2:'Sunday',3:'Monday',4:'Tuesday',5:'Wednesday',6:'Thursday',0:'Friday',1:'Saturday'}
    a = d % 7
    return (d1[a])

# to print the month
def printmonth(year , month):
    months = {1:31 , 2 : 28 , 3 : 31 , 4 : 30 , 5 : 31 , 6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31}
    monthsleap = {1:31 , 2 : 29 , 3 : 31 , 4 : 30 , 5 : 31 , 6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31}
    dict1 = dict()
    for i in range (1 , month+1):
        if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
            for i in range (1, monthsleap[month]+1):
                dict1[i] = day(year , month , i)
        else:
            for i in range (1, months[month]+1):
                dict1[i] = day(year , month , i)
    d1 = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    d2 = {'Sunday':6,'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5}
    b = dict1[len(dict1)]
    d3 = {1:'01',2:'02',3:'03',4:'04',5:'05',6:'06',7:'07',8:'08',9:'09',10:'10',11:'11',12:'12',13:'13',14:'14',15:'15',16:'16',17:'17',18:'18',19:'19',20:'20',21:'21',22:'22',23:'23',24:'24',25:'25',26:'26',27:'27',28:'28',29:'29',30:'30',31:'31'}
    dict2 = dict()
    for i in range (7):
        d = list()
        for j in range(1,len(dict1)+1):
            if (d1[i] == dict1[j]):
                d = d + [d3[j]]
        if (i > d2[b]):
            d = d + ['  ']
        for j in range (0,7):
            if (len(d) != 6):
                d = ['  '] + d
            else:
                break
        dict2[d1[i]] = list(d)
    for i in range (0,len(dict2)):
        print(d1[i][0:3] , dict2[d1[i]][0] , dict2[d1[i]][1] , dict2[d1[i]][2] , dict2[d1[i]][3] , dict2[d1[i]][4] , dict2[d1[i]][5])

# to print the year
def printyear(year):
    print(year , end = '\n\n')
    y = {1:'January',2:'February',3:'March',4:"April",5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    for i in range (1,13):
        print(y[i])
        printmonth(year , i)
        print ("\n")