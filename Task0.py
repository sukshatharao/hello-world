#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
csvfile = pd.read_csv("calls_copy.csv", names=["calling_no", "recieving_no", "call_timestamp", "duration"]);
print(csvfile.tail(1));
call_calling = csvfile.calling_no
call_recieving = csvfile.recieving_no
call_duration= csvfile.duration
csvfile1 = pd.read_csv("texts.csv", names=["sending_no", "recieving_no", "msg_timestamp"]);
print(csvfile1.head(1));
text_sending = csvfile1.sending_no
text_recieving = csvfile1.recieving_no


# In[ ]:





# In[ ]:





# In[ ]:




