import sqlite3

def stream_users_in_batches(batch_size):
    """
    Generator: Yields batches (lists) of users from the user_data table.
    """
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:  # loop 1
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        # Convert rows to dicts and yield them as one batch
        yield [dict(row) for row in rows]

    conn.close()


def batch_processing(batch_size):
    """
    Generator: Iterates over batches and yields users over age 25.
    """
    for batch in stream_users_in_batches(batch_size):  # loop 2
        for user in batch:  # loop 3
            if user['age'] > 25:
                yield user   # <---- yield generator used here
