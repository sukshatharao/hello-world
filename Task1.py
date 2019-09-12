#!/usr/bin/env python
# coding: utf-8

# # Task 1 - Implementation 1st -way

# In[2]:


import csv
with open('calls_copy.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

output_arr = set()

for row in calls:
    output_arr.add(row[0])
    output_arr.add(row[1])

total_unique_tel_numbers = len(output_arr)
#print(output_arr)
print("There are ",total_unique_tel_numbers ," different telephone numbers in the call records.")       


# # Task 1 - Implementation 2nd -way

# In[8]:


import pandas as pd
csvfile = pd.read_csv("calls_copy.csv", names=["calling_no", "recieving_no", "call_timestamp", "duration"]);
call_calling = csvfile.calling_no
call_recieving = csvfile.recieving_no
csvfile1 = pd.read_csv("texts.csv", names=["sending_no", "recieving_no", "msg_timestamp"]);
text_sending = csvfile1.sending_no
text_recieving = csvfile1.recieving_no

arr_call = []
for row in call_calling: 
    if (row not in arr_call):
        arr_call.append(row) 
        
for row in call_recieving: 
    if (row not in arr_call): 
        arr_call.append(row)    

print("There are",len(arr_call),"different telephone numbers in the call records")

arr_text = []
for row in text_sending: 
    if (row not in arr_text):
        arr_text.append(row) 
        
for row in text_recieving: 
    if (row not in arr_text): 
        arr_text.append(row)    

print("There are",len(arr_text),"different telephone numbers in the text records")


# In[ ]:




