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