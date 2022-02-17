# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# load rankings data:
coasters_wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
# print(coasters_wood)
coasters_steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
# print(coasters_steel.head())


# write function to plot rankings over time for 1 roller coaster:
def plot_rankings(coaster_name,df,park_name):
    # select data
    rankings = df[['Rank','Year of Rank']][(df.Name == coaster_name) & (df.Park == park_name)]
    
    # create plot
    plt.figure()
    ax = plt.subplot()
    plt.plot(rankings['Year of Rank'], rankings.Rank)
    ax.invert_yaxis()
    ax.set_xticks(rankings['Year of Rank'].values)
    ax.set_yticks(rankings['Rank'].values)
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title(coaster_name + ' Rankings')
    plt.show(block = False)

# test function
plot_rankings('El Toro',coasters_wood,'Six Flags Great Adventure')
plot_rankings('El Toro',coasters_wood,'Freitzeitpark Plohn')


# %%
# write function to plot rankings over time for 2 roller coasters here:
def plot_2rankings(coaster1,coaster2,df1,df2,park_name1,park_name2):
    # select data
    rankings1 = df1[['Rank','Year of Rank']][(df1.Name == coaster1) & (df1.Park == park_name1)]
    rankings2 = df2[['Rank','Year of Rank']][(df2.Name == coaster2) & (df2.Park == park_name2)]
    
    # create plot
    plt.figure()
    ax = plt.subplot()
    plt.plot(rankings1['Year of Rank'], rankings1.Rank,label = coaster1)
    plt.plot(rankings2['Year of Rank'], rankings2.Rank, label = coaster2)
    plt.title(coaster1+ ' vs ' + coaster2+ ' Rankings')
    ax.invert_yaxis()
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend()
    plt.show(block = False)

# test function
plot_2rankings('El Toro','Boulder Dash',coasters_wood,coasters_wood,'Six Flags Great Adventure','Lake Compounce')


# %%
# write function to plot top n rankings over time here:
def plot_nrankings(n,df):
    # select top n rankings ever
    top_n_rankings = df[df['Rank'] <= n]

    # create plot for each
    plt.figure(figsize=(10,10))
    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        plt.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=coaster)
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title('Top ' + str(len(set(top_n_rankings['Name']))) + ' Rankings')
    plt.legend(loc=4)
    plt.show(block = False)

# test function
plot_nrankings(5,coasters_wood)


# %%
# load roller coaster data here:
coasters_df = pd.read_csv('roller_coasters.csv')
print(coasters_df.head())


# write function to plot histogram of column values:
def plot_histogram(df, column):
    # remove outliers for height
    if column == 'height':
        # plt.hist(df[column])
        plt.figure()
        plt.hist(df[column][df[column] <= 140].dropna())  
    else:
        plt.figure()
        plt.hist(df[column].dropna())

    # rename
    if column == 'num_inversions':
        column = 'Number of Inversions'
    
    plt.xlabel(column.capitalize())
    plt.ylabel('Count')
    plt.title('Histogram of Roller Coaster {}'.format(column.capitalize()))
    plt.show(block = False)

# test function
plot_histogram(coasters_df, 'speed')
plot_histogram(coasters_df, 'length')
plot_histogram(coasters_df, 'num_inversions')
plot_histogram(coasters_df, 'height')


# %%
# write function to plot inversions by coaster at a park:
def plot_bar_inversions(df,park_name):
    # select park data
    park_df = df[df.park == park_name]
    # sort data by num_inversions
    coasters = park_df.sort_values('num_inversions',ascending = False)['name']
    inversions = park_df.sort_values('num_inversions', ascending = False)['num_inversions'] 
    
    # create bar plot
    plt.figure()
    plt.bar(range(len(inversions)),inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coasters)))
    ax.set_xticklabels(coasters,rotation=90)
    plt.title('Number of Inversions Per Coaster at {}'.format(park_name))
    plt.xlabel('Roller Coaster')
    plt.ylabel('Inversions')
    plt.show(block = False)


# test function
plot_bar_inversions(coasters_df,'Disneyland Park')
plot_bar_inversions(coasters_df,'Walibi Rhône Alpes')
plot_bar_inversions(coasters_df, 'Six Flags Great Adventure')

# %%
# write function to plot pie chart of operating status:
def plot_pie_operating(df):
    # select operational and closed
    operating = sum(df.status == 'status.operating')
    noperating = sum(df.status == 'status.closed.definitely')

    # create pie chart
    plt.figure()
    plt.pie([operating, noperating],autopct = '%0.1f%%',labels = ['Operational','Closed'])
    plt.axis('equal')
    plt.title('Operational coasters')
    plt.show(block = False)
    
