#!/usr/bin/env python
# coding: utf-8

# # Task3

# In[1]:


import re
import csv
with open('calls_copy.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

code_dict = dict()
bng_calls_recieved = 0

for row in calls:
    word= re.search('\(\d[0-9]*\)',row[0])
    word1 = re.search('\(\d[0-9]*\)',row[1])
    if word1 is not None and word1.group() == '(080)' :
        bng_calls_recieved += 1
    if word is not None and word.group() == '(080)' :
        if word1 is not None:
            if word1.group() not in code_dict:
                code_dict[word1.group()] = 1
            else:
                code_dict[word1.group()] = code_dict[word1.group()]+1
                
#print("The telephone codes being called to, by the Banaglore '080' fixed line are following:", code_dict)
#print("\nCalls recieved by Bangalore fixed line number:", bng_calls_recieved)
print("\nCalls made from Bangalore fixed line:",code_dict['(080)'], "\n% calls from fixed line in BNG to fixed line in BNG :",code_dict['(080)']/bng_calls_recieved *100)


# In[ ]:




