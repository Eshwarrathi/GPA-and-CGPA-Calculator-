def calculate_cgpa(grades):
    grade_points = {'A+': 4.0, 'A': 3.75, 'A-': 3.5, 'B+': 3.25, 'B': 3.0, 'B-': 2.75,
                    'C+': 2.5, 'C': 2.0, 'C-': 1.5, 'F': 0.0}

    total_credits = 0
    total_grade_points = 0

    for course in grades:
        credit_hours = course['credit_hours']
        grade = course['grade']

        total_credits += credit_hours
        total_grade_points += grade_points[grade] * credit_hours

    cgpa = total_grade_points / total_credits
    return cgpa


def main():
    num_courses = int(input("Enter the number of courses: "))
    grades = []

    for i in range(num_courses):
        print(f"\nCourse {i + 1}:")
        credit_hours = int(input("Enter credit hours: "))
        grade = input("Enter grade (A+, A, A-, B+, B, B-, C+, C, C-, F): ")

        grades.append({'credit_hours': credit_hours, 'grade': grade})

    cgpa = calculate_cgpa(grades)
    print(f"\nCGPA: {cgpa:.2f}")


if __name__ == '__main__':
    main()
