from analytics.attendance_analysis import (
    get_department_attendance_statistics
)

departments = get_department_attendance_statistics()

print("\nDepartment Wise Attendance")
print("-" * 35)

for dept in departments:

    print(f"Department: {dept[0]}")
    print(f"Average Attendance: {round(dept[1], 2)}%")

    print("-" * 35)