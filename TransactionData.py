# Handle Tips and Payroll
# TransactionData.py

import os
import csv
import datetime
import time
import ShiftData as sd


def sendResources():
    print("Please enter the path for the transaction export file")
    path = input()
    pathStatus = sd.checkPath(path)
    while not pathStatus:
        pathStatus = sd.checkPath(path)
        print("Wrong path")
        path = input()
    return path


def readData():
    file = sendResources()
    with open(file, mode='r') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter = ',')
        lineCount = 0
        tipData = []
        for row in csv_reader:
            if lineCount == 0:
                lineCount += 1
                continue
            else:
                tipData.append(row[8])
    return tipData
                
def fixData():
    data = readData()
    dataFixed = []
    for x in data:
        y = x.replace("$","")
        y = float(y)
        dataFixed.append(y)
    return sum(dataFixed)


def transactionFinal():
    totalTip = fixData()
    date = datetime.date.today().strftime("%m%d%y")
    fileName = "TransactionReports" + date + ".csv"
    ansh = round(totalTip*0.05, 2)
    employeeTotalTip = round(totalTip * 0.95, 2)
    individualTip = round(employeeTotalTip/4, 2)
    employee = ["Ansh", "Juan", "Lynn", "Nico", "Tam", "Total"]
    finalList = []
    for x in employee:
        lst = []
        if x == "Ansh":
            lst = [x, ansh]
        elif x == "Total":
            lst = [x, totalTip]
        else:
            lst = [x, individualTip]
        finalList.append(lst)
    print(finalList)
    with open(fileName, mode='w', newline='') as csv_file:
        columnNames = ["Name", "Tip Recieved"]
        writer = csv.writer(csv_file)

        writer.writerow(columnNames)
        writer.writerows(finalList)
