# import pandas as pd
# print("pandas version:",pd.__version__)
# ls=[10,20,30]
# print(ls)
# print(type(ls))

# data=pd.Series(ls)
# print(data)
# print(type(data))

# data=pd.Series([10,20,30,40,50])
# print(data)
# print(type(data))

# marks=pd.Series([85,90,76,92,68])
# print("first mark:",marks[0])
# print("average mark:",marks.mean())
# print("maximum:",marks.max())

# marks=pd.Series(                                      #custom indexes
#     [85,90,75,92],
#     index=["Anu","Ciya","Rithu","Akki"]
# )
# print(marks)
# print("Anu's marks:",marks["Anu"])
# print("Marks above80:")
# print(marks[marks>80])

# salary={                                                #series from dictionary
#     "Anita":50000,
#     "Rahul":45000,
#     "Meera":70000
# }
# salary_series=pd.Series(salary)
# print(salary_series)

# monthly_sales=pd.Series(
#     [25000,30000,45000],
#     index=["Jan","Feb","Mar"]
# )

# print(monthly_sales)
# print(monthly_sales["Jan"])                          #accessing data using index
# print(monthly_sales.iloc[0])                         #accessing using position

# print(monthly_sales["Jan":"Feb"])                    #slicing
# print(monthly_sales[0:2])
# print(monthly_sales+5000)                            #Arithemetic operatoions (boardcasting)

# print(monthly_sales.mean())                          #Statistical operations
# print(monthly_sales.max())
# print(monthly_sales.min())

# high_sales=monthly_sales[monthly_sales>26000]         #filtering series
# print(high_sales)


#Data Frame

import pandas as pd

# data={
#     "Name":["Anita","Rahul","Meera"],
#     "Age":[22, 24, 23],
#     "Course":["Analytics","Python","Analytics"]
# }
# df=pd.DataFrame(data)
# print(df)
# print(type(df))
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())

# print(df["Name"])                             #indexing and selecting rows and columns
# print(type(df["Name"]))

# print(df[["Name","Course"]])                    #selecting multiple columns

# df=pd.read_csv("student.csv")
# print(df)
# print(df)
# print(type(df))
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())