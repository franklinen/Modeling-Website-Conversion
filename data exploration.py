# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:49:26 2021

@author: MAIN
"""


#import dataset
df = pd.read_csv("data.csv", na_values= " ")
#basic dataset exploration
print(df.head(n=5)) 
print(df.describe())  
print(df.shape)  #dataframe shape
print(df.dtypes)  #dtatypes of the individual columns
# Exploratory Data Analysis
#Channel with the highest number of transactions
df.groupby('channelGrouping')['transactions'].nunique().plot(kind='bar')
plt.show()
#Top visitors with highest transaction numbers and number of visits. No strong correlation between sum transactions and number of visits
df.groupby(['fullVisitorID']).agg({'transactions':'sum', 'visitNumber':'count'}).sort_values(by= ['transactions','visitNumber'], ascending=False)[:10].plot(kind='bar')
#Device type with highest average timeOnsite
#there is a need to optimise the website mobile and tablet view so its easier to scroll through the products online annd 
df.groupby(['deviceCategory']).agg({'timeOnSite':'sum'}).sort_values(by= ['timeOnSite'], ascending=False).plot(kind='bar')
plt.show()
#Top countries with highest transaction numbers
df.groupby(['country']).agg({'transactions':'sum'}).sort_values(by= ['transactions'], ascending=False)[:10].plot(kind='barh')

#check correlation with seaborn heatmap
sns.set_style("whitegrid")
plt.figure(figsize=(30,30))
sns.heatmap(df.corr(), cmap='RdBu_r', annot=True, vmax=1, vmin=-1)
plt.show()
