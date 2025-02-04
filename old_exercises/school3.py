#!/var/www/test/.venv/bin/cgi_venv_launch

import os
import mysql.connector as database

username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")

conn = database.connect(
    user=username,
    password=password,
    host="localhost",
    database="school"
)
cursor = conn.cursor()

def add_student(first_name: str, last_name: str) -> None:
    try:
        statement = "INSERT INTO students (first_name,last_name) VALUES (%s, %s)"
        data = (first_name, last_name)
        cursor.execute(statement, data)
        conn.commit()
        print("Successfully added student to database")
    except database.Error as e:
        print(f"Error adding student to database: {e}")


def print_student_data(last_name: str) -> None:
    try:
        statement = "SELECT first_name, last_name FROM students WHERE last_name=%s"
        data = (last_name,)
        cursor.execute(statement, data)
        for first_name, last_name in cursor:
            print(f"Successfully retrieved student: {first_name}, {last_name}")
    except database.Error as e:
        print(f"Error retrieving entry from database: {e}")


def print_student_data_except(exclude_last_name: str) -> None:
    try:
        statement = "SELECT first_name, last_name FROM students WHERE last_name!=%s"
        data = (exclude_last_name,)
        cursor.execute(statement, data)
        for first_name, last_name in cursor:
            print(f"Successfully retrieved student: {first_name}, {last_name}")
    except database.Error as e:
        print(f"Error retrieving entry from database: {e}")


def print_student_data_first_like(first_name_like: str) -> None:
    try:
        statement = "SELECT first_name, last_name FROM students WHERE first_name LIKE %s"
        data = (first_name_like,)
        cursor.execute(statement, data)
        for first_name, last_name in cursor:
            print(f"Successfully retrieved student: {first_name}, {last_name}")
    except database.Error as e:
        print(f"Error retrieving entry from database: {e}")


print_student_data_first_like("Lu%")


conn.close()
