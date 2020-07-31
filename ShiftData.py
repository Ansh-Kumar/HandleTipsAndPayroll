# Handle Tips and Payroll Pt 1 - Shift Data
# ShiftData.py

import os
import csv
import datetime
import time

# "/Users/anshkumar/Downloads/shifts-export_2020-07-01_2020-07-15.csv"

def getResources():
    paths = []
    print("Please enter the path for the shift export file: ")
    pathShift = input()
    paths.append(pathShift)
    return paths

    
def sendResources():
    resources = getResources()
    shiftP = resources[0]
    shiftStatus = checkPath(shiftP)
    if shiftStatus == True:
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
    timeRtrn = str(hour) + ":" + str(minute)
    return timeRtrn

def openShift():
    resources = sendResources()
    with open(resources[0], mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        lineCount = 0
        data = []
        dataF = []
        for row in csv_reader:
            if lineCount == 0:
                lineCount += 1
                continue
            else:
                if row[1] != "":
                    data.append(row[1])
                    data.append(row[4])
                    data.append(row[5])
                    data.append(row[7])
                    startN = row[5]
                    endN = row[7]
                    start = convertToSec(startN)
                    end = convertToSec(endN)
                    timeElapsed = end-start
                    timeElapsed = convertTimeElapsed(timeElapsed)
                    data.append(timeElapsed)
            dataF.append(data)
            data = []
        dataF.pop()
    return dataF

def data():
    data = openShift()
    anshHours = 0
    lynnHours = 0
    nicoHours = 0
    tamHours = 0
    juanHours = 0
    for row in data:
        if row[0] == "Ansh":
            hoursS = row[4]
            hours = int(hoursS[0])
            minuteS = hoursS[2] + hoursS[3]
            minute = int(minuteS)
            anshHours += hours + (minute/60)
        elif row[0] == "Lynn":
            hoursS = row[4]
            hours = int(hoursS[0])
            minuteS = hoursS[2] + hoursS[3]
            minute = int(minuteS)
            lynnHours += hours + (minute/60)
        elif row[0] == "Tam":
            hoursS = row[4]
            hours = int(hoursS[0])
            minuteS = hoursS[2] + hoursS[3]
            minute = int(minuteS)
            tamHours += hours + (minute/60)
        elif row[0] == "Nico":
            hoursS = row[4]
            hours = int(hoursS[0])
            minuteS = hoursS[2] + hoursS[3]
            minute = int(minuteS)
            nicoHours += hours + (minute/60)
        else:
            hoursS = row[4]
            hours = int(hoursS[0])
            minuteS = hoursS[2] + hoursS[3]
            minute = int(minuteS)
            juanHours += hours + (minute/60)
    lstHours = []
    anshHours = simplifyHours(anshHours)
    lynnHours = simplifyHours(lynnHours)
    tamHours = simplifyHours(tamHours)
    nicoHours = simplifyHours(nicoHours)
    lstHours.append(anshHours)
    lstHours.append(lynnHours)
    lstHours.append(tamHours)
    lstHours.append(nicoHours)
    lstHours.append(juanHours)
    fullData = findTotalPay(lstHours)
    return fullData

def simplifyHours(totalHour):
    hourString = str(totalHour)
    decimalPart = hourString[-2:]
    intHour = int(totalHour)
    intDeci = int(decimalPart)
    if intDeci >= 0 and intDeci < 13:
        intDeci = 0
    elif intDeci >= 13 and intDeci <= 38:
        intDeci = 0.25
    elif intDeci > 38 and intDeci <= 63:
        intDeci = 0.5
    elif intDeci > 63 and intDeci < 88:
        intDeci = 0.75
    else:
        intDeci = 1
    totalHourRtrn = intHour + intDeci
    return totalHourRtrn

def findTotalPay(Hours):
    anshHours = Hours[0]
    lynnHours = Hours[1]
    tamHours = Hours[2]
    nicoHours = Hours[3]
    juanHours = Hours[4]
    anshPay = anshHours * 7
    lynnPay = lynnHours * 16
    tamPay = tamHours * 13
    nicoPay = nicoHours * 13

    data = []
    
    anshRow = ["Ansh"]
    anshRow.append(anshHours)
    anshRow.append(anshPay)
    data.append(anshRow)

    lynnRow = ["Lynn"]
    lynnRow.append(lynnHours)
    lynnRow.append(lynnPay)
    data.append(lynnRow)

    tamRow = ["Tam"]
    tamRow.append(tamHours)
    tamRow.append(tamPay)
    data.append(tamRow)

    nicoRow = ["Nico"]
    nicoRow.append(nicoHours)
    nicoRow.append(nicoPay)
    data.append(nicoRow)

    return data

def shiftFinal():
    dataFull = data()
    date = datetime.date.today().strftime("%m%d%y")
    newFileName = "ShiftReports" + date + ".csv"
    with open(newFileName, mode = "w", newline='') as csv_file:
        columnNames = ["Name", "Total Hours", "Total Pay"]
        writer = csv.writer(csv_file)

        writer.writerow(columnNames)
        writer.writerows(dataFull)

