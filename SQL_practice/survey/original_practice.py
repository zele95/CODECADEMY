# Write a Python program that creates a new database in a file
# called original.db containing a single
# table called Pressure, with a single field 
# called reading, and inserts 100,000 random numbers
# between 10.0 and 25.0. How long does it take this program to run?
# How long does it take to run a program that simply writes those random numbers to a file?

import sqlite3

# import random number generator
from numpy.random import uniform
import timeit


start = timeit.default_timer()
random_numbers = uniform(low=10.0, high=25.0, size=100000)

connection = sqlite3.connect("original.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Pressure (reading float not null)")
query = "INSERT INTO Pressure (reading) VALUES (?);"

for number in random_numbers:
    cursor.execute(query, [number])

cursor.close()
# save changes to file for next exercise
connection.commit()
connection.close()

stop = timeit.default_timer()

print('Time SQL: ', stop - start) 


start = timeit.default_timer()
# write random numbers to a file
random_numbers = uniform(low=10.0, high=25.0, size=100000)
with open('random_numbers.txt', 'w') as outfile:
    for number in random_numbers:
        # need to add linebreak \n
        outfile.write("{}\n".format(number))

stop = timeit.default_timer()

print('Time python: ', stop - start)  