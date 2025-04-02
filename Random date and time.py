import random
import time

def giverandomdate(startdate,enddate):
    print("Giving output of random date between ",startdate," and ",enddate)
    randomgen= random.random()
    date= "%d/%m/%Y"

    startingtime= time.mktime(time.strptime(startdate,date))
    endingtime=time.mktime(time.strptime(enddate,date))

    randomtime= startingtime+randomgen *(endingtime-startingtime)
    randomdate= time.strftime(date,time.localtime(randomtime))
    return randomdate

print("randomdate = ",giverandomdate("1/1/2000","1/1/2005"))
