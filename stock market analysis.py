#!/usr/bin/env python
# coding: utf-8

# # STOCK MARKET ANALYSIS

# ## A stock market, equity market or share market is the aggregation of buyers and sellers (a loose network of economic transactions, not a physical facility or discrete entity) of stocks (also called shares), which represent ownership claims on businesses; these may include securities listed on a public stock exchange, as well as stock that is only traded privately.

# ## DESCRIPTION:-
# 
# ### The project actually analyses the stock market changes and also predicts the upcoming fluctuations in the level of stock market. The project is going to cover some very important factor in the stock market sector like ''daily return of stock on average'', ''moving average of various stocks'', ''correlation between different stocks closing prices'', also some other things. The project consists of different graphs for describing some important factors...

# In[1]:


#Some important libraries of python that are used are:-
import numpy as np
import sys
import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style='Whitegrid'
import pandas_datareader as dr
from pandas_datareader import data
from datetime import datetime
import datetime
import pylab as pl
plt.grid()
get_ipython().run_line_magic('matplotlib', 'inline')


# ### The companies used are:-
# #### Maruti (MARUTI.NS) , Hindustan unilever Ltd (HINDUNILVR.NS) , Reliance (RELIANCE.NS) , Bajaj Finance (BAJFINANCE.NS)

# In[2]:


print(f'Here is the list of some biggest companies in Stock Market area: {"MARUTI","HINDUNILVR","RELIANCE","BAJFINANCE"}')


# In[3]:


#tech_list is the stock companies list created to store the names of the stock companies
tech_list=["MARUTI","HINDUNILVR","RELIANCE","BAJFINANCE"]


# In[4]:


tech_list


# Now we are going to put the start and end date to extract the stock data in that particular time only...

# In[5]:


# the date from where we want to start our analysis
start = input('Enter a start date in YYYY-MM-DD format: ')
year, month, day = map(int, start.split('-'))
date1 = datetime.date(year, month, day)
print(f'the start date is : {start}')

#it is the date till where we want to do our analysis
end = datetime.datetime.now().date()
print(f" the end date is : {end}")


# ## YAHOO FINANCE
# So now we are going to use YAHOO FINANCE to extract the stock data and we are going to represent that data in the form of DATAFRAME to make it more understandable.

# In[6]:


#"df" is the short form for dataframe. 
#In this actually we use data science with python library GET_DATA_YAHOO to fetch the data between the start and the end date.. 


# In[7]:


#dr.data.get_data_yahoo is the python library used to extract data from yahoo using DatarRader"dr"
df_MARUTI= dr.data.get_data_yahoo("MARUTI.NS",start,end)


# In[8]:


df_HINDUNILVR= dr.data.get_data_yahoo("HINDUNILVR.NS",start,end)


# In[9]:


df_RELIANCE= dr.data.get_data_yahoo("RELIANCE.NS",start,end)


# In[10]:


df_BAJFINANCE= dr.data.get_data_yahoo("BAJFINANCE.NS",start,end)


# In[11]:


df_MARUTI


# In[12]:


df_HINDUNILVR.head()


# In[13]:


df_BAJFINANCE.head()


# An adjusted closing price is a "stock's closing price" on any given day of trading that has been amended to include any distributions and corporate actions that occurred at any time before the next day's open.
# 
# So we are going to use "Adj close" from the dataframes to do some analytics on the data provided to us.

# ### Adjusted Closing Price:-

# In[14]:


# So we are going to do some historical analysis of MARUTI company..
df_MARUTI['Adj Close'].plot(legend=True,color='Blue',figsize=(15,8),linewidth=4)
plt.title("Adjusted closing price graph",weight= 'bold')
plt.ylabel("Adj clsoe")
plt.grid()


# In[15]:


# So we are going to do some historical analysis of RELIANCE company..
df_RELIANCE['Adj Close'].plot(legend=True,color='yellow',figsize=(15,8),linewidth=4)
plt.title("Adjusted closing price graph",weight= 'bold')
plt.ylabel("Adj clsoe")
plt.grid()


# In[16]:


# So we are going to do some historical analysis of BAJFINANCE company..
df_BAJFINANCE['Adj Close'].plot(legend=True,color='red',figsize=(15,8),linewidth=4)
plt.title("Adjusted closing price graph",weight= 'bold')
plt.ylabel("Adj close")
plt.grid()


# So, Below I have created a DataFrame consisting of the adjusted closing price of these stocks, first by making a list of these objects and using the join method...
# 
# 

