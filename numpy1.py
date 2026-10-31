# import numpy as np                          #version
# print(np.__version__)

# import numpy as np
# numbers=np.array([10,20,30,])                  #np.array()
# print(numbers)
# print(type(numbers))
                                                
# a=np.zeros(3)                                   #bilt-in function
# print("zeros:",a)        

# b=np.ones(3)
# print("ones:",b)

# c=np.arange(1,11)
# print("range:",c)

# d=np.arange(2,21,2)
# print("range with step:",d)

# e=np.arange(1,21,2)
# print("range with step:",e)

# e=np.linspace(1,10,3)
# print("linspace:",e)

# import numpy as np
# a=np.array([10,20,30,40,50])
# b=np.array([
#     [10,20,30,40],
#     [10,30,50,40]
# ])
# print("1D array:")
# print(a)

# print("2D array:")
# print(b)

# # print("Dimensions:",a.ndim)
# # print("shape:",a.shape)
# # print("total elements:",a.size)

# print("Dimensions:",b.ndim)                        #shape returns the number of rows and columns,while size retruns total number of elements
# print("shape:",b.shape)
# print("total elements:",b.size)

# a=np.array([10,20,30])
# b=np.array([2.5,3.5,5.5])
# c=np.array([True,False])
# d=np.zeros(5)

# print(a.dtype)
# print(b.dtype)
# print(c.dtype)
# print(d.dtype)

# marks=np.array([80,60,75,45])
# print("first marks:",marks[0])
# print("third marks:",marks[2])
# print("last marks:",marks[-1])

# marks[1]=65

# print("updated marks:",marks)


# import numpy as np
# numbers=np.array([75,82,68,91,88])                       #task1
# print(numbers)

# a=np.zeros(5)
# print("zeros:",a)

# b=np.ones(5)
# print("ones:",b)

# c=np.arange(10,20)
# print("rannge:",c)

# d=np.arange(2,21,2)
# print("range:",d)

# e=np.linspace(1,10,5)
# print("linspace:",e)

# import numpy as np
# student_marks=np.array([                            #task2 and 3
#     [75,82,68],
#     [91,88,95],
#     [65,72,80]
# ])
# print(student_marks)

# print("number of dimensions:",student_marks.ndim)
# print("shape of the array:",student_marks.shape)
# print("total number of elements:",student_marks.size)
# print("data type of the array:",student_marks.dtype)


# import numpy as np
# marks=np.array([75,82,68,91,88])                       #task4
# print("first mark:",marks[0])
# print("third mark:",marks[2])
# print("last mark:",marks[-1])
# print("second last mark:",[-2])
# marks[1]=90
# marks[-1]=95
# print("updated mark:",marks)

# import numpy as np
# ages=np.array([18,20,19,21,18])                         #task5
# print("first age:",ages[0])
# print("last age:",ages[-1])
# ages[2]=22
# print("updated age:",ages)
# print("shape:",ages.shape)
# print("dimensions:",ages.ndim)
# print("elements:",ages.size)
# print("datatype:",ages.dtype)

# students={
#     "Rithu":{"Python":85, "SQL":90, "Excel":80},
#     "Rahul":{"Python":95, "SQL":88, "Excel":92},
#     "Gokul":{"Python":75, "SQL":85, "Excel":90},
# }
# while True:
#     print("\n===== STUDENT MARKS MANAGEMNET SYSTEM =====")
#     print("1. Display all Students")
#     print("2. Search for a students")
#     print("3. Calculate Total and Average")
#     print("4. Find Class topper")
#     print("5. update marks")
#     print("6. Add a New Student")
#     print("7. Display subject-wise Topper")
#     print("8. Exit")

#     choice=input("Enter your choice")

#     if choice=="1":
#         for name, marks in students.items():
#             print("\nstduents:", name)
#             for subject, marks in marks.items():
#                 print(subject,":",marks)

#     elif choice=="2":
#         name==input("Enter student name: ")
#         if name in students:
#             print("marks of:", name, ":", students[name])
#         else:
#             print("stdeunt not found!")

#     elif choice=="3":
#         for name,marks in students.items():
#             total = sum(marks.value())
#             average=total/len(marks)

#             print("\nstudents:",name)
#             print("Total marks", total)
#             print("average marks:",round(average,2))

