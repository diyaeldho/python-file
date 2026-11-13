import numpy as np

# ======= ARRAY CREATION =======
# number=np.arange(1,21)
# print("Array:",number)                                  
# print("Number of elements:",number.size)
# print("Data type:",number.dtype)
# print("Dimension:",number.ndim)
# print("Shape:",number.shape)

# ======= EVEN AND ODD NUMBERS ========
# even=np.arange(2,51,2)                                   
# odd=np.arange(1,51,2)
# print("Even Numbers:",even)
# print("odd Number:",odd)
# print("Count of even number:",even.size)
# print("Count of odd number:",odd.size)

# ======= ARRAY INDEXING AND SLICING =======
# number=np.array([12,25,38,45,56,67,78,89,90,100])          
# print("First three:",number[:3])
# print("Last three:",number[-3:])
# print("Index 2 to 6:",number[2:7])
# print("Reverse:",number[::-1])
# number[4]=99
# print("After replacing fith number:",number)

# ======= CREATE A METRIX =======
# number=np.arange(1,10)                                       
# matrix=number.reshape(3,3)

# print("Matrix:\n",matrix)
# print("First row:",matrix[0])
# print("Last column:",matrix[:,2])
# print("Diagonal numbers:",matrix.diagonal())
# print("Sum of all elements:",matrix.sum())

# ======= RESHAPE AN ARRAY =======
# number=np.arange(1,25)                                   
# a=number.reshape(4,6)
# b=number.reshape(6,4)
# c=number.reshape(2,12)

# print("4*6 array:\n",a)
# print("shape:",a.shape)

# print("6*4 array:\n",b)
# print("Shape:",b.shape)

# print("2*12 array:\n",c)
# print("Shape:",c.shape)


# for rows, cols in [(4,6), (6,4), (2,12), (12,2)]:
#     result = number.reshape(rows, cols)
#     print(f"Shape {rows} x {cols}:")
#     print(result)
#     print("Shape:", result.shape)



# ======= ARITHEMETIC OPERATORS =======
# a=np.array([10,20,30,40,50])                                 
# b=np.array([2,4,5,8,10])
# print("Addition:",a+b)
# print("Substraction:",a-b)
# print("Mulitplication:",a*b)
# print("Division:",a/b)
# print("Pwer:",a**b)
# print(5//2)


# ======= ARRAY JOINING =======
# a=np.array([
#     [1,2],
#     [3,4]
# ])
# b=np.array([
#     [5,6],
#     [7,8]
# ])
# print("Concatenate:",np.concatenate((a,b)))
# print("Vertical stack:",np.vstack((a,b)))
# print("Horizontal stack:",np.hstack((a,b)))
# print("axis 0:",np.concatenate((a,b),axis=0))
# print("axis 1:",np.concatenate((a,b),axis=1))

# ======= SORTING AND SEARCHING =======
# numbers=np.array([12,45,89,34,67,23,90,56])
# print("Number:",numbers)
# print("Ascending order:",np.sort(numbers))
# print("Decending order:",np.sort(numbers)[::-1])
# print("Highest value:",np.max(numbers))
# print("Lowest value:",np.min(numbers))
# print("Index of higherst value:",np.argmax(numbers))
# print("index of lowest value:",np.argmin(numbers))
# print("Is 67 is present:",67 in numbers)


# ======== FILTERING VALUES =======
# salary=np.array([18000,2500,32000,45000,28000,55000,60000,22000,75000,40000])
# print("Salaries:",salary)
# print("Salaries greater than 30000:",salary[salary>30000])
# print("salary less than 25000:",salary[salary>25000])
# print("Salary in between 25000 and 50000:",salary[(salary>=25000) & (salary<=50000)])
# print("employees earning more than 40000:",np.sum(salary>4000))


#======= UNIQUE VALUES =======
# num=np.array([10,20,30,20,40,10,50,30,60,20])
# print("Numbers:",num)
# unique=np.unique(num)
# print("Unique values:",num)
# values, count=np.unique(num, return_counts=True)
# print("value occurance:")
# for i in range(len(values)):
#     print(values[i],":",count[i])
# duplicates=values[count>1]
# print("Duplicates values:",duplicates)

# ======= MATHEMATICAL AND STATISTICAL OPERATIONS =======
# marks=np.array([78, 85, 92, 45, 67, 89, 55, 76, 95, 62])
# print("Total:",np.sum(marks))
# print("Average mark:",np.mean(marks))
# print("Highest Mark:",np.max(marks))
# print("Lowest marks:",np.min(marks))
# print("Median:",np.median(marks))
# print("Standard Deviation:",round(np.std(marks),2))

# ======= VARIANCE AND STANDARD DEVIATION =======
# a=np.array([50,50,50,50,50])
# b=np.array([40,45,50,55,60])
# c=np.array([10,30,50,70,90])
# print("Mean:",np.mean(a))
# print("Mean:",np.mean(b))
#  print("Mean:",np.mean(c))
# variance_a=np.var(a)
# variance_b=np.var(b)
# variance_c=np.var(c)
# print("Variance:",variance_a)
# print("Variance:",variance_b)
# print("Variance:",variance_c)
# maximum=max(variance_a,variance_b,variance_c)
# print("Standard Deviation:",round(np.std(a),2))
# print("Standard Deviation:",round(np.std(b),2))
# print("Standard Deviation:",round(np.std(c),2))
# print("Dataset with highest variation:",maximum)

