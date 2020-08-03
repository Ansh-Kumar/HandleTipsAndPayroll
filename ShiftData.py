# Handle Tips and Payroll Pt 1 - Shift Data
# ShiftData.py

import os
import csv
import datetime
import time

# "/Users/anshkumar/Downloads/shifts-export_2020-07-16_2020-07-31.csv"

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
            data = []
            if lineCount == 0:
                lineCount += 1
            else:
                data.append(row[1])
                data.append(handleHrs(row[13]))
                dataF.append(data)
        return dataF

def handleHrs(stringHrs):
    hours = float(stringHrs)
    hours = simplifyHours(hours)
    return hours



def simplifyHours(totalHour):
    hourString = str(totalHour)
    intHour = int(totalHour)
    intDeci = totalHour - intHour
    if intDeci >= 0 and intDeci < .13:
        intDeci = 0
    elif intDeci >= .13 and intDeci <= .38:
        intDeci = 0.25
    elif intDeci > .38 and intDeci <= .63:
        intDeci = 0.5
    elif intDeci > .63 and intDeci < .88:
        intDeci = 0.75
    else:
        intDeci = 1
    totalHourRtrn = intHour + intDeci
    return totalHourRtrn

def calcPay(employeeName, totalHrs):
    if employeeName == "Tam" or employeeName == "Nico":
        pay = totalHrs * 13
    elif employeeName == "Lynn":
        pay = totalHrs * 16
    elif employeeName == "Ansh":
        pay = totalHrs * 7
    else:
        pay = 0
    return pay

def data():
    dataF = openShift()
    anshHours = 0
    lynHours = 0
    nicoHours = 0
    tamHours = 0
    for x in dataF:
        if x[0] == "Ansh":
            anshHours += x[1]
        elif x[0] == "Lynn":
            lynHours += x[1]
        elif x[0] == "Tam":
            tamHours += x[1]
        elif x[0] == "Nico":
            nicoHours += x[1]
        else:
            continue
    anshPay = calcPay("Ansh", anshHours)
    lynPay = calcPay("Lynn", lynHours)
    tamPay = calcPay("Tam", tamHours)
    nicoPay = calcPay("Nico", nicoHours)

    anshRow = ["Ansh"]
    anshRow.append(anshHours)
    anshRow.append(anshPay)
    lynRow = ["Lynn"]
    lynRow.append(lynHours)
    lynRow.append(lynPay)
    tamRow = ["Tam"]
    tamRow.append(tamHours)
    tamRow.append(tamPay)
    nicoRow = ["Nico"]
    nicoRow.append(nicoHours)
    nicoRow.append(nicoPay)

    dataF = []

    dataF.append(anshRow)
    dataF.append(lynRow)
    dataF.append(tamRow)
    dataF.append(nicoRow)

    return dataF

def shiftFinal():
    dataFull = data()
    date = datetime.date.today().strftime("%m%d%y")
    newFileName = "ShiftReports" + date + ".csv"
    with open(newFileName, mode = "w", newline='') as csv_file:
        columnNames = ["Name", "Total Hours", "Total Pay"]
        writer = csv.writer(csv_file)

        writer.writerow(columnNames)
        writer.writerows(dataFull)

