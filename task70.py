# marks=[40.50,60,80,45,75]
# passed=[]
# for m in marks:
#     if m>=50:
#         passed.append(m)
# print("Passed:",passed)

# distinction=[m for m in marks if m>=75]
# print("Distinction:",distinction)

# square=[m for m in passed]
# print("Squares:",square)

# def add(a,b):
#     return a+b
# def average(m):
#     return sum(m)/len(m)
# def grade(m):
#     if m>=90:
#         return"A"
#     elif m>=75:
#         return "B"
#     elif m>=50:
#         return "C"
#     else:
#         return "failed"
# print("Adition:",add(10,20))
# print("Average:",average(marks))
# print("Grade:",grade(85))

# def avg(*m):
#     print("Average:",sum(m)/len(m))
# avg(80,90,70)

# def profile(**data):
#     print(data)
# profile(name="Anu", age=22, course="MBA")

# class Employee:
#     def __init__(self, id, name, dept, salary):
#         self.id=id
#         self.name=name
#         self.dept=dept
#         self.salary=salary

#     def display(self):
#         print(self.id, self.name, self.dept, self.salary)
#     def annual(self):
#         print("Annual Salary:", self.salary*12)
#     def high_earner(self):
#         print("high_earner:", self.salary>=50000)
        
# e = Employee(101,"Arun","Finance", 55000)
# e.display()
# e.annual()
# e.high_earner()

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name, self.age)

# class Student(Person):
#     def __init__(self, name, age, sid, marks):
#         super().__init__(name, age)
#         self.sid=sid
#         self.marks=marks

#     def details(self):
#         self.dispaly()
#         print(self.sid, self.marks)

#     def result(self):
#         if self.marks>=50:
#             print("passed")
#         else:
#             print("failed")

# s=Student("Anu",22,201,85)
# s.display()
# s.result()