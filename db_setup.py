import sqlite3 as lite

con = lite.connect('appointments_management.db')

with con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE medical_appointments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            specialty TEXT NOT NULL,
            priority  TEXT NOT NULL
    )""")
