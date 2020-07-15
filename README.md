# HandleTipsAndPayroll
## Story
Conroy's Flowers Redondo Beach recently switched its walk-in transactions technology from BMS to Square. However, when seeing some of the features that Square offers and realizing the extra cost of these features left me to wonder if there was yet an easier way.
## Problem
As you may have realized, the problem found in this was me trying to find a cheaper alternative to handling the data found in each reciept and then calculating pay and tips data from the data.
## Solution
As a Computer Scientist, I realized that I could ask for the data as a CSV file which is in reality just a bunch of goop. So I could read through the data, find the important parts and then calculate all the information needed and present this in a much simpler CSV file which organizes all the important content and displays it.

# The Original Plan
Thinking about this problem and possible solution I wrote a couple of ideas and a basic structure for this program. The end result will obviously be a lot more complex but this gives the rough Idea.
## Goals
### Overall
Create Python Code that will handle all tips and payroll through CSV transactions from Square
### Function 1 
Edit shift data and fix
### Function 2 
Edit transaction data and fix
### Function 3
Calculate Payroll
## Parameters
### Overall
Shift Export and Transaction Export
### Function 1 
Shift Export
### Function 2 
Transaction Export
### Function 3
Shift Export
## Return
### Overall
A CSV File 

4 columns: Name, Calculated Tip Total, Calculated Payroll Total, Calculated Grand Total
### Function 1 
A CSV File

5 columns: Name, Date, Start Time, End Time, Total Time per Employee
### Function 2 
A CSV File

2 columns: Name, Total Tip
