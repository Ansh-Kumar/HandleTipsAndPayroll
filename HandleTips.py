# Handle Tips and Payroll
# HandleTips.py

import os
import csv


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
    print(shiftStatus, transStatus)
    if shiftStatus == True and transStatus == True:
        return resources

def checkPath(path):
    if os.path.exists(path):
        return True
    else:
        return False

'''
def openShift():
    with open()
'''
