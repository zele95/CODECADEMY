# Write a Python program that creates a new database called 
# backup.db with the same structure as original.db and copies 
# all the values greater than 20.0 from original.db to backup.db. 
# Which is faster: filtering values in the query, or reading everything 
# into memory and filtering in Python?

import sqlite3
import timeit


start = timeit.default_timer()

connection_original = sqlite3.connect("original.db")
cursor_original = connection_original.cursor()
cursor_original.execute("SELECT * FROM Pressure;")
results = cursor_original.fetchall()
cursor_original.close()
connection_original.close()

connection_backup = sqlite3.connect("backup.db")
cursor_backup = connection_backup.cursor()
cursor_backup.execute("CREATE TABLE Pressure (reading float not null)")
query = "INSERT INTO Pressure (reading) VALUES (?);"

for entry in results:
    # number is saved in first column of the table
    if entry[0] > 20.0:
        cursor_backup.execute(query, entry)

cursor_backup.close()
connection_backup.commit()
connection_backup.close()

stop = timeit.default_timer()

print('Time SQL: ', stop - start) 

# delete pressure table
# ...

start = timeit.default_timer()

connection_original = sqlite3.connect("original.db")
cursor_original = connection_original.cursor()
cursor_original.execute("SELECT * FROM Pressure WHERE reading > 20.0;")
results = cursor_original.fetchall()
cursor_original.close()
connection_original.close()

connection_backup = sqlite3.connect("backup.db")
cursor_backup = connection_backup.cursor()
cursor_backup.execute("CREATE TABLE Pressure (reading float not null)")
query = "INSERT INTO Pressure (reading) VALUES (?);"

for entry in results:
    cursor_backup.execute(query, entry)

cursor_backup.close()
connection_backup.commit()
connection_backup.close()

stop = timeit.default_timer()

print('Time python: ', stop - start) 