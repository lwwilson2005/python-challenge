
# coding: utf-8

# In[1]:


import os
import csv
from datetime import datetime


# In[2]:


emp1 = os.path.join('employee_data1.csv')
emp1
file_results =emp1.split(".")
file1 = file_results[0]
emp2 = os.path.join('employee_data2.csv')
emp2
file_results =emp2.split(".")
file2 = file_results[0]
print(file1, file2)


# In[3]:


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[4]:


empid = []
name = []
dateofbirth = []
socsecnum = []
state = []
fname = []
lname = []

rownum = 0


# In[5]:


rownum = 0
with open(emp1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        #print(row[0])
        if rownum == 0 and row[0] == "Emp ID":
            header = row
            rownum +=1
            
            print(header)
        else:
            empid.append(row[0])
            name.append(row[1])
            dateofbirth.append(row[2])
            socsecnum.append(row[3])
            state.append(row[4])
            #print(row)
rownum = 0
with open(emp2, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        #print(row[0])
        if rownum == 0 and row[0] == "Emp ID":
            header = row
            rownum +=1
            
            #print(header)
        else:
            empid.append(row[0])
            name.append(row[1])
            dateofbirth.append(row[2])
            socsecnum.append(row[3])
            state.append(row[4])
            #print(row)
   


# In[6]:


i = 0
ssn = []
dob = []
st = []
print(len(empid))
while i <= len(empid)-1:
    #
    #separate the name
    fn = name[i].split(" ")
    fn2 = str(name[i])
    fn3 = fn2.split()[0]
    fn4 = fn2.split()[-1]
    fname.append(fn3)
    lname.append(fn4)
    #ssn tranformation
    ssntemp = str(socsecnum[i])
    ssn.append('***-**-'+ssntemp.split("-")[-1])
    #date of birth transformation
    dobtemp = str(dateofbirth[i])
    #db2 = dobtemp.split("-")[1]+'/'+dobtemp.split("-")[2]+'/'+dobtemp.split("-")[0]
    dob.append(dobtemp.split("-")[1]+'/'+dobtemp.split("-")[2]+'/'+dobtemp.split("-")[0])
    #time to work on the state
    st.append(us_state_abbrev[state[i]])
    #print(empid[i],name[i])
    i+=1
    


# In[7]:


cleanedcsv = zip(empid,fname,lname,dob,ssn,st)
outputfile = os.path.join("Employee_NF.csv")
csvheader = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
with open(outputfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(csvheader)
    writer.writerows(cleanedcsv)





# In[8]:


date_object = datetime.now()
current_time = date_object.strftime('%H:%M:%S')
print("process complete: " + current_time)

