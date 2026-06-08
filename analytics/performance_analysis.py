from utils.db_connection import get_connection


def get_total_students():

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM students"

    cursor.execute(query)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

def get_average_marks():

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT AVG(marks) FROM students"

    cursor.execute(query)

    average = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return round(average, 2)

def get_top_performer():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT student_name, marks
    FROM students
    ORDER BY marks DESC
    LIMIT 1
    """

    cursor.execute(query)

    top_student = cursor.fetchone()

    cursor.close()
    conn.close()

    return top_student

def get_lowest_performer():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT student_name, marks
    FROM students
    ORDER BY marks ASC
    LIMIT 1
    """

    cursor.execute(query)

    lowest_student = cursor.fetchone()

    cursor.close()
    conn.close()

    return lowest_student

def get_pass_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE marks >= 40"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

def get_fail_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE marks < 40"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

def get_department_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT department, COUNT(*)
    FROM students
    GROUP BY department
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def get_department_average_marks():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT department, AVG(marks)
    FROM students
    GROUP BY department
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result