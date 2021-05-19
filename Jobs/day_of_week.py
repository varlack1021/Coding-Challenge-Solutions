from datetime import datetime
import time

def dayOfWeek(birthdayDate):
    start = time.time()
    date = birthdayDate.split("-")
    
    month = int(date[0])
    day = int(date[1])
    start_year = int(date[2])
    year = start_year
    
    day_of_week = datetime.strptime(birthdayDate, '%m-%d-%Y').weekday()
    print(day_of_week)
    if month == 2 and day == 29:
        return 28
    ##skip one a day per none leap year, two days a leap year
    
    while True:
        year += 1
        print(year)
        print("{}-{}-{}".format(month, day, year))
        next_day = datetime.strptime("{}-{}-{}".format(month, day, year), '%m-%d-%Y').weekday()
        
        if next_day == day_of_week:
            break
    
    print(time.time() - start)        
    return year - start_year

print(datetime.strptime('01-21-2021', '%m-%d-%Y').weekday())
print(dayOfWeek('01-21-2016'))
