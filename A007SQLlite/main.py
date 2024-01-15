import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS records 
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# INSERT (Create): Insert a row of data
cur.execute("INSERT INTO records (name, age) VALUES ('Alice', 30)")

# Commit the changes
conn.commit()

# SELECT (Read): Query the database
cur.execute("SELECT * FROM records")
print("Data after insertion:", cur.fetchall())

# UPDATE: Update data
cur.execute("UPDATE records SET age = 31 WHERE name = 'Alice'")

# Commit the changes
conn.commit()

# SELECT (Read): Query the database
cur.execute("SELECT * FROM records")
print("Data after update:", cur.fetchall())

# DELETE: Delete data
cur.execute("DELETE FROM records WHERE name = 'Alice'")

# Commit the changes
conn.commit()

# SELECT (Read): Query the database
cur.execute("SELECT * FROM records")
print("Data after deletion:", cur.fetchall())

# Close the connection
conn.close()
