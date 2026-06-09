from flask import Flask, render_template
from models.student import (
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

if __name__ == "__main__":
    app.run(debug=True)
    