#     elif choice=="4":
#         topper = max(students, key=lambda name: sum(students[name].values()))
#         total=sum(students[topper].values())

#         print("class topper:",topper)
#         print("total marks:0",total)

#     elif choice=="5":
#         name=input("Enter student name: ")
#         if name in students:
#             subject = input("Enter subject (Python/SQL/excel): ")
#             if subject in students[name]:
#                 marks=int(input("Enter new marks: "))
#                 students[name][subject]=marks
#                 print("marks updated successfully!")
#             else:
#                 print("Invalid subject")
#         else:
#             print("student not found!")

#     elif choice =="6":
#         name=input("Enter new students name:")
#         if name in students:
#             print("Students already exists!")
#         else:
#             Python=int(input("Enter Python marks:"))
#             SQL=int(input("Enter SQL marks:"))
#             Excel=int(input("Enter Excel Marks:"))

#             students[name]={
#                 "Python":python,
#                 "SQL":sql,
#                 "Excel":excel,
#             }
#             print("Student added sucessfully!")
            
#     elif choice=="7":
#         subject=["Python","SQL","Excel"]
#         for subject in subject:
#             topper=max(
#                 students,
#                 key=lambda name: students[name][students]
#             )
#             print(
#                 subject,
#                 "Topper:",
#                 topper,
#                 "-Marks:",
#                 students[topper][subject]
#             )
#     elif choice=="8":
#         print("Thank you for using the studnet Marks Management Systems!")
#         break
#     else:
#         print("Invalid choice! Please enter a number from 1 to 8.")

# import numpy as np

# marks=np.array([
#     [80,85,90],
#     [70,75,80],
#     [90,95,85]
# ])
# print("First row:",marks[0])
# print("Second row, third subject:",marks[1,2])
# print("First column:", marks[:,0])
# print(marks[:2,:])

# import numpy as np
# a=np.array([10,20,30])
# b=np.array([1,2,3])
# print("Addition:",a+b)
# print("Substraction:",a-b)
# print("Multiplication:",a*b)
# print("Division:",a/b)
# print("power:",a**2)

# import numpy as np
# marks=np.array([65,70,80,85,90,95])
# print("Total:",np.sum(marks))
# print("average:",np.mean(marks))
# print("Median:",np.median(marks))
# print("Minimum:",np.min(marks))
# print("maximum:",np.max(marks))
# print("Standard Deviation:",round(np.std(marks),2))

# import numpy as np
# marks=np.array([                             
#     [70,75,80,],                            
# ])
# print("Student averages:")
# print(np.mean(marks,axis=1))                       #axis=0: performs the opeartion column wise, giving subject averages

# print("student average:")                           #axis=1: performs the operations row wise, giving student averages
# print(np.mean(marks,axis=0))

# print("Student averages:")
# print(np.sum(marks,axis=1))

# import numpy as np
# np.random.seed(10) 
# a=np.random.randint(1,101,size=5)                 #randint()generates random intergers, while rand() gemerates randpom decimal values between 0 to 1
# b=np.random.rand(5)
# print("random integers:",a)                       #using np.random.seed(10) makes the result reproducible
# print("random decimals:",b)

# import numpy as np
# marks = np.array([78,45,92,65,88,54])             #np.sort() returns a sorted array without changing the original array
# sorted_marks = np.sort(marks)
# print("ascending:",sorted_marks)
# print("descending:",np.sort(marks[::-1]))
# print("original:",marks)

# import numpy as np
# numbers=np.arange(1,13)                              #reshape an array
# matrix=numbers.reshape(3,4)
# print(numbers)
# print(matrix)
# print("Shape:",matrix.shape)

# import numpy as np                                   #join two arrays
# a=np.array([10,20,30])
# b=np.array([40,50,60])
# print("concateante:",np.concatenate((a,b)))
# print("vertical stack:",np.vstack((a,b)))
# print("horizontal stack:",np.hstack((a,b)))

# import numpy as np                                   #filter values using conditions
# marks=np.array([45,78,32,90,65,28,85])
# passed=marks[marks>=40]                              # this is called boolen indexing and is especially used in data analysis
# failed=marks[marks<40]
# high_score=marks[marks>=80]
# print("passed:",passed)
# print("failed:",failed)
# print("high score:",high_score)