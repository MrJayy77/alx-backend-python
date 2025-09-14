# Python Generators - 0x00

This project seeds a MySQL database (`ALX_prodev`) with sample user data from `user_data.csv`.

## Files
- `seed.py`: Handles database setup, table creation, and data insertion.
- `0-main.py`: Test script to run seeding.

## Functions
- `connect_db()` — connect to MySQL server.
- `create_database(connection)` — create `ALX_prodev` database.
- `connect_to_prodev()` — connect to the `ALX_prodev` database.
- `create_table(connection)` — create `user_data` table.
- `insert_data(connection, csv_file)` — insert CSV data into the table.

## Usage
```bash
python3 0-main.py
