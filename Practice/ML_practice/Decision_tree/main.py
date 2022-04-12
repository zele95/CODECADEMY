# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# get data
flags = pd.read_csv('flags.csv', header = 0)
print(flags.head())
print(flags.columns)

# select features and labels
labels = flags.Landmass
# data = flags[["Red","Green","Blue","Gold","White","Black","Orange"]]
data = flags[["Red", "Green", "Blue", "Gold",
 "White", "Black", "Orange",
 "Circles",
"Crosses","Saltires","Quarters","Sunstars",
"Crescent","Triangle"]]

# check for the best depth value
score = []
for i in range(1,21):
  train_data, test_data, train_labels, test_labels = train_test_split(data,labels, random_state = 1)

  tree = DecisionTreeClassifier(random_state = 1, max_depth = i)

  tree.fit(train_data,train_labels)
  score.append(tree.score(test_data,test_labels))
  # print(score)
  
plt.plot(range(1,21),score)
plt.show()