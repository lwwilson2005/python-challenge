
# coding: utf-8

# In[56]:


import os
import csv
from datetime import datetime


# In[57]:


budgetcsv = os.path.join('budget_data_2.csv')
budgetcsv
file_results = budgetcsv.split(".")
filename = file_results[0]
print(filename)


# In[58]:


date = []
revenue = []
revincrease = 0
currentmonth = 0
prevmonth = 0
revincr_ndx = 0
revdecr_ndx = 0
gr_rev_incr = 0
gr_rev_decr = 0
delta_rev = 0
avg_chg = 0


# In[59]:


rownum = 0
with open(budgetcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if rownum == 0 and row[1] == "Revenue":
            header = row
            print(header)
        else:
            date.append(row[0])
            revenue.append(float(row[1]))
        


# In[60]:


tot_rev = sum(revenue)
tot_periods = len(date)
avg_chg = round(tot_rev/tot_periods)
#print(tot_rev, tot_periods, round(tot_rev/tot_periods,2))


# In[61]:


i = 0
while i <= tot_periods-1:
    currentmonth = revenue[i]
    if  currentmonth - prevmonth >= gr_rev_incr:
        gr_rev_incr = currentmonth - prevmonth
        revincr_ndx = i
    elif currentmonth - prevmonth <= gr_rev_decr:
        gr_rev_decr = currentmonth - prevmonth
        revdecr_ndx = i
    prevmonth = currentmonth
    delta_rev = delta_rev + currentmonth
    i = i+1
#print(date[revincr_ndx], gr_rev_incr)
#print(date[revdecr_ndx], gr_rev_decr)
#print(round(delta_rev/tot_periods,2))


# In[62]:


o_line = []
o_line.append("Financial Analysis for " + filename)
o_line.append("_________________________________")
o_line.append("Total Months: " +str(tot_periods))
o_line.append("Total Revenue: " + str(tot_rev))
o_line.append("Average Revenue Change: " + str(avg_chg))
o_line.append("Greatest Increase in Revenue: " + str(date[revincr_ndx]) + "   " + str(round(gr_rev_incr,2)))
o_line.append("Greatest Decrease in Revenue: " + str(date[revdecr_ndx]) + "   " + str(round(gr_rev_decr,2)))
print(o_line[0])
print(o_line[1])
print(o_line[2])
print(o_line[3])
print(o_line[4])
print(o_line[5])
print(o_line[6])
#print("Financial Analysis for ", filename)
#print("_________________________________")
#print("Total Months: ", tot_periods)
#print("Total Revenue: ", tot_rev)
#print("Average Revenue Change: ", avg_chg)
#print("Greatest Increase in Revenue: ",date[revincr_ndx], round(gr_rev_incr,2))

#print("Greatest Decrease in Revenue: ",date[revdecr_ndx], round(gr_rev_decr,2))


# In[63]:


#with open(filename + ".txt", "w", newline = "") as f:
#    f.write(o_line[0])
#    f.write(o_line[1])
#    f.write(o_line[2])
#    f.write(o_line[3])
#    f.write(o_line[4])
#    f.write(o_line[5])

#    f.write(o_line[6])
outputfile = os.path.join(filename + ".txt")
with open(outputfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow([o_line[0]])
    writer.writerow([o_line[1]])
    writer.writerow([o_line[2]])
    writer.writerow([o_line[3]])
    writer.writerow([o_line[4]])
    writer.writerow([o_line[5]])
    writer.writerow([o_line[6]])
    
date_object = datetime.now()
current_time = date_object.strftime('%H:%M:%S')
print("process complete: " + current_time)

