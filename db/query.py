import sqlite3
from datetime import datetime

from db.initial_db import create_connection


def get_information(name: str) -> list:
    with create_connection() as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM people WHERE name = ?;", (name,))
        result = cursor.fetchall()
        return result


def insert_data(data: dict) -> None:
    today = datetime.now().isoformat()
    data['created_at'] = today
    try:
        with create_connection() as con:
            cursor = con.cursor()
            cursor.execute(
                """
                INSERT INTO
                people (name, gender, age, nationality, created_at)
                VALUES
                (?, ?, ?, ?, ?);
                """,
                (data['name'], data['gender'], data['age'],
                 data['nationality'], data['created_at'])
            )
    except sqlite3.IntegrityError as e:
        print(f"The error '{e}' occurred")
