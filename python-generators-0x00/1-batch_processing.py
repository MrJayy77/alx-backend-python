import sqlite3

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the database."""
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:  # loop 1
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield [dict(row) for row in rows]

    conn.close()


def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):  # loop 2
        for user in batch:  # loop 3
            if user['age'] > 25:
                print(user)
