import math

import psycopg2
from faker import Faker
fake = Faker()

# Connect to an existing database
conn = psycopg2.connect(dbname="postgres", user="postgres", password="secret", host="localhost", port=5432)

# Open a cursor to perform database operations
cur = conn.cursor()

# Drop table if it exists
cur.execute("DROP TABLE IF EXISTS test")

# Execute a command: this creates a new table
cur.execute("CREATE  TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",  (100, "abc'def"))
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",  (32, "class"))


for x in range(100):
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",  (32, fake.name()))


# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
# result = cur.fetchone()
for result in cur:
    print("Result: ")
    print(result)
    for x in result:
        print("X: ", x)
    #print(result[0])
    #print(result[1]) 
    #print(result[2])
# print(cur.fetchone())

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

