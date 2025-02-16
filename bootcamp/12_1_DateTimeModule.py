

# DATE

import datetime

today = datetime.date.today()

print(today)
print('ctime:', today.ctime())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Month abbreviation, day and year	
d2 = today.strftime("%d/%b/%Y")
print("d2 =", d2)

# DATETIME

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


# ARITHMETIC

from datetime import date

date1=date(2025,11,29)

date2=date(2024,11,20)

result = date1 - date2
print(str(result))