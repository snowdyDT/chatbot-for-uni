import sqlite3
import pandas as pd

df = pd.read_csv('conversations.csv')

# Connect to the SQLite database
conn = sqlite3.connect('chatbot_for_uni.db')

# Create a table named 'conversations' and insert the data from the DataFrame
df.to_sql('conversations', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

# # Execute a SELECT query to fetch all rows from the conversations table
# c.execute("SELECT * FROM conversations")
#
# # Fetch all rows from the result set
# rows = c.fetchall()
#
# # Print the fetched rows
# for row in rows:
#     print(row)
#
# # Close the database connection
# conn.close()



# Connect to the SQLite database
# con = sqlite3.connect('chatbot_for_uni.db')
#
# # Create a cursor object
# cur = con.cursor()
#
# # Clear the table
# cur.execute("DELETE FROM conversations")
#
# # Commit the changes and close the connection
# con.commit()
# con.close()