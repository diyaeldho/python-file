
# Student Information and Grading System

# 1. Student Details
# name = input("Enter Student Name: ")
# age = int(input("Enter Age: "))
# course = input("Enter Course: ")
# status = input("Enter Employment Status: ")
# stipend = float(input("Enter Monthly Stipend: "))

# 2. String Operations
# print("\nName:", name)
# print("First 3 Letters:", name[:3])
# print("Uppercase Name:", name.upper())

# 3. Tuple
# student = (name, age, course, status, stipend)
# print("\nStudent Details:", student)

# 4. List Operations
# marks = [80, 90, 70, 80, 60]
# print("\nOriginal Marks:", marks)

# marks.append(95)
# print("After Adding:", marks)

# marks.remove(60)
# print("After Removing:", marks)

# marks.sort()
# print("Sorted Marks:", marks)

# unique_marks = list(set(marks))
# print("Unique Marks:", unique_marks)

# 5. Dictionary
# subjects = {
#     "Python": 80,
#     "MySQL": 90,
#     "Excel": 70
# }

# subjects["Python"] = 95
# subjects["Power BI"] = 85

# print("\nSubject Marks:", subjects)

# 6. Frozenset
# fixed_subjects = frozenset(["Python", "MySQL", "Excel"])
# print("Frozenset:", fixed_subjects)

# 7. Set Operations
# online = {"Anu", "Rahul", "John"}
# offline = {"Rahul", "John", "Meera"}

# print("\nCommon Students:", online & offline)
# print("All Students:", online | offline)
# print("Only Online Students:", online - offline)

# 8. Average Marks
# average = sum(subjects.values()) / len(subjects)

# # 9. Grade Calculation
# if average >= 90:
#     grade = "A"
# elif average >= 75:
#     grade = "B"
# elif average >= 50:
#     grade = "C"
# else:
#     grade = "Fail"

# 10. Final Output
# print("\n----- STUDENT PROFILE -----")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Course: {course}")
# print(f"Employment Status: {status}")
# print(f"Monthly Stipend: {stipend}")
# print(f"Average Marks: {average:.2f}")
# print(f"Grade: {grade}")

# 11. Data Types
# print("\nData Types:")
# print(type(name))
# print(type(age))
# print(type(stipend))
# print(type(student))
# print(type(marks))
# print(type(subjects))
# print(type(fixed_subjects))
