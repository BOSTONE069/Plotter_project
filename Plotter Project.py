#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import cufflinks as cf
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


po.init_notebook_mode(connected=True)#this is to enable the making of plotly in offline mode
cf.go_offline()


# In[3]:


def createdata(data): #this is defining the creation of the data from the user input
    if(data == 1):
        x = np.random.rand(100,5)
        df1 = pd.DataFrame(x , columns =['A', 'B' , 'C' , 'D' , 'E'])
    elif(data == 2):
        x = [0,0,0,0,0]
        r1 = [0,0,0,0,0]
        r2 = [0,0,0,0,0]
        r3 = [0,0,0,0,0]
        r4 = [0,0,0,0,0]
        print('Please Enter the values for the columns')
        i=0
        for i in [0,1,2,3,4]: #this is a loop for creating the coulumns
            x[i] = input()
            i = i + 1
        print('Please Enter the values for the first row')
        i=0
        for i in [0,1,2,3,4]: #this is a loop for creating the rows
            r1[i] = int(input())
            i = i + 1
        print('Please Enter the values for the second row')
        i=0
        for i in [0,1,2,3,4]: #this is a loop for creating the rows
            r2[i] = int(input())
            i = i + 1
        print('Please Enter the values for the third row')
        i=0
        for i in [0,1,2,3,4]: #this is a loop for creating the rows
            r3[i] = int(input())
            i = i + 1
        print('Please Enter the values for the fourth row')
        i=0
        for i in [0,1,2,3,4]: #this is a loop for creating the rows
            r4[i] = int(input())
            i = i + 1
        df1 = pd.DataFrame([r1,r2,r3,r4] , columns = x)
    elif(data == 3):
        file = input('Enter The File Name')
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
    else:
        print('DataFrame Creation Failed Please Enter the values between 1 and 3 and try again')
    return df1


# In[4]:


def plotter(plot): #this functions checks the kind of plot that the user is working with for plotting the whole data
    if(plot == 1):
        finalplot = df1.iplot(kind='scatter')
    elif(plot == 2):
        finalplot = df1.iplot(kind='scatter',mode='markers' ,symbol='x',colorscale='paired')
    elif(plot == 3):
        finalplot = df1.iplot(kind='bar')
    elif(plot == 4):
        finalplot = df1.iplot(kind='hist')
    elif(plot == 5):
        finalplot = df1.iplot(kind='box')
    elif(plot == 6):
        finalplot = df1.iplot(kind='surface')
    else:
        finalplot = print('Select only between 1 to 7')
    return finalplot


# In[5]:


def plotter2(plot):# this is a function for defining the data to plotted
    col = input('Enter the number of columns you want to plot by selecting only 1 , 2 or 3')
    col = int(col)
    if(col==1): #this is used to plot one column argumne only
        colm = input('Enter the column you want to plot by selecting any column from dataframe head')
        if(plot==1):
            finalplot = df1[colm].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[colm].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[colm].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[colm].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[colm].iplot(kind='box')
        elif(plot==6 or plot==7):
            finalplot = print('Bubble plot and surface plot require more than one column arguments')
        else:
            finalplot = print('Select only between 1 to 7')
    elif(col==2):#this is used to plot two columns in in the selected data
        print('Enter the columns you want to plot by selecting from dataframe head')
        x = input('First column')
        y = input('Second column')
        if(plot==1):
            finalplot = df1[[x,y]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y]].iplot(kind='surface')
        elif(plot==7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,size=size)
        else:
            finalplot = print('Select only between 1 to 7')
    elif(col==3): #this is used to plot three columns in the selected data
        print('Enter the columns you want to plot')
        x=input('First column')
        y=input('Second column')
        z=input('Third column')
        if(plot==1):
            finalplot = df1[[x,y,z]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y,z]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y,z]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y,z]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y,z]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y,z]].iplot(kind='surface')
        elif(plot==7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,z=z,size=size )
        else:
            finalplot = print('Select only between 1 to 7')
    else:
        finalplot = print('Please enter only 1 , 2 or 3')
    return finalplot


# In[ ]:





# In[6]:


def main(cat): # this fuction is used to define the type of plot that the user wants
    if(cat == 1):
        print('Select the type of plot you need to plot by writing 1 to 6')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        plot = int(input())
        output = plotter(plot)
    elif(cat == 2):
        print('Select the type of plot you need to plot by writing 1 to 7')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('7.Bubble plot')
        plot = int(input())
        output = plotter2(plot)
    else:
        print('Please enter 1 or 2 and try again')     


# In[7]:


print('Select the type of data you need to plot(By selecting 1 or 2 or 3)') #this is defining the interface that the user is interacting with
print('1. Random data woth 100 rows and 5 columns') #this is defining the interface that the user is interacting with
print('2. Customized dataframe with 5 columns and 4 rows') #this is defining the interface that the user is interacting with
print('3. Upload the csv/json /txt file') #this is defining the interface that the user is interacting with
data = int(input())#this is defining the interface that the user is interacting with
df1 = createdata(data)


# In[8]:


print('Your DataFrame is given below check columns to plot using cufflinks')
df1.head()


# In[9]:


print('what kind of plot do you need, the complete data plot or columns plot')
cat = input('Press 1 for a full data plot or 2 for a specified columns plot') #Cat in denoting category
cat = int(cat)


# In[10]:


main(cat)


# In[ ]:





# In[ ]:




