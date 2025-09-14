# 0-databaseconnection.py
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        # store the database name
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        # open the database connection
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # close the connection
        if self.conn:
            self.conn.close()

# Use the context manager
with DatabaseConnection('users.db') as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
