#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator that streams rows from user_data table one by one.
    """
    try:
        # connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # <-- change to your MySQL root password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)  # dictionary=True gives dict rows

        cursor.execute("SELECT * FROM user_data;")
        for row in cursor:
            yield row  # stream rows one at a time

    except Error as e:
        print(f"Error streaming users: {e}")
    finally:
        # Ensure resources are closed after generator finishes
        if cursor:
            cursor.close()
        if connection:
            connection.close()
