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

# import pandas as pd

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

# import pandas as pd

# data={
#     "Name":["Anita","Rahul","Meera"],
#     "Salary":[60000,45000,40000],
#     "Department":["IT","HR","Finance"]
# }
# df=pd.DataFrame(data)

# df['Departments']=df['Department']
# df['EmployeeID']='EMP001'
# df['Bonus']=df['Salary']*0.10
# df.drop('EmployeeID',axis=1,inplace=True)
# df.drop(['Departments','Bonus'],axis=1,inplace=True)

# result=df[df['Salary']>50000]
# print(result)

# result=df[(df["Department"]=="IT")&(df["Salary"]>50000)]
# print(result)

# result=df[(df["Department"]=="IT")|(df["Salary"]>50000)]
# print(result)

# result=df[~(df["Department"]=="IT")]
# print(result)

# result=df[df["Department"].isin(["IT","HR"])]
# print(result)

# result=df[df["Name"].str.startswith("A")]
# print(result)

# result=df[df["Name"].str.endswith("a")]
# print(result)

# result=df[df["Name"].str.contains("ra")]
# print(result)

# print(df.isnull())

# print(df.isnull().sum())

# print(df.dropna())

# result=df["Salary"].fillna(df["Salary"].mean(),inplace=True)
# print(result)

# df["Department"]=df["Department"].fillna("Unknown")
# print(df)

# result=df.fillna(0,inplace=True)
# print(result)

# data={
#     "Name":["Anita","Rahul","Meera"],
#     "EmployeeID":[101,102,103]
# }
# df1=pd.DataFrame(data)
# print(df,df1)


# import pandas as pd
# data={
#     "Sales":[25000,30000,20000,40000,28000],
#     "Profit": [5000,7000,4000,10000,6000]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.describe())
# print(df["Sales"].count())
# print(df["Sales"].mean())
# print(df["Sales"].std())
# print(df["Sales"].min())
# print(df["Sales"].max())
# print(df["Sales"].median())
# print(df["Sales"].mode())
# print(df.sort_values(by="Sales"))
# print(df.sort_values(by="Sales",ascending=False))
# print(df.sort_values(by=["Sales","Profit"],ascending=[False,True]))

# df["Sales_Ranking"]=df["Sales"].rank(ascending=False)
# print(df)

# top_sales=df.sort_values(by="Sales",ascending=False).head(3)
# print(top_sales)

# print(df.tail())

# df["Region"]=["North","South","East","West","North"]
# print(df)
# print(df.groupby("Region")["Sales"].sum())
# print(df.groupby("Region")["Sales"].mean())
# print(df.groupby("Region")["Sales"].max())
# print(df.groupby("Region")["Sales"].min())
# print(df.groupby("Region").agg({"Sales":"sum","Profit":"mean"}))

# df.corr(numeric_only=True)
# df['Sales'].corr(df['Profit'])