# In[17]:


#stocks is the DataFrame for the adjusted closing price of the companies.
stocks = pd.DataFrame({"MARUTI.NS":df_MARUTI["Adj Close"],
                      "RELIANCE.NS": df_RELIANCE["Adj Close"],
                      "HINDUNILVR.NS": df_HINDUNILVR["Adj Close"],
                      "BAJFINANCE.NS": df_BAJFINANCE["Adj Close"]})
 
stocks.head()


# In[18]:


stocks.plot(secondary_y=["MARUTI.NS","RELIANCE.NS"],grid=True,legend=True,figsize=(20,12),linewidth=4)
plt.title("Adjusted colsing graph of all companies",weight= 'bold')


# ### Stock Change:-
# now we are going to find out the STOCK CHANGE for all companies..

# In[19]:


stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1)))

stock_change.plot(grid = True).axhline(y = 0, color = "black")
stock_change.plot(grid=True,figsize=(20,8))
plt.title("Stock change graph of all companies",weight='bold')


# ## Daily Returns:-
# ### So, below is the list of the DAILY RETURNS of the stock companies....

# In[20]:


# tech_daily_rets is the daily returns of the stocks company..
# pct_change is the percentage change of the stocks DataFrame and is stored in the tech_daily_rets DataFrame 
tech_daily_rets = stocks.pct_change()


# In[21]:


tech_daily_rets.dropna().head()


# ### So now we're going to print a jointplot that is going to compare the daily returns of MARUTI.NS with RELIANCE.NS

# In[22]:


g=sns.jointplot('MARUTI.NS','RELIANCE.NS',tech_daily_rets,color='red',kind='reg')
g.fig.set_figheight(8)
g.fig.set_figwidth(8)


# So now i'm going to print a jointplot that is going to compare the daily returns of HINDUNILVR.NS with BAJFINANCE.NS

# In[23]:


g=sns.jointplot('HINDUNILVR.NS','BAJFINANCE.NS',tech_daily_rets,color='darkblue',kind='reg')
g.fig.set_figheight(8)
g.fig.set_figwidth(8)


# ### Another representation with the help of PAIR PLOT
# 

# In[24]:


sns.pairplot(tech_daily_rets.dropna())


# ### Now if you want to find the correlation between the daily return values of the stocks then HEATMAP comes into play..

# In[25]:


#This is going to display a "heatmap" showing the correlation between the "tech_daily_return" values...
plt.figure(figsize = (12,7))
sns.heatmap(tech_daily_rets.dropna().head(),annot=True)


# ## RISK ANALYSIS:- 
# 
# #### There are many ways we can quantify risk, one of the most basic ways using the information we have gathered on daily percentage return, is by comparing the expected return with standard deviation.

# In[26]:


rets = tech_daily_rets.dropna()


# In[27]:


area = np.pi*20

plt.scatter (rets.mean(),rets.std(),s=area)
#set the plot axis title
plt.xlabel('Expected returns')
plt.ylabel('Risk')
plt.grid()
plt.title("Graph of Risk Analysis",weight='bold',fontsize=12)

for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
      plt.annotate("",
            xy=(x, y), xycoords='data',
            xytext=(50, 50), textcoords='offset points',
            arrowprops=dict(arrowstyle='fancy', connectionstyle='arc3,rad=-0.3'))
            


# # Moving Average :-

# ### The moving average (MA) is a simple technical analysis tool that smooths out price data by creating a constantly updated average price. 

# In[28]:


df_MARUTI["15d"]=np.round(df_MARUTI["Adj Close"].rolling(window=15,center=False).mean(),2).plot(figsize=[10,8],legend=True,color='indianred',linewidth=4.3)
plt.title("MARUTI MOVING AVERAGE",weight='bold',fontsize=15)
plt.grid()


# In[29]:


df_HINDUNILVR["15d"]=np.round(df_HINDUNILVR["Adj Close"].rolling(window=15,center = False).mean(),2).plot(figsize=[10,8],legend=True,color='black',linewidth=4.3)
plt.title("HINDUNILVR MOVING AVERAGE",weight='bold',fontsize=15)
plt.grid()


# In[30]:


df_RELIANCE["15d"]=np.round(df_RELIANCE["Adj Close"].rolling(window=15,center = False).mean(),2).plot(figsize=[10,8],legend=True,color='blue',linewidth=4.3)
plt.title("RELIANCE MOVING AVERAGE",weight='bold',fontsize=15)
plt.grid()


# In[31]:


