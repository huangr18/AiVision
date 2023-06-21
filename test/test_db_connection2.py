import psycopg2
import sys

with open("PoseVideos/v7.mp4", "rb") as file:
    byte = file.read() # read a byte (a single character in text)
    #byte_val = ord(byte) # convert the string character into a number
    byte_array = bytearray(byte)
# Establish connection
connection = psycopg2.connect(
    host="localhost",
    port="9001",
    database="test",
    user="test",
    password="test"
)

# Create a cursor
cursor = connection.cursor()

# Execute CREATE TABLE statement
create_table_query = '''
CREATE TABLE IF NOT EXISTS test_for_video (
    id            SERIAL         PRIMARY KEY,
    name          VARCHAR(255),
    age           INTEGER,
    video         BYTEA
)
'''
cursor.execute(create_table_query)

# Insert data into the table
insert_data_query = '''
INSERT INTO test_for_video (name, age, video) VALUES (%s, %s, %s)
'''
data = [('John', 25, byte_array)]  # Example data
cursor.executemany(insert_data_query, data)

# Commit the changes
connection.commit()


# Execute SQL queries
cursor.execute("SELECT * FROM test_for_video")
result = cursor.fetchall()

# Print the query result
for row in result:
    print(row)

# Commit and close the connection
connection.commit()
connection.close()