import csv
import mysql.connector

#connect to data base
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Max123max123',  # Replace with your password
    database='Crypto_history'  # Replace with your database name
)
keywords = ["buy", 'sell', 'positive', 'negative']
#open the CSV file
file_name = 'keywordcsv.csv'
with open(file_name, mode = "r") as file:
    csv_reader = csv.reader(file)

    #now I will read it and pull out keywords
