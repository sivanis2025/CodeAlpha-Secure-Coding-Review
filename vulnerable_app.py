import sqlite3

username = input("Enter Username: ")
password = input("Enter Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Login Failed")

conn.close()