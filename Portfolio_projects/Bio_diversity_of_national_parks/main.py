# %% INTRODUCTION, GETTING TO KNOW THE DATA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from functions import species_pie, num_categories, parks_pie,\
     get_protected_category_counts, tidy_up_data, conservation_status_distribution,\
         most_endangered

# load data
species = pd.read_csv('species_info.csv')
observations = pd.read_csv('observations.csv')

# basic data information and summary statistics
print(species.info())
print(species.describe())

print(observations.info())
print(observations.iloc[:,:2].describe())

# %% BASIC INFORMATION ABOUT CATEGORIES, STATUS AND PARKS

# what is the ratio of species under 
# conservation status
species_pie(species)

# how many of each category there is
num_categories(species)

# what is the ratio of parks
parks_pie(observations)

# Therefore, for each species (total 5824)
# the observation number at each park is noted
# in observations.csv (total 23296 species (4*5824))

# %% ANALISYS OF THE CONSERVATION STATUS FOR ANIMALS

# what is the distribution of the conservation status? 

# fill all the nan values and create is_protected column
tidy_up_data(species)

# show the distribution of protectes species and conservation status
conservation_status_distribution(species)

# %%
# Are certain types of species more likely to be endangered?
most_endangered(species)

# We can see that mammals and birds are the most endangered
# with some birds already in recovery, therefore the most endangered 
# are mammals

# %%
# Are the differences between species and their conservation status significant?

# create a table of protected percentage for each category
print(get_protected_category_counts(species))

# create a crosstab
xtab = pd.crosstab(index=species['category'], columns = species['is_protected'])
print(xtab)


_, p_val, _, _ = chi2_contingency(xtab.loc[['Bird','Mammal']])
print(f'Bird and Mammal: {p_val}')

_, p_val, _, _ = chi2_contingency(xtab.loc[['Mammal','Vascular Plant']])
print(f'Mammal and Vascular Plant: {p_val}')

_, p_val, _, _ = chi2_contingency(xtab.loc[['Nonvascular Plant','Reptile']])
print(f'Nonvascular Plant and Reptile: {p_val}')

_, p_val, _, _ = chi2_contingency(xtab.loc[['Amphibian','Reptile']])
print(f'Amphibian and Reptile: {p_val}')

_, p_val, _, _ = chi2_contingency(xtab.loc[['Amphibian','Fish']])
print(f'Amphibian and Fish: {p_val}')

_, p_val, _, _ = chi2_contingency(xtab.loc[['Nonvascular Plant','Fish']])
print(f'Nonvascular Plant and Fish: {p_val}')



# %%
# Which species were spotted the most at each park?

# What are the most observed species?
most_observed = observations.sort_values(by = 'observations',ascending = False)
print(most_observed)


