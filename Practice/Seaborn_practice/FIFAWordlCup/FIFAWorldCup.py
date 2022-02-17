from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv',nrows=852)
# print(df.head())

df['Total Goals']= df['Home Team Goals']+df['Away Team Goals']
# df.insert(7, 'Total Goals',df['Home Team Goals']+df['Away Team Goals'])
print(df.head())
# df.Year.astype(int)
print(df.dtypes)

# change different palettes and styles
sns.set_style('whitegrid')
sns.set_context('notebook')
f, ax = plt.subplots(figsize = (12,7))
sns.barplot(data = df, y = 'Total Goals', x = 'Year', palette = 'pastel')
ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")
plt.show(block = False)

f, ax = plt.subplots(figsize = (12,7))
sns.barplot(data = df, y = 'Total Goals', x = 'Year', palette = 'tab10')
ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")
plt.show(block = False)

sns.set_style('white')
sns.set_context('poster',font_scale=0.5)
f, ax = plt.subplots(figsize = (12,7))
sns.barplot(data = df, y = 'Total Goals', x = 'Year')
ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")
plt.show(block = False)


# change different palettes and styles
sns.set_context('notebook')
f, ax2 = plt.subplots(figsize = (12,7))
sns.boxplot(data = df, x = 'Year', y = 'Home Team Goals', palette = 'Spectral')
ax2.set_title('Mjau')
plt.show(block = False)

sns.set_style('whitegrid')
sns.set_context('poster')
f, ax2 = plt.subplots(figsize = (12,7))
sns.boxplot(data = df, x = 'Year', y = 'Home Team Goals', palette = 'deep')
ax2.set_title('Mjau')
plt.show()
