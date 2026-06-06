import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

username = input("Enter Username: ")
password = input("Enter Password: ")

if not username or not password:
    print("Username and password cannot be empty")
else:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, hashed_password))

    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Login Failed")

    conn.close()