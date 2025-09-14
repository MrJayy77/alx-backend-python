import seed

def stream_user_ages():
    """
    Generator that yields ages from user_data one by one.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:  # loop 1
        yield row['age']

    connection.close()


def calculate_average_age():
    """
    Calculates and prints the average age using the generator.
    """
    total = 0
    count = 0
    for age in stream_user_ages():  # loop 2
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average}")
    else:
        print("No users found.")


if __name__ == "__main__":
    calculate_average_age()