# test function
plot_pie_operating(coasters_df)

# %%
# write function to create scatter plot of any two numeric columns:
def plot_scatter(df, column1, column2):

    # remove outliers from height
    if column1 == 'heigth' or column2 == 'height':
        df = df[df['height'] <= 140]
    
    # create scatter plot
    plt.figure()
    plt.scatter(df[column1],df[column2])
    plt.xlabel(column1.capitalize())
    plt.ylabel(column2.capitalize())
    plt.title('Scatter Plot of {} vs. {}'.format(column1.capitalize(),column2.capitalize()))
    plt.show(block = False)

# test function
plot_scatter(coasters_df, 'length', 'height')
plot_scatter(coasters_df, 'length', 'num_inversions')
plot_scatter(coasters_df, 'speed', 'height')


# %%
# What roller coaster seating type is most popular?
# And do different seating types result in 
# higher/faster/longer roller coasters?


# extract seating type data
seatings = coasters_df.seating_type.value_counts()

# Rename to 'Other' seating_types that have a count less than 50
mask = coasters_df.seating_type.isin(seatings[seatings<50].index)
coasters_df_pie = coasters_df
coasters_df_pie.seating_type[mask] = 'Other'
seatings = coasters_df_pie.seating_type.value_counts()

# create a pie chart
labels = seatings.index
values = seatings.values
plt.pie(values,labels = labels, autopct = '%d%%')
plt.title('Rollercoasters seatting types' )
plt.show(block = False)

# create a box plot for seating types and a choosen feature
def plot_seatingtype(df,column):
    plt.figure(figsize = (12,7))
    # sns.set_style()
    sns.boxplot(data = df.dropna(), x = 'seating_type', y = column)
    plt.xlabel('Seating type')
    plt.ylabel(column.capitalize())
    plt.show(block = False)

plot_seatingtype(coasters_df,'length')
plot_seatingtype(coasters_df,'speed')


# %%
# Do roller coaster manufacturers have any specialties
# (do they focus on speed, height, seating type, or inversions)?

# create a bar chart for a specific feature for top manufacturers
def plot_manufact_feature(df,column):
    
    # select which manufact. are best in this feature
    manufacturers = df.dropna().groupby('manufacturer')[column].mean().reset_index().sort_values(column, ascending = False)
    print(manufacturers)
    top_manufacturers = manufacturers.manufacturer.to_list()[:10]
    print(type(top_manufacturers))

    # select only those manufact. data
    mask = df.manufacturer.isin(top_manufacturers)
    new_df = df[mask]
    print(mask)

    # create a bar plot
    plt.figure(figsize = (12,7))
    sns.set_style('whitegrid')
    sns.barplot(data = new_df,x = 'manufacturer', y = column)
    plt.xlabel('Manufacturer')
    plt.ylabel(column.capitalize())
    plt.title(column.capitalize() + ' for top 10 manufacturers')
    plt.xticks(rotation = 90)

    plt.show(block = False)

plot_manufact_feature(coasters_df,'speed')
# plot_manufact_feature(coasters_df,'height')
# plot_manufact_feature(coasters_df,'length')
plot_manufact_feature(coasters_df,'num_inversions')

# compare seating_types for a specific manufacturer
def plot_manufacturer_seating_type(df, manufacturer):
    new_df = df[df.manufacturer == manufacturer]
    sns.countplot(data = new_df, x = 'seating_type')
    plt.title('Seating types for '+ manufacturer)
    plt.show(block = False)

plot_manufacturer_seating_type(coasters_df, 'Giovanola')
# %%
# Do amusement parks have any specialties?

# create a bar chart for a specific feature for the amusement parks
def plot_park_feature(df,column):
    
    # select which parks are best in this feature
    parks = df.dropna().groupby('park')[column].mean().reset_index().sort_values(column, ascending = False)
    print(parks)
    top_parks = parks.park.to_list()[:10]
    print(type(top_parks))

    # select only those park data
    mask = df.park.isin(top_parks)
    new_df = df[mask]
    print(mask)

    # create a bar plot
    plt.figure(figsize = (12,7))
    sns.set_style('whitegrid')
    sns.barplot(data = new_df,x = 'park', y = column)
    plt.xlabel('Park')
    plt.ylabel(column.capitalize())
    plt.title(column.capitalize() + ' for top 10 parks')
    plt.xticks(rotation = 90)
    plt.show()

plot_park_feature(coasters_df,'speed')
plot_park_feature(coasters_df,'length')
