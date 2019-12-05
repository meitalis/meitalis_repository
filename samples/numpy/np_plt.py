#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


np.random.seed(0)
np.random.randint(10,20,(3,2))


# In[7]:


np.random.random_sample(10)


# In[6]:


np.random.random_sample((3,2))


# In[43]:


aa = np.random.random_sample(10)
aa


# In[44]:


a,b = 10,20
aa = a + (b-a)*aa


# In[45]:


aa


# In[46]:


plt.plot(aa)


# In[57]:


_ = plt.hist(aa,bins=20)


# In[58]:


bb = np.random.randint(2, 10, 3)


# In[59]:


bb


# In[62]:


a = np.array([1,2,0,-1,1])
np.random.choice(a)


# In[64]:


a = np.array([1,2,0,-1,1])
np.random.choice(a,6)


# In[83]:


a = np.array([1,2,0,-1,1])
b = np.random.choice(a,(2,2))
print(b)
print(a)


# In[92]:


a = np.array([1,2,0,-1,1])
b = np.random.choice(a,5,p=[0.1,0.1,0.1,0.7,0])
b


# In[102]:


plt.hist(b,color="pink")


# In[118]:


print(a)
b = np.random.permutation(a)
print(a)
print(b)


# In[139]:


a = np.random.normal(80,10,100)


# In[159]:


a = np.random.poisson(5.5,24)
a


# In[161]:


plt.hist(a,bins = 24)


# In[ ]:





# In[ ]:




