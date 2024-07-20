import sqlite3 as lite

con = lite.connect('appointments_management.db')


def create_form_data(info):
    with con:
        cur = con.cursor()
        query = (
            'INSERT INTO medical_appointments(name, email, phone_number, appointment_date, '
            'appointment_time, specialty, priority) VALUES (?, ?, ?, ?, ?, ?, ?)'
        )
        cur.execute(query, info)


def read_form_data():
    user_info = []
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM medical_appointments'
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            user_info.append(row)
    return user_info


def update_form_data(info):
    with con:
        cur = con.cursor()
        query = (
            'UPDATE medical_appointments SET name = ?, email = ?, phone_number = ?, appointment_date = ?, '
            'appointment_time = ?, specialty = ?, priority = ? WHERE id = ?')
        cur.execute(query, info)
        return cur.rowcount > 0


def delete_form_data(index):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM medical_appointments WHERE id = ?'
        cur.execute(query, index)
        