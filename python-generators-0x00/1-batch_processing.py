#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
    Generator that yields rows from user_data table in batches of batch_size.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # <-- change this to your actual MySQL password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data;")
        batch = []
        for row in cursor:                          # loop #1
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    except Error as e:
        print(f"Error streaming users in batches: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25 and prints them.
    """
    for batch in stream_users_in_batches(batch_size):   # loop #2
        # filter users over 25
        filtered = (user for user in batch if user['age'] > 25)  # generator expression (not a loop)
        for user in filtered:                                  # loop #3
            print(user)
