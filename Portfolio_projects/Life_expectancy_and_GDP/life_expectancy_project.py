# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Get to know the data, and some basic summary stats
df = pd.read_csv('all_data.csv')
df = df.rename(columns ={'Life expectancy at birth (years)':'LE'})
print(df.head())
print(df.info())
print(df.describe())

# The average of the LE and GDP in each country
sns.set_style('darkgrid')
plt.figure(figsize = (20,12))
plt.subplot(2,1,1)
sns.barplot(data = df, x = 'Country', y = 'GDP')
plt.title('Average GDP')

plt.subplot(2,1,2)
sns.barplot(data = df, x = 'Country', y = 'LE')
plt.title('Average Life Expectancy')
plt.show()

# How LE and GDP changed over time in each country
sns.set_style('whitegrid')
plt.figure(figsize = (10,8))
plt.subplot(2,1,1)
plt.title('GDP over the years')
sns.lineplot(data = df, x = 'Year', y = 'GDP', hue = 'Country')

plt.subplot(2,1,2)
sns.lineplot(data = df, x = 'Year', y = 'LE',hue = 'Country')
plt.title('Life Expectancy over the years')
plt.show()


# %%
# Is there a correlation between life expectancy
# and GDP in these contries?

# separate 'Outliers', Chile and Zimbabwe
new_df = df[(df.Country != 'Zimbabwe') & (df.Country != 'Chile')]
sns.lmplot(data = new_df, x = 'GDP', y = 'LE',hue = 'Country')
plt.title('Life Expectancy vs GDP of mode developed countries')
plt.show()

# Show correlation for Chile and Zimbabwe
Chile_df = df[df.Country == 'Chile']
sns.lmplot(data = Chile_df, x = 'GDP', y = 'LE')
plt.title('Life Expectancy vs GDP of Chile')
plt.show()

Zimbabwe_df = df[df.Country == 'Zimbabwe']
sns.lmplot(data = Zimbabwe_df, x = 'GDP', y = 'LE')
plt.title('Life Expectancy vs GDP of Zimbabwe')
plt.show()

# It is clear that the correlation is strong

# Correlation coefficients calculation
correlations = []
p_values = []
countries = df.Country.unique()
# for each country
for country in countries:
    correlation, _ = pearsonr(df.GDP[df.Country == country], df.LE[df.Country == country])
    correlations.append(correlation)
    
# corr_dict = dict(zip(df.Country.unique(),correlations))

# create a data frame with correlations
corr_df = pd.DataFrame({'Country':countries,'Correlation':correlations})
print(corr_df)

# There is a strong correlation between GDP and life expectancy
# for all countries 
# %%
# Additional plots
sns.kdeplot(data = new_df, shade = True, x = 'LE', hue = 'Country', alpha = 0.5)
plt.show()

sns.displot(data = Zimbabwe_df , x = 'LE', kde = True)
plt.show()

sns.displot(data = df, x = 'GDP', hue = 'Country')
plt.show()

sns.kdeplot(data = new_df, shade = True, x = 'GDP', hue = 'Country', alpha = 0.5)
plt.show()



