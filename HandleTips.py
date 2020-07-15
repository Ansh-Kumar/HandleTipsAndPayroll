# Handle Tips and Payroll
# HandleTips.py

import os
import csv
import datetime

# "/Users/anshkumar/Downloads/shifts-export_2020-07-01_2020-07-15.csv"

def getResources():
    # Get the paths to the specific file.
    # Add them to a list.
    # Return the list
    paths = []
    print("Please enter the path for the shift export file: ")
    pathShift = input()
    print("Please enter the path for the transaction export file: ")
    pathTransaction = input()
    paths.append(pathShift)
    paths.append(pathTransaction)
    return paths

    
def sendResources():
    resources = getResources()
    shiftP = resources[0]
    transP = resources[1]
    shiftStatus = checkPath(shiftP)
    transStatus = checkPath(transP)
    if shiftStatus == True and transStatus == True:
        return resources

def checkPath(path):
    if os.path.exists(path):
        return True
    else:
        return False

def handleDateTime(value):
    wholeThing = []
    hourL = []
    minL = []
    secL = []
    # TOD is time of day (AM/PM)
    todL = []
    # determine hour
    for x in value:
        if x != ":":
            wholeThing.append(x)
    wholeThing.remove(" ")
    for x in range(5):
        wholeThing.pop()
    if len(wholeThing) == 6:
        wholeThing.insert(0, "0")
    hourS = wholeThing[0] + wholeThing[1]
    minuteS = wholeThing[2] + wholeThing[3]
    secondS = wholeThing[4] + wholeThing[5]
    tod = wholeThing[6]
    hour = int(hourS)
    minute = int(minuteS)
    second = int(secondS)
    if tod == "P":
        hour += 12
    hourS = str(hour)
    whole = hourS + minuteS + secondS
    return whole

def convertToSec(value):
    timeA = handleDateTime(value)
    timeL = list(timeA)
    if len(timeL) == 5:
        timeL.insert(0, "0")
    hourS = timeL[0] + timeL[1]
    minuteS = timeL[2] + timeL[3]
    secondS = timeL[4] + timeL[5]
    hour = int(hourS)
    minute = int(minuteS)
    second = int(secondS)
    time = (hour*3600) + (minute*60) + second
    return time

def convertTimeElapsed(seconds):
    hour = int(seconds/3600)
    minute = int((seconds-(3600*hour))/60)
    second = int((seconds - (3600*hour)-(minute*60)))
    print(hour, minute, second)

def openShift():
    resources = sendResources()
    with open(resources[0], mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        lineCount = 0
        for row in csv_reader:
            if lineCount == 0:
                lineCount += 1
                continue
            else:
                if row[1] != "":
                    print("Name: ", row[1])
                    print("Date: ", row[4])
                    print("Start Time: ", row[5])
                    print("End Time: ", row[7])
                    startN = row[5]
                    endN = row[7]
                    start = convertToSec(startN)
                    end = convertToSec(endN)
                    timeElapsed = end-start
                    timeElapsed = convertTimeElapsed(timeElapsed)
                    print(timeElapsed)
