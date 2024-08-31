#this inserts all names into data base, 14000 of them, could not get it working in jupyter so #kept is seperate
import csv
import mysql.connector

# Establish the database connection
cnx = mysql.connector.connect(
    user='root', 
    password='Max123max123',
    host='127.0.0.1',
    database='Crypto_history')

cursor = cnx.cursor()

# Open the CSV file
with open(r'crypto_names_to_db.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if there is one
    for row in reader:
        # Prepare the insert statement
        insert_stmt = (
            "INSERT INTO Crypto_names (name, ticker) "
            "VALUES (%s, %s)"
        )
        # Execute the SQL statement
        cursor.execute(insert_stmt, row)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()

print("CSV data imported successfully.")
