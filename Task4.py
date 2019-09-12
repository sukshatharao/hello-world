#!/usr/bin/env python
# coding: utf-8

# # Task4
# 

# In[1]:


import re
import csv
with open('calls_copy.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

with open('texts.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    texts = list(reader1)

tele_list = []
for r1 in calls:
    word = re.search('^140', r1[0])
    word1 = re.search('^140', r1[1])
    if word is not None and r1[0] not in tele_list :
        tele_list.append(r1[0])
    if word1 is not None and r1[1] in tele_list:
        tele_list.remove(r1[1])

for r2 in texts:
    word2 = re.search('^140', r2[0])
    word3 = re.search('^140', r2[1])
    if word2 is not None and r2[0] in tele_list :
        tele_list.remove(r2[0])
    if word3 is not None and r2[1] in tele_list:
        tele_list.remove(r2[1])
print("\nThe list of telemarketers are: " , tele_list)


# In[ ]:




