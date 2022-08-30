## Basic Structure for importing into SQLite, does not work


import sqlite3, csv

def import_database(filename):
    connection = sqlite3.connect('biological_samples.db')
    cursor = connection.cursor()

    with open(filename, 'r') as file:
        for row in file:
            cursor.execute("INSERT INTO Database (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row.split(","))
            connection.commit()
    connection.close()