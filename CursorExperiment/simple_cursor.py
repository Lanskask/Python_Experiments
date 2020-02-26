import sqlite3

def getSingleRows():
    try:
        connection = sqlite3.connect('SQLite_Python.db')
        cursor = connection.cursor()
        print("Connected to database")

        sqlite_select_query = """SELECT * from database_developers"""
        cursor.execute(sqlite_select_query)
        print("Fetching single row")
        record = cursor.fetchone()
        print(record)

        print("Fetching next row")
        record = cursor.fetchone()
        print(record)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The Sqlite connection is closed")

getSingleRows()