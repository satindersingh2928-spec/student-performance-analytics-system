from flask import Flask, render_template, request, redirect
from models.student import (
    add_student,
    delete_student,
    get_student_by_id,
    update_student,
    get_all_students,
    get_total_students,
    get_average_marks,
    get_top_performer
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

    return render_template(
        "dashboard.html",
        total_students=total_students,
        average_marks=average_marks,
        top_student=top_student
    )
    
@app.route("/students")
def students():

    students_data = get_all_students()

    print(students_data)

    return render_template(
        "students.html",
        students=students_data
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

if __name__ == "__main__":
    app.run(debug=True)
    
