##########################################################################################
######## Generate a list of dates between a given start date and a given end date ########
##########################################################################################

from datetime import date, timedelta

def getdates(start_date, end_date):
    '''
    start_date, end_date: date objects
    return datelist: list of dates
    '''
    datelist = [start_date]
    while start_date != end_date:
        start_date += timedelta(days = 1)
        datelist.append(start_date)
    return datelist
