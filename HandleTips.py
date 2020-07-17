# Handle Tips and Payroll
# HandleTips.py

import os
import csv
import datetime
import time
import ShiftData as shiftdata
import TransactionData as transdata

# "/Users/anshkumar/Downloads/shifts-export_2020-07-01_2020-07-15.csv"
# /Users/anshkumar/Downloads/transactions-2020-07-01-2020-07-16.csv

shiftdata.shiftFinal()
transdata.transactionFinal()
