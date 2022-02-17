# %%
import pandas as pd
import sqlite3
from matplotlib import pyplot as plt
import numpy as np

# # CREATE A DATABASE
# df_stream = pd.read_csv('stream.csv')
# # Show DataFrame
# print(df_stream)
# # Instantiate a connection
# connection = sqlite3.connect("stream.db")
# # Instantiate a cursor
# cursor = connection.cursor()
# # Create a table
# df_stream.to_sql("stream", connection)

# cursor.close()
# connection.close()



## Select the top 10 games and number of viewers and plot on a bar chart

# Instantiate a connection
connection = sqlite3.connect("stream.db")
cursor = connection.cursor()
games_df = pd.read_sql_query('''SELECT game, COUNT(*) AS viewers
                            FROM stream
                            GROUP BY game
                            ORDER BY COUNT(*) DESC
                            LIMIT 10;''',connection)

print(games_df)


viewers = list(games_df.viewers)
# games = list(games_df.game)
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]


# create a bar chart
plt.figure()
plt.bar(range(len(games)), viewers)
plt.title('Featured Games Viewers')
plt.legend(["Twitch"])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_xticks(range(10))
ax.set_xticklabels(games, rotation=30)
plt.show(block=False)
# %%



## Select and plot LoL viewers in each countries

LoL_df = pd.read_sql_query('''SELECT country, COUNT(*) AS viewers
                                FROM stream
                                WHERE game = 'League of Legends'
                                GROUP BY 1
                                ORDER BY 2 DESC
                                LIMIT 12;''',connection)

print(LoL_df)

countries = list(LoL_df.viewers)

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

# pie chart
plt.figure()
plt.pie(countries, colors = colors, explode = explode, shadow = True, startangle=345, autopct='%1.0f%%',pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.axis('equal')
plt.legend(labels, loc="right")
plt.show(block=False)
# %%



## Select viewers by hour for US on 1.1.2015

hours_df = pd.read_sql_query('''SELECT strftime('%H', time) AS Hour,
                                COUNT(*) AS Viewers
                                FROM stream
                                WHERE country = 'US'
                                GROUP BY 1;''',connection)

print(hours_df)

viewers_hour = list(hours_df.Viewers)
hour = list(hours_df.Hour)

# plot with uncertanty
plt.figure() 
plt.title("Time Series")
plt.xlabel("Hour")
plt.ylabel("Viewers")
plt.plot(hour, viewers_hour)
plt.legend(['2015-01-01'])
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_yticks([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000])

y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)
plt.show()

cursor.close()
connection.close()