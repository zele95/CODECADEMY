# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from functions import plot_all_features, linReg

# load and investigate the data
df = pd.read_csv('tennis_stats.csv')
print(df.head())

# %%
# perform exploratory analysis
plot_all_features(df,'Wins')

plot_all_features(df,'Losses')

plot_all_features(df,'Winnings')

plot_all_features(df,'Ranking')


# %%
## perform single feature linear regressions
linReg(df,'Aces', 'Wins')
linReg(df,'BreakPointsOpportunities', 'Winnings')
linReg(df,'BreakPointsFaced', 'Losses')
linReg(df,'DoubleFaults', 'Wins')
linReg(df,'ReturnGamesPlayed', 'Winnings')
linReg(df,'ServiceGamesPlayed', 'Wins')

# %%
## perform two feature linear regressions 
linReg(df,['BreakPointsOpportunities', 'Aces'], 'Wins')
linReg(df,['DoubleFaults', 'Aces'], 'Wins')
linReg(df,['BreakPointsOpportunities', 'ServiceGamesPlayed'], 'Wins')

linReg(df,['BreakPointsOpportunities', 'Aces'], 'Winnings')
linReg(df,['DoubleFaults', 'Aces'], 'Winnings')
linReg(df,['BreakPointsOpportunities', 'ServiceGamesPlayed'], 'Winnings')

# %%
## perform multiple feature linear regressions
linReg(df,['BreakPointsOpportunities', 'Aces',\
    'BreakPointsFaced','DoubleFaults','ReturnGamesPlayed',\
        'ServiceGamesPlayed'], 'Wins')


linReg(df,['BreakPointsOpportunities', 'Aces',\
    'BreakPointsFaced','DoubleFaults','ReturnGamesPlayed',\
        'ServiceGamesPlayed'], 'Winnings')


