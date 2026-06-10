from flask import Flask, render_template, request, redirect, send_file, Response
import csv
from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Table
from models.student import (
    add_student,
    delete_student,
    get_student_by_id,
    update_student,
    get_all_students,
    get_total_students,
    get_average_marks,
    get_top_performer,
    get_average_attendance,
    get_department_counts,
    search_students,
    get_department_average_marks,
    get_top_5_students,
    get_low_performers,
    get_low_attendance_students,
    get_department_toppers,
    get_performance_categories,
    get_student_details,
    get_students_count,
    get_total_pages
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    total_students = get_total_students()

    average_marks = get_average_marks()

    top_student = get_top_performer()
    
    average_attendance = get_average_attendance()
    
    department_counts = get_department_counts()
    
    department_avg_marks = get_department_average_marks()
    
    top_5_students = get_top_5_students()
    
    low_performers = get_low_performers()
    
    low_attendance_students = get_low_attendance_students()
    
    department_toppers = get_department_toppers()
    
    performance_data = get_performance_categories()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        average_marks=average_marks,
        top_student=top_student,
        average_attendance=average_attendance,
        department_counts=department_counts,
        department_avg_marks=department_avg_marks,
        top_5_students=top_5_students,
        low_performers=low_performers,
        low_attendance_students=low_attendance_students,
        department_toppers=department_toppers,
        performance_data=performance_data
    )
    
@app.route("/students")
def students():

    search_query = request.args.get("search")
    sort_by = request.args.get("sort")
    page = request.args.get("page", 1, type=int)

    if search_query:

        students_data = search_students(search_query)

    else:
        students_data = get_all_students(sort_by, page)
        
    total_students = get_students_count()
    total_pages = get_total_pages()

    return render_template(
    "students.html",
    students=students_data,
    search_query=search_query,
    sort_by=sort_by,
    page=page,
    total_students=total_students,
    total_pages=total_pages
)
    
@app.route("/add-student", methods=["GET", "POST"])
def add_student_page():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        semester = request.form["semester"]
        marks = request.form["marks"]
        attendance = request.form["attendance"]

        add_student(
            name,
            email,
            department,
            semester,
            marks,
            attendance
        )

        return redirect("/students")

    return render_template("add_student.html")

@app.route("/delete-student/<int:student_id>")
def delete_student_route(student_id):

    delete_student(student_id)

    return redirect("/students")

@app.route("/edit-student/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    if request.method == "POST":

        marks = request.form["marks"]
        attendance = request.form["attendance"]

        update_student(
            student_id,
            marks,
            attendance
        )

        return redirect("/students")

    student = get_student_by_id(student_id)

    return render_template(
        "edit_student.html",
        student=student
    )
    
@app.route("/export-csv")
def export_csv():

    students = get_all_students()

    def generate():

        yield "ID,Name,Email,Department,Year,Marks,Attendance\n"

        for student in students:

            row = f"{student[0]},{student[1]},{student[2]},{student[3]},{student[4]},{student[5]},{student[6]}\n"

            yield row

    return Response(
        generate(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=students.csv"
        }
    )
    
@app.route("/export-excel")
def export_excel():

    students = get_all_students()

    workbook = Workbook()
    sheet = workbook.active

    sheet.title = "Students Data"

    # Header Row
    sheet.append([
        "ID",
        "Name",
        "Email",
        "Department",
        "Year",
        "Marks",
        "Attendance"
    ])

    # Student Data
    for student in students:
        sheet.append(student)

    file_name = "students.xlsx"

    workbook.save(file_name)

    return send_file(
        file_name,
        as_attachment=True
    )
    
@app.route("/export-pdf")
def export_pdf():

    students = get_all_students()

    pdf_file = "students_report.pdf"

    document = SimpleDocTemplate(pdf_file)

    data = [
        ["ID", "Name", "Department", "Marks", "Attendance"]
    ]

    for student in students:

        data.append([
            student[0],
            student[1],
            student[3],
            student[5],
            student[6]
        ])

    table = Table(data)

    elements = [table]

    document.build(elements)

    return send_file(
        pdf_file,
        as_attachment=True
    )
    
@app.route("/student/<int:student_id>")
def student_details(student_id):

    student = get_student_details(student_id)

    return render_template(
        "student_details.html",
        student=student
    )

if __name__ == "__main__":
    app.run(debug=True)
    
