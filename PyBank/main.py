



''' 
/python-challenge/PyBank/main.py
1.1 Open the csv
1.2 Define the variables: 
        prev_month (in case of exists duplicates)
        month_count = get the total number of months
        total_amount = sum the total amount of "Profit/Losses"
1.2.1 To get the changes:
        prev_value = the prev row
        value = current value
        change = (prev_value - value)
        total_change = sum of changes
1.2.2 To get the greates_inc & greatest_dec will be use a conditional.
        greatest_inc 
        greatest_dec

'''
#1.2
import csv
import os

month=0
prev_month = None
months_count = 0
total_amount=0
value = 0
row_number=0
prev_value = 0
total_change = 0
greatest_inc= 0
greatest_dec= 0
lowest_month = None
 

#1.1
#with open ('/Users/breeze/Desktop/BootCamp/Bootcamp/Challenges/Python-Challenge/python-challenge/PyBank/Resources/budget_data.csv',mode='r',encoding= 'UTF-8') as csv_file:
with open ('.''/Resources/budget_data.csv',mode='r',encoding= 'UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # 1.3 Calculate the total number of months included in the dataset
        for row in csv_reader:
                row_number+=1
                month= row['Date']
                amount = row['Profit/Losses']

                if prev_month != None or prev_month!= month:
                        months_count +=1
                        # 1.4 Calculate the net total amount of "Profit/Losses" over the entire period
                        total_amount +=int(amount)
                prev_month = month

                # 1.5 Calcuate the changes in "Profit/Losses" over the entired period. 
                if row_number>2:
       
                        value= int(row['Profit/Losses'])
                        change= value - prev_value
                        total_change+= change
                        # 1.7 Calculate the greatest increase in profits(date and amount) over the entire period        
                        if 0< change >= greatest_inc:
                                greatest_month= month
                                greatest_inc= change
                        # 1.8 Calculate the greates decrease in profits (date and amount) over the entire period
                        elif greatest_dec > change :
                                lowest_month= month
                                greatest_dec= change
                elif row_number==1:
                        value= int(row['Profit/Losses'])
                        
                prev_value = int(value)
# 1.6 Calculate the average of those changes
if prev_value != None:
        avg_change= total_change/(months_count-1)


# 1.9 Print the result 

result=f'''Financial Analysis
-----------------------------------------------
     
Total Months: {int(months_count)}
Total: $ {"{:,}".format(total_amount)}
Average Change: ${"{:,.2f}".format(avg_change)}
Greatest Increase in Profit : {greatest_month}  (${"{:,}".format(greatest_inc)})
Greatest Decrease in Profit : {lowest_month}   (${"{:,}".format(greatest_dec)})
      '''
print(result)

# 7. Export the result to txt file

with open('PyBank_Results.txt',mode= 'w', encoding='UTF-8') as csv_file:
        csv_file.write(result)
