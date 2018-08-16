
# coding: utf-8

# In[1]:

name = "wonderwoman"

name = "superman"


# In[20]:


age = 99


# In[21]:


print(name)


# In[22]:


print(age)


# In[23]:


print("my name is")


# In[24]:


print("my name is",name)


# In[25]:


print("my age is",age)


# In[30]:


print("my name is", name,"and my age is",age)


# In[31]:


newage = age - 67


# In[32]:


multipliedage = age * 2


# In[33]:


print("your age is actually", newage)


# In[34]:


print("your multiplied age is",multipliedage)


# In[35]:


NewAge = 100


# In[36]:


newage = 50


# In[37]:


sequence = "CTAGCTAG"


# In[38]:


print(sequence)


# In[39]:


print(sequence[0])


# In[40]:


print(sequence[3])


# In[41]:


print("my fourth letter is", sequence[3])


# In[42]:


len(sequence)


# In[43]:


print("the length of the sequence is",len(sequence))


# In[44]:


COX1 = "CTAG"


# In[47]:


name = "Hideaki"


# In[48]:


first_name = "Hideaki"


# In[51]:


sequence[0:2]


# In[52]:


sequence[0:3]


# In[53]:


type(sequence)


# In[54]:


type(name)


# In[56]:


type(age)


# In[57]:


cox2 = "TACG"


# In[58]:


cox1 = "CTAG"


# In[60]:


cox1 + cox2


# In[61]:


firstname = "Hideaki"


# In[62]:


lastname = "Kato"


# In[63]:


firstname + lastname


# In[64]:


firstname + " " + lastname


# In[65]:


age


# In[66]:


len(age)


# In[67]:


name


# In[72]:


5**2


# In[74]:


print(5**2)


# In[75]:


print("5 square is",5**2)


# In[76]:


5**3


# In[77]:


5%2


# In[78]:


5/2


# In[80]:


#this is a comment


# In[81]:


#adding two sequences because  they turned out to be the same genes


# In[82]:


cox1 + cox2


# In[83]:


max(22,2,5)


# In[84]:


round(3.14232343434)


# In[85]:


round(3.1415243434,2)


# In[86]:


min(2,3,4)


# In[87]:


help(round)


# In[88]:


max(21,32,45)


# In[89]:


max(21,32,45) + min(21,32,45)


# In[90]:


hundred_C = "c" * 100


# In[91]:


print(hundred_C)


# In[92]:


hundred_C + cox1


# In[94]:


len(hundred_C + cox1)


# In[95]:


import math


# In[96]:


math.cos(180)


# In[97]:


math.sin(180)


# In[98]:


math.sin(3.14)


# In[99]:


math.pi


# In[101]:


math.sin(math.pi)


# In[102]:


math.cos(math.pi)


# In[103]:


help(math)


# In[107]:


math.cos(45)

import math as m
# In[108]:


import math as m


# In[109]:


m.cos(45)


# In[110]:


from math import cos


# In[111]:


cos(45)


# In[112]:


sin(45)


# In[113]:


m.sin(45)


# In[114]:


math.sin(45)


# In[115]:


from math import *


# In[116]:


print("sin(pi/2)=",sin(pi/2))


# In[117]:


from math import sin,pi


# In[118]:


print("sin(pi/2)=",sin(pi/2))


# In[119]:


print("sin(pi)=",sin(pi))


# In[120]:


from math import degrees,pi


# In[121]:


angle = degrees(pi/2)


# In[122]:


print(angle)


# In[123]:


import pandas


# In[124]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[125]:


pwd


# In[126]:


pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[129]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv")

print(data)
# In[130]:


print(data)


# In[131]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv", index_col="country")


# In[132]:


print(data)


# In[133]:


data


# In[134]:


data.info()


# In[135]:


data


# In[136]:


data.T


# In[137]:


age.T


# In[138]:


name.T


# In[139]:


data.T


# In[140]:


man type


# In[141]:


type.data


# In[142]:


data.type


# In[143]:


data.describe()


# In[144]:


data.T.describe()


# In[145]:


type(data)


# In[151]:


americas = pandas.read_csv("data/gapminder_gdp_americas.csv", index_col="country")


# In[152]:


americas


# In[153]:


americas.describe()


# In[154]:


americas.info()


# In[155]:


americas.describe()


# In[156]:


data.columns


# In[157]:


data.iloc[1,2]


# In[158]:


data


# In[159]:


data.iloc[0,0]


# In[160]:


data.loc["Australia", "gdpPercap_1952"]


# In[162]:


data.loc["Australia",:]


# In[166]:


data.loc[:,:]


# In[167]:


data.loc[:,"gdpPercap_1952"]


# In[168]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"]


# In[169]:


data.loc["Australia","gdpPercap_1952":"gdpPercap_1962"]


# In[170]:


data.iloc[0,0:2]


# In[171]:


data.iloc[:,0:2].max()


# In[172]:


data.iloc[:,0:3].max()


# In[174]:


subset = data.iloc[:,0:3]


# In[175]:


print(subset > 11000)


# In[177]:


subset[subset>11000]


# In[178]:


subset[subset>11000].describe()


# In[180]:


Europe = pandas.read_csv("data/gapminder_gdp_europe.csv")


# In[181]:


Europe


# In[185]:


Europe.iloc[22,12]


# In[187]:


Europe = pandas.read_csv("data/gapminder_gdp_europe.csv", index_col="country")


# In[189]:


Europe.loc["Serbia", "gdpPercap_2007"]


# In[190]:


Europe


# In[191]:


subset_Europe = Europe.loc["Italy":"Norway","gdpPercap_1962":"gdpPercap_1972"]


# In[192]:


subset[subset_Europe<15000].describe()


# In[193]:


subset_Europe


# In[196]:


subset_Europe[subset_Europe<15000].describe()

