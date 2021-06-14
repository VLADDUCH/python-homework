#Python home
import pandas as pd
import statistics
#PyBank pseudocoding
#Your task is to create a Python script that analyzes the records to calculate each of the following:
                #Variables
                                  
TM = "Total Months" 
TP = "Total profits"
AC = "Average Change"
GIP = "Greatest Increase in Profits"
GDP = "Greatest Decrease in Profits"


#IC = pd.read_csv('.csv')
#print(df.to_string()) 


#The total number of months included in the dataset.
#use len for months the company records. iehhhhhhhhhhhhhhhhhhhhhhhhhhh
#len (monthly_records - nomonthly_records)

#The net total amount of Profit/Losses over the entire period.
#ie profit= inser data set 
#TM = (IC)
#x= sum (TM)

#The average of the changes in Profit/Losses over the entire period.
#import statictics 
#print(statistics.mean(IC[]))

#The greatest increase in profits (date and amount) over the entire period.
#GIP= max (IC)
#print GIP

#The greatest decrease in losses (date and amount) over the entire period.
#GDP = min (IC)
#print GDP

#Your resulting analysis should look similar to the following:
#Financial Analysis
#----------------------------
print ("Total Months: " + TM)
print ("Total: " + T)
print ("Average Change: " + AC)
print ("Greatest Increase in Profits: " + GIP)
print ("Greatest Decrease in Profits: " + GDP)
#Your final script should print the analysis to the terminal and export a text file with the results.
#References https://www.w3schools.com/python/python_reference.asp