df_BAJFINANCE["15d"]=np.round(df_BAJFINANCE["Adj Close"].rolling(window=15,center = False).mean(),2).plot(figsize=[10,8],legend=True,color='green',linewidth=4.3)
plt.title("BAJFINANCE MOVING AVERAGE",weight='bold',fontsize=15)
plt.grid()


# ## Value Of Risk:-

# ### Let's go ahead and define a risk parameter for our stocks. We can treat value at risk as the amount of money we can expect to lose for a particular interval of time. There are several methods for finding out the value of risk.
# 
# 
# 
# 
# 
# 
# ### Value of risk by " MONTE CARLO METHOD"
# 

# #### using the monte carlo to run many trials with random market conditions, then will calculate the portfolio losses for each trials. After this will use the aggregation of all these simulations to establish how risky the stock is.
# 
# 
# 
# 

# ### MARUTI (Value of risk) by MONTE CARLO..

# In[32]:


days = 365

dt = 1/days

mu = tech_daily_rets.mean()["MARUTI.NS"]

sigma = tech_daily_rets.std()["MARUTI.NS"]

start_price = df_MARUTI["Open"][0]


# In[33]:


def stock_monte_carlo(start_price,days,mu,sigma):
    
    price = np.zeros(days)
    price[0]= start_price
    
    shock = np.zeros(days)
    drift = np.zeros(days)
    
    for x in range(1,days):
        # formula for finding the shock term 
        shock[x] = np.random.normal(loc=mu*dt,scale=sigma*np.sqrt(dt))
        # formula for finding the drift term
        drift[x] = mu*dt
        #formula of price..
        price[x] = price[x-1] + (price[x-1]*(drift[x]+shock[x]))
        
    return price    
        
        


# In[34]:


start_price=df_MARUTI["Open"][0]
start_price


# In[35]:



runs = 10000

simulation = np.zeros(runs)

for run in range(runs):
    simulation[run] = stock_monte_carlo(start_price,days,mu,sigma)[days-1]
    


# In[36]:



q = np.percentile(simulation,1)

plt.hist(simulation,bins=200)

#starting price
plt.figtext(0.6,0.8, s= "Start Price: $%.2f" %start_price)

#Mean ending price
plt.figtext(0.6,0.7, s= "Mean final Price: $%.2f" %simulation.mean())

#Variance of the price (within 99% confidence interval)
plt.figtext(0.6,0.6, s= "VaR(0.99): $%.2f" %(start_price - q,))

#display 1% qunatile
plt.figtext(0.15,0.8, s= "q(0.99): $%.2f" % q)

# plot a line at the 1% quantile result
plt.axvline(x=q,linewidth=4,color = 'r')

plt.grid()

#Title
plt.title(u"final price distribution for particular stock after %s days" % days , weight= 'bold')


# ### RELIANCE (Value of risk) by MONTE CARLO..

# In[37]:


days = 365

dt = 1/days

mu = tech_daily_rets.mean()["RELIANCE.NS"]

sigma = tech_daily_rets.std()["RELIANCE.NS"]

start_price_1 = df_RELIANCE["Open"][0]


# In[38]:


def stock_monte_carlo(start_price_1,days,mu,sigma):
    
    price = np.zeros(days)
    price[0]= start_price_1
    
    shock = np.zeros(days)
    drift = np.zeros(days)
    
    for x in range(1,days):
        # formula for finding the shock term 
        shock[x] = np.random.normal(loc=mu*dt,scale=sigma*np.sqrt(dt))
        # formula for finding the drift term
        drift[x] = mu*dt
        #formula of price..
        price[x] = price[x-1] + (price[x-1]*(drift[x]+shock[x]))
        
    return price    
        
        


# In[39]:


start_price_1=df_RELIANCE["Open"][0]
start_price_1


# In[40]:


runs = 10000

simulation = np.zeros(runs)

for run in range(runs):
    simulation[run] = stock_monte_carlo(start_price_1,days,mu,sigma)[days-1]
    


# In[41]:


q = np.percentile(simulation,1)

plt.hist(simulation,bins=200)

#starting price
plt.figtext(0.6,0.8, s= "Start Price: $%.2f" %start_price_1)

#Mean ending price
plt.figtext(0.6,0.7, s= "Mean final Price: $%.2f" %simulation.mean())

#Variance of the price (within 99% confidence interval)
plt.figtext(0.6,0.6, s= "VaR(0.99): $%.2f" %(start_price_1 - q,))

