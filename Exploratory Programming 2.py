#!/usr/bin/env python
# coding: utf-8

# In[21]:


fingers = [-2 ,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[22]:


print fingers


# In[26]:


def positive():
    positive() >= 1


# In[30]:


def negative():
    negative() <= -1


# In[ ]:


# made function that returns true for each positive number


# In[38]:


def bepositive(sequence):
    result = [sequence]
    for positive in sequence:
        print "true"
    return result


# In[ ]:





# In[39]:


bepositive(fingers)


# In[ ]:


#attempting and failing to create a function that removes negatives from the list


# In[50]:


def howpositive(sequence):
    result = [sequence]
    for negative in sequence:
        set(sequence) >= 1
    return result


# In[52]:


howpositive(fingers)

