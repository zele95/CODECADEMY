# Import pandas with alias
import pandas as pd
# Import sqlite3
import sqlite3
 
# CREATE A DATABASE
# # Use read_csv to read in data as a pandas dataframe
# df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# # Show DataFrame
# print(df)
# # Instantiate a connection
# connection = sqlite3.connect("titanic.db")
# # Instantiate a cursor
# cursor = connection.cursor()
# # Create a table
# df.to_sql("titanic", connection)

# Instantiate a connection
connection = sqlite3.connect("titanic.db")
# Instantiate a cursor
cursor = connection.cursor()

# Create first_five object
first_five = cursor.execute('''SELECT * FROM titanic''').fetchmany(5)
#Print first_five
print(first_five)

# Create fifties object
fifties = cursor.execute('''SELECT * FROM titanic WHERE age = 50.0''').fetchall()
# Print fifties object
print(fifties)

# Create femme object
femme = cursor.execute('''SELECT COUNT(*) FROM titanic WHERE Sex = 'female'; ''').fetchall()
# Print femme object
print(femme)

# Create new_df DataFrame
new_df = pd.read_sql_query('''SELECT * from titanic''',connection)
# Print new_df
print(new_df)

cursor.close()
connection.close()