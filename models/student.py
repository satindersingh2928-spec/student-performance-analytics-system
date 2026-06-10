from utils.db_connection import get_connection


def add_student(name, email, department, year, marks, attendance):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students
    (student_name, email, department, year_of_study, marks, attendance)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (name, email, department, year, marks, attendance)

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    print("Student Added Successfully!")
    
def get_all_students():

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students

def search_students(search_query):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT * FROM students
    WHERE student_name LIKE %s
    """

    cursor.execute(query, ('%' + search_query + '%',))

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students

def get_student_by_id(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return student

def update_student(student_id, marks, attendance):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE students
    SET marks = %s,
        attendance = %s
    WHERE student_id = %s
    """

    values = (marks, attendance, student_id)

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    print("Student Updated Successfully!")
    
def delete_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    conn.commit()

    cursor.close()
    conn.close()

    print("Student Deleted Successfully!")
    
def get_total_students():

    students = get_all_students()

    return len(students)

def get_average_marks():

    students = get_all_students()

    total_marks = 0

    for student in students:

        total_marks += float(student[5])

    average = total_marks / len(students)

    return round(average, 2)

def get_top_performer():

    students = get_all_students()

    top_student = students[0]

    for student in students:

        if student[5] > top_student[5]:

            top_student = student

    return top_student

def get_average_attendance():

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT AVG(attendance) FROM students"

    cursor.execute(query)

    average_attendance = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return round(float(average_attendance), 2)

def get_department_counts():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT department, COUNT(*)
    FROM students
    GROUP BY department
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

def get_department_average_marks():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT department, AVG(marks)
    FROM students
    GROUP BY department
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

def get_top_5_students():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM students
    ORDER BY marks DESC
    LIMIT 5
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students

def get_low_performers():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM students
    WHERE marks < 70
    ORDER BY marks ASC
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students

def get_low_attendance_students():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM students
    WHERE attendance < 75
    ORDER BY attendance ASC
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students

def get_department_toppers():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT s1.department,
           s1.student_name,
           s1.marks
    FROM students s1
    WHERE s1.marks = (
        SELECT MAX(s2.marks)
        FROM students s2
        WHERE s2.department = s1.department
    )
    ORDER BY s1.department
    """

    cursor.execute(query)

    toppers = cursor.fetchall()

    cursor.close()
    conn.close()

    return toppers

def get_performance_categories():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        SUM(CASE WHEN marks >= 90 THEN 1 ELSE 0 END) AS Excellent,
        SUM(CASE WHEN marks >= 75 AND marks < 90 THEN 1 ELSE 0 END) AS Good,
        SUM(CASE WHEN marks >= 60 AND marks < 75 THEN 1 ELSE 0 END) AS Average,
        SUM(CASE WHEN marks < 60 THEN 1 ELSE 0 END) AS Poor
    FROM students
    """

    cursor.execute(query)

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data