#display 1% qunatile
plt.figtext(0.15,0.8, s= "q(0.99): $%.2f" % q)

# plot a line at the 1% quantile result
plt.axvline(x=q,linewidth=4,color = 'r')


plt.grid()

#Title
plt.title(u"final price distribution for particular stock after %s days" % days , weight= 'bold')


# ### HINDUNILVR (Value of risk) by MONTE CARLO..

# In[42]:


days = 365

dt = 1/days

mu = tech_daily_rets.mean()["HINDUNILVR.NS"]

sigma = tech_daily_rets.std()["HINDUNILVR.NS"]

start_price_2 = df_HINDUNILVR["Open"][0]


# In[43]:


def stock_monte_carlo(start_price_2,days,mu,sigma):
    
    price = np.zeros(days)
    price[0]= start_price_2
    
    shock = np.zeros(days)
    drift = np.zeros(days)
    
    for x in range(1,days):
        # formula for finding the shock term 
        shock[x] = np.random.normal(loc=mu*dt,scale=sigma*np.sqrt(dt))
        # formula for finding the drift term
        drift[x] = mu*dt
        #formula of price..
        price[x] = price[x-1] + (price[x-1]*(drift[x]+shock[x]))
        
    return price    
        


# In[44]:


start_price_2=df_HINDUNILVR["Open"][0]
start_price_2


# In[45]:


runs = 10000
simulation = np.zeros(runs)
for run in range(runs):
    simulation[run] = stock_monte_carlo(start_price_2,days,mu,sigma)[days-1]
    


# In[46]:


q = np.percentile(simulation,1)

plt.hist(simulation,bins=200)

#starting price
plt.figtext(0.6,0.8, s= "Start Price: $%.2f" %start_price_2)

#Mean ending price
plt.figtext(0.6,0.7, s= "Mean final Price: $%.2f" %simulation.mean())

#Variance of the price (within 99% confidence interval)
plt.figtext(0.6,0.6, s= "VaR(0.99): $%.2f" %(start_price_2 - q,))

#display 1% qunatile
plt.figtext(0.15,0.8, s= "q(0.99): $%.2f" % q)

#plot a line at the 1% quantile result
plt.axvline(x=q,linewidth=4,color = 'r')

#figsize
plt.plot(figsize=[25,8])

plt.grid()

#Title
plt.title(u"final price distribution for particular stock after %s days" % days , weight= 'bold')


# ### BAJFINANCE (Value of risk) by MONTE CARLO..

# In[47]:


days = 365

dt = 1/days

mu = tech_daily_rets.mean()["BAJFINANCE.NS"]

sigma = tech_daily_rets.std()["BAJFINANCE.NS"]

start_price_3 = df_BAJFINANCE["Open"][0]


# In[48]:


def stock_monte_carlo(start_price_3,days,mu,sigma):
    
    price = np.zeros(days)
    price[0]= start_price_3
    
    shock = np.zeros(days)
    drift = np.zeros(days)
    
    for x in range(1,days):
        # formula for finding the shock term 
        shock[x] = np.random.normal(loc=mu*dt,scale=sigma*np.sqrt(dt))
        # formula for finding the drift term
        drift[x] = mu*dt
        #formula of price..
        price[x] = price[x-1] + (price[x-1]*(drift[x]+shock[x]))
        
    return price    
        


# In[49]:


start_price_3=df_BAJFINANCE["Open"][0]
start_price_3


# In[50]:


runs = 10000
simulation = np.zeros(runs)
for run in range(runs):
    simulation[run] = stock_monte_carlo(start_price_3,days,mu,sigma)[days-1]
    


# In[51]:


q = np.percentile(simulation,1)

plt.hist(simulation,bins=200)

#starting price
plt.figtext(0.6,0.8, s= "Start Price: $%.2f" %start_price_3)

#Mean ending price
plt.figtext(0.6,0.7, s= "Mean final Price: $%.2f" %simulation.mean())

#Variance of the price (within 99% confidence interval)
plt.figtext(0.6,0.6, s= "VaR(0.99): $%.2f" %(start_price_3 - q,))

#display 1% qunatile
plt.figtext(0.15,0.8, s= "q(0.99): $%.2f" % q)

#plot a line at the 1% quantile result
plt.axvline(x=q,linewidth=4,color = 'r')

#figsize
plt.plot(figsize=[25,8])

plt.grid()

#Title
plt.title(u"final price distribution for particular stock after %s days" % days , weight= 'bold')


# 

# 

# 

# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




