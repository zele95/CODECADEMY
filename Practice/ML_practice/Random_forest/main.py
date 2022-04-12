# %%
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# get data
income_data = pd.read_csv('income.csv', header = 0, delimiter = ', ')
# print(income_data.head())

# map categoricals to int
income_data["sex-int"] = income_data["sex"].apply(lambda row: 0 if row == "Male" else 1)
# print(income_data["native-country"].value_counts())
income_data["native-country-int"] = income_data["native-country"].apply(lambda row: 0 if row == 'United-States' else 1)

# select data and labels
labels = income_data.income
data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week",'sex-int','native-country-int']]

# split data
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)

# create and fit random forest
forest = RandomForestClassifier(random_state = 1)
forest.fit(train_data,train_labels)

# print feature importance and score
print(list(zip(data.columns,forest.feature_importances_)))
print(f'score: {forest.score(test_data,test_labels)}')
