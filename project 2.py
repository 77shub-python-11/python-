#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd 


# In[11]:


#project 2

#2. Create a Data Base of 25 employe with:
#Name Age Gender Experience Salary expertise(python:py,java:ja,GoLang:GL)
#Make one person salary 4500000/- other employee should not exceed more then 15 lac
#By take Input from user for each employee
#1.Print head
#2.Print Tail
#3.Print whole Data Frame
#Save the above data frame to csv in the same folder.(use pandas )

#3. Import the above data base by read csv (use pandas)
#Now make 2 cell None in each: salary,gender,expertise,age make sure they are in different rows.
#Now handle these null values.
#Fill these null Values
#And find out the following

#1.Who is in majority in company Male  or False
#2.which employee has the highest salary
#3.what is the average salary,average age
#4.which is the highest expertise in all 3 categories
#5.Is there any out Liner in Salary 
#6.What are the other inside you are getting from Data Base.



# In[5]:


c=[]#names of  empl
d=[]#age of empl
g=[]#gender of empl
x=[]#experience
s=[]#salary 
w=[]#expertise
i=int(input("enter no elements u would like  enter : "))
while i > 0:
    a=input("enter names : ")
    b=int(input("Age  : "))
    f=input("Gender : ")
    y=int(input("experience : "))
    h=int(input("Salary :"))
    z=input("Expertise in py,ja,gl")
    w.append(z)
    s.append(h)
    x.append(y)
    g.append(f)
    c.append(a)
    d.append(b)
    
    i=i-1
e={"names":c,"Age ":d,"Gender ":g,"experience":x,"salary":s,"expertise":w}
ds=pd.DataFrame(e)
ds


# In[3]:


ds2=pd.read_csv("ds.csv")


# In[4]:


ds2


# In[6]:


ds2.head()


# In[7]:


ds2.tail()


# In[8]:


ds3=ds2


# In[9]:


ds4=ds3.reindex(index=("a","b")+(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24))


# In[10]:


ds4#created new rows with null value


# In[ ]:




