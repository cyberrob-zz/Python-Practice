import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

cursor = connection.cursor()

word = input("Enter a word: ")

query = cursor.execute(f"SELECT * from Dictionary WHERE Expression = '{word}'")

results = cursor.fetchall()

if results:
    for reuslt in results:
        print(reuslt[1])
else:
    print("No definition found.")
