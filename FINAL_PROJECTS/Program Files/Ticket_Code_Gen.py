from datetime import datetime
from string import *
from random import *

def Gen_Code():
    date_time = datetime. now()
    todays_date = date_time.date()
    print(todays_date)
    todays_date = list(str(todays_date))

    corrected_date = ""
    for i in todays_date:
        if i in punctuation :
            pass
        else :
            corrected_date = corrected_date + i
            
    corrected_date = list(corrected_date)
    yyyy =  corrected_date[0:4]
    mm =  corrected_date[4:6]
    dd = corrected_date[6:8]
    corrected_date = []
    corrected_date.extend(dd)
    corrected_date.extend(mm)
    corrected_date.extend(yyyy)

    corrected_date_ = ""

    for i in corrected_date :
        corrected_date_ = corrected_date_ + i
        
    print(corrected_date_)

    sec = list(ascii_letters)
    rand_elem = sample(sec, 8)
    rand_code = "".join(map(str,rand_elem))

    ticket_code = corrected_date_ + rand_code
    return ticket_code

def return_date_time(millisecond = False):
    if millisecond == True :
        now_time = str(datetime. now())
        return now_time
    else:
        now_time = str(datetime. now()).split(".")
        return now_time[0]
    

