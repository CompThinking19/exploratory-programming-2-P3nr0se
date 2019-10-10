#!/usr/bin/env python
# coding: utf-8

# In[3]:


fingers = [-2 ,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[4]:


print fingers


# In[5]:


x = len(fingers)


# In[6]:


print x


# In[77]:


def positive(list):
   positive is float in list > 0


# In[82]:


#This function will run only if there is no negative in the list. I'm notably having trouble creating a function that will create a list of exclusively positive numbers


# In[78]:


def howpositive(list):
    y = []
    for element in list:
        if (element < 0):
            raise TypeError("No negativity!")
    for element in list:
        if (element > 0):
            print element
    
    


# In[79]:


howpositive(fingers)


# In[80]:


hand = [1, 2, 3, 4, 5]


# In[81]:


howpositive(hand)

