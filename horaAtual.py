from datetime import datetime

dt = datetime.today()
dtf = '23:59'

def diff_dates(date1, date2):
    return abs(date2-date1).days


result = diff_dates(d1,d2)

d1 = dt.strptime(dt, '%d/%m/%Y %H:%M')
d2 = dt.strptime(dt, '%d/%m/%Y')+" "+dtf


print (result)






   
   




