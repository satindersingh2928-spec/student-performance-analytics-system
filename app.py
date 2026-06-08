from analytics.performance_analysis import (
    get_department_average_marks
)

departments = get_department_average_marks()

print("\nDepartment Wise Average Marks")
print("-" * 40)

for dept in departments:
    print(f"Department: {dept[0]}")
    print(f"Average Marks: {round(dept[1], 2)}")
    print("-" * 40)