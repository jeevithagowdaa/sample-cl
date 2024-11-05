# Define a list of students with their grades
students_grades = {
    "Alice": [85, 90, 78],
    "Bob": [75, 80, 82],
    "Charlie": [95, 88, 92],
    "Diana": [70, 65, 72]
}

# Calculate average grade for each student
averages = {}
for student, grades in students_grades.items():
    averages[student] = sum(grades) / len(grades)

# Write the results to a text file
with open("student_averages.txt", "w") as file:
    for student, average in averages.items():
        file.write(f"{student}: {average:.2f}\n")

print("Average grades have been written to student_averages.txt")
