#SIMPL Type 3 get_time module

#---Library Imports---
import time #import the time module
#---------------------

def return_leap_or_no(potential_leap):
    if potential_leap % 4 == 0 and potential_leap % 100 == 0 and potential_leap % 400 == 0: #is a leap year
        return True
    elif potential_leap % 4 == 0 and potential_leap % 100 == 0:
        return False
    elif potential_leap % 4 == 0: #is a leap year
        return True
    elif potential_leap % 4 != 0:
        return False

def find_decimal_number(num):
    while num > 1 and num != 1:
        num = num - 1
    else:
        return num

def get_time_secs(): #function that returns only the unix time epoch in seconds
    return time.time()

def get_time_string(): #function that returns a string with the format mm:hh dd/mm/yyyy UTC
    current_time_seconds = time.time() #assigns the unix time epoch to the variable 'current_time_seconds'
    #current_time_seconds = 2147483647 #<-- 'oh fuck' moment right here
    
    days_since_1970 = 0 #initialises a variable that holds the number of days since 00:00 UTC January 1st, 1970
    days_since_1970 = current_time_seconds / 86400 #divide the number of seconds since unix epoch by 86,400 to get the no. of days

    abs_days_since_1970 = int(days_since_1970 // 1) #finds the absolute of the variable 'days_since_1970'
    #print(abs_days_since_1970)

    year = 1970 #richard nixon is in the white house

    #basically the logic for the following code is as such:
    #whilst the number of days since 1970 is greater than 366,
    #find out if the year (starting in 1970, obviously) is a leap year
    #if so, subtract 366 from the day count
    #if not, subtract 365 days
    #once the day counter variable is less than 366,
    #find out if the last year is a leap year
    #if it isn't, subtract 365 days once more and add one to the year counter, thus leaving you with a year and day counter

    #why is the calender so fucking complicated!?
    #fuck you roman motherfuckers
    
    while abs_days_since_1970 > 366: 
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #is a leap year
            #print(year, "is a leap year")
            abs_days_since_1970 = abs_days_since_1970 - 366
        elif year % 4 == 0 and year % 100 == 0:
            #print(year, "is not a leap year")
            abs_days_since_1970 = abs_days_since_1970 - 365
        elif year % 4 == 0: #is a leap year
            #print(year, "is a leap year")
            abs_days_since_1970 = abs_days_since_1970 - 366
        elif year % 4 != 0:
            #print(year, "is not a leap year")
            abs_days_since_1970 = abs_days_since_1970 - 365

        #print(abs_days_since_1970)
        year = year + 1
    else:
        if abs_days_since_1970 >= 365:
            if year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #is a leap year
                pass
            elif year % 4 == 0 and year % 100 == 0:
                abs_days_since_1970 = abs_days_since_1970 - 365
            elif year % 4 == 0: #is a leap year
                pass
            elif year % 4 != 0:
                abs_days_since_1970 = abs_days_since_1970 - 365

    #print("The year is: " + str(year)) #just keeping the user up to date with 
    #print("We are " + str(abs_days_since_1970) + " days into " + str(year))

    if return_leap_or_no(year) == True:
        days_for_each_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_for_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    months_of_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    current_month = 0 #0 for january, 1 for february... 11 for december

    while days_for_each_month[current_month] < abs_days_since_1970:
        abs_days_since_1970 = abs_days_since_1970 - days_for_each_month[current_month]
        current_month = current_month + 1

    #print("It is " + str(abs_days_since_1970 + 1) + " of " + months_of_the_year[current_month])

    sub_day_value = find_decimal_number(days_since_1970)
    hour_number = sub_day_value * 24

    sub_hour_value = find_decimal_number(hour_number)
    minute_number = sub_hour_value * 60

    abs_hour_number = str(int(hour_number // 1))
    abs_minute_number = str(int(minute_number // 1))

    if len(abs_minute_number) == 1:
        abs_minute_number = "0" + abs_minute_number

    if len(abs_hour_number) == 1:
        abs_hour_number = "0" + abs_hour_number

    abs_days_since_1970 = str(abs_days_since_1970 + 1)
    current_month = str(current_month + 1)

    if len(abs_days_since_1970) == 1:
        abs_days_since_1970 = "0" + abs_days_since_1970

    if len(current_month) == 1:
        current_month = "0" + current_month

    total_string = abs_hour_number + ":" + abs_minute_number + " " + abs_days_since_1970 + "/" + current_month + "/" + str(year) + " UTC"

    return total_string