# ======= SUBJECT WISE AVERAGE =======
# marks=np.array([
#     [80,75,90],
#     [65,85,70],
#     [90,95,88],
#     [55,60,65],
#     [75,80,85]
# ])
# total=np.sum(marks,axis=1)
# print("total marks:",total)

# average=np.average(marks,axis=1)
# print("Average marks:",average)

# subject_avg=np.mean(marks,axis=0)
# print("Subject wise average:",subject_avg)

# highest=np.argmax(total)
# print("Highest score:",highest +1)
# print("total highest:",total[highest])

# ======= RANDOM NUMBER GENERATION =======
# np.random.seed(10)
# number=np.random.randint(1,101,20)
# print("Number:",number)
# print("Maximum number:",np.max(number))
# print("Minimum number:",np.min(number))
# print("mean:",np.mean(number))
# count=np.sum(number>50)
# print("Numbers greater than 50:",count)
# sorted_number=np.sort(number)
# print("Sorted numbers:",sorted_number)

# ======= PERCENTAGE AND RANKING =======
# marks=np.array([
#     [80,70,55,60],
#     [45,80,50,40],
#     [90,85,75,88],
#     [66,77,88,99],
#     [70,73,84,86]
# ])
# total=np.sum(marks,axis=1)
# print("Total marks:",marks)
# percentage=(total/400)*100
# print("Percentage:",percentage)
# print("Ascending order:",np.sort(marks))

# ========== EMPLOYEE SALARY ANALYSIS =======
# salary=np.array([18000,22000,25000,30000,35000,40000,45000,50000,55000,60000])
# print("Salary:",salary)
# print("Average salary:",np.mean(salary))
# print("Highest salary:",np.max(salary))
# print("Lowest Salary:",np.min(salary))
# print("Total salary:",np.sum(salary))
# above_avg=salary[salary>np.mean(salary)]
# print("above average salary:",above_avg)
# print("Standard Deviation:",round(np.std(salary),2))

# ======= WEEKLY SALES ANALYSIS =======
# sales=np.array([12000,15000,18000,10000,22000,25000,20000])
# days=np.array(["Monday","Tuesday","Wedensday","Thursday","Friday","Saturday","Sunday"])
# print("Total weekly sales:",np.sum(sales))
# print("Average daily sales:",np.mean(sales))
# print("Highest sales:",days[np.argmax(sales)])
# print("Lowest sales:",days[np.argmin(sales)])
# # print("Sales above 18000:",sales[sales>18000])
# # print("high to low:",np.sort(sales)[::-1])
# print("Days with sales above 18000")
# d=days[sales>18000]
# print(d)
# e=sales[sales>18000]
# print(e)
# for day, amount in zip(d,e):
#     print(day,":",amount)


# ======= ATTENDANCE ANALYSIS =======
# percentage=np.array([95, 88, 76, 65, 92, 55, 80, 45, 98, 72])
# print("Percentage above 75:",percentage[percentage>75])
# print("Percentage below 60:",percentage[percentage<60])
# print("Average attenadnce:",np.mean(percentage))
# print("Highest Attendance:",np.max(percentage))
# print("Lowest Attendance:",np.min(percentage))
# print(percentage>=75)
# count=np.sum(percentage>=75)
# print("Eligible attenadnce percentage:",count)

# ======= TEMPERATURE ANALYSIS =======
# temperature=np.array([29, 31, 30, 32, 28, 35, 33])
# print("Highest Temperature:",np.max(temperature))
# print("Lowest Temperature:",np.min(temperature))
# print("Average Temperature:",np.mean(temperature))
# print("Temperature Range:",np.max(temperature) - np.min(temperature))
# print("Temperature exceed 30:",temperature[temperature>30])

# ======= IMAGE ARRAY ANALYSIS =======
# image=np.array([
#      [10, 20, 30, 40, 50],
#     [60, 70, 80, 90, 100],
#     [110, 120, 130, 140, 150],
#     [160, 170, 180, 190, 200],
#     [210, 220, 230, 240, 250]
# ])
# print("Image:",image)
# print("Maximun:",np.max(image))
# print("Minimum:",np.min(image))
# print("Average:",np.mean(image))
# modified_image=image.copy()
# print(modified_image)
# modified_image[modified_image<100]=0
# modified_image[modified_image>200]=255
# print("Modified image:",modified_image)
# print(image)

# ======= STUDENT PERFORMANCE ANALYSIS SYSTEM =======
# marks = np.array([
#     [85, 90, 78, 88, 92],
#     [45, 55, 60, 70, 65],
#     [90, 95, 92, 88, 96],
#     [35, 60, 75, 80, 55],
#     [70, 75, 80, 85, 90],
#     [30, 35, 45, 50, 60],
#     [88, 82, 90, 85, 80],
#     [65, 70, 75, 80, 85],
#     [95, 92, 98, 96, 94],
#     [55, 60, 65, 70, 75]
# ])
# students=np.arange(1,11)
# print("Student Marks:\n",marks)
# total=np.sum(marks,axis=1)
# average=np.mean(marks,axis=1)
# print("Average marks:",average)
# print("\nSubject-wise average:",np.mean(marks,axis=0))
# topper=np.argmax(total)
# print("\nTopper: Student",students[topper])
# print("Highest total:",total[topper])
# print("\nStudents scoring below 40:",np.where(np.any(marks<40,axis=1))[0]+1)
# print("\nClass Average:",np.mean(marks))
# print("standard deviation:",np.std(marks))
# rank=np.argsort(-total)+1
# print("\nStudent ranking:",rank)
# passed=np.where(np.all(marks>=40,axis=1))[0]+1
# print("\nPassed all subjects:",passed)