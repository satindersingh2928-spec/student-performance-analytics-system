from utils.db_connection import get_connection


def get_average_attendance():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(attendance) FROM students"
    )

    average = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return round(average, 2)


def get_highest_attendance_student():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT student_name, attendance
    FROM students
    ORDER BY attendance DESC
    LIMIT 1
    """

    cursor.execute(query)

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return student

def get_lowest_attendance_student():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT student_name, attendance
    FROM students
    ORDER BY attendance ASC
    LIMIT 1
    """

    cursor.execute(query)

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return student

def get_attendance_defaulters():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT student_name, attendance
    FROM students
    WHERE attendance < 75
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students

def get_department_attendance_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT department, AVG(attendance)
    FROM students
    GROUP BY department
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result