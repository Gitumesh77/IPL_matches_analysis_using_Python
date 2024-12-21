# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:42:36 2024

@author: User
"""

#import the required libraries
import numpy as np 
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# to read the csv file 
data = pd.read_csv(r"C:\Users\User\Downloads\matches (1).csv")

data.head(10)

data.shape

data.info

# name of all the columns
data.columns

''' Index(['id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner',
       'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs',
       'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire2',
       'umpire3'],
      dtype='object') 
'''

# data preprocessing. finding NaN values
data.isna().any()

# statistical description of dataset
data.describe()

# Q1) How many matches were played (in total)according to the dataset 
data['id'].count()

# Q2) How many IPL seasons are we using for analyse
data['season'].unique()

# Q3) Which IPL team won by scoring maximum runs
data['win_by_runs'].max()

data.iloc[data['win_by_runs'].idxmax()]

# Q4) Which IPL team won by maximum wickets
data.iloc[data['win_by_wickets'].idxmax()]

# Q5) which IPL team won by minimum wickets
data.iloc[data['win_by_wickets'].idxmin()]

# Q6) which season consisted at highest number of matches played
fig_dims = (20, 4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='season', ax=ax, data=data)
plt.show()

# 7) which is the most successful team 
data1 = data.winner.value_counts()
sns.barplot(y=data1.index, x= data1)

# 8 ) probability of winning matches who won the toss
probability_of_win= data['toss_winner'] == data['winner']
probability_of_win.groupby(probability_of_win).size()

sns.countplot(probability_of_win) # we got the wrong plot for this qn need to check

pd.set_option('display.max_rows', 99999)
pd.set_option('display.max_colwidth', 400)

pd.describe_option('max_colwidth')

# 9) highest matches won by team per season
data.groupby('season')['winner'].value_counts()

#9(1) toss decision 
data['toss_decision'].value_counts()

#10) which player has maximum number of man of the match 
data['player_of_match'].value_counts()

#11) which all the cities matches were played 
data['city'].value_counts()
