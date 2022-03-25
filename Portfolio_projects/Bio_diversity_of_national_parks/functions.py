import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency



def species_pie(species_file):
    print(species_file.groupby("conservation_status").size())
    partitions = species_file.conservation_status.value_counts().values
    labels = species_file.conservation_status.value_counts().index.to_list()
    plt.pie(partitions, labels = labels, autopct = '%d%%')
    plt.show()


def num_categories(species_file):
    print(species_file.groupby("category").size())
    sns.countplot(data = species_file, x = 'category')
    plt.xticks(rotation = 30)
    plt.show()


def parks_pie(observations_file):
    partitions = observations_file.park_name.value_counts().values
    labels = observations_file.park_name.value_counts().index.to_list()
    plt.pie(partitions, labels = labels, autopct = '%d%%')
    plt.show()

def tidy_up_data(species_file):
    species_file.fillna('Not Endangered', inplace=True)
    species_file['is_protected'] = species_file.conservation_status != 'Not Endangered'

def conservation_status_distribution(species_file):
    print(species_file.groupby("is_protected").size())
    sns.countplot(data = species_file, x = 'category', hue = 'is_protected')
    plt.xticks(rotation = 30)
    plt.show()

    
    print(species_file.groupby("conservation_status").size())
    sns.countplot(data = species_file[species_file.conservation_status\
         != 'Not Endangered'], x = 'category', hue = 'conservation_status')
    plt.xticks(rotation = 30)
    plt.show()


def most_endangered(species):
    sns.countplot(data = species[species.is_protected == True], x = 'category')
    plt.xticks(rotation = 30)
    plt.title('Protected species')
    plt.show()

    sns.countplot(data = species[species.conservation_status == 'Endangered'], x = 'category')
    plt.xticks(rotation = 30)
    plt.title('Endangered species')
    plt.show()

    sns.countplot(data = species[species.conservation_status == 'In Recovery'], x = 'category')
    plt.xticks(rotation = 30)
    plt.title('Species in recovery')
    plt.show()



def get_protected_category_counts(species_file):
    category_counts = species_file.groupby(['category', 'is_protected'])\
                            .scientific_name.nunique()\
                            .reset_index()\
                            .pivot(columns='is_protected',
                                        index='category',
                                        values='scientific_name')\
                            .reset_index()
    category_counts.columns = ['category', 'not_protected', 'protected']
    category_counts['percent_protected'] = category_counts.protected / \
                                        (category_counts.protected + category_counts.not_protected) * 100
    return category_counts




