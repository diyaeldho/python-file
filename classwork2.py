import pandas as pd  
# data = { 
#     'Employee': [ 'Arun', 'Anu', 'Rahul', 'Meera', 'John',         
#                  'Priya', 'David', 'Sara', 'Kevin', 'Neha',         
#                  'Arun', 'Meera', 'John', 'Priya', 'David'],      
#     'Region': ['North', 'South', 'West', 'North', 'South',         
#                'West', 'North', 'South', 'West', 'North',         
#                'South', 'West', 'North', 'South', 'West'],      
#     'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile',         
#                 'Laptop', 'Tablet', 'Mobile', 'Laptop', 'Tablet',        
#                   'Mobile', 'Laptop', 'Tablet', 'Mobile', 'Laptop'],      
#     'Sales': [ 45000, 30000, 25000, 55000, 35000,        
#                60000, 20000, 40000, 75000, 15000,         
#                32000, 50000, 28000, 42000, 65000 ],      
#     'Profit': [9000, 6000, 5000, 11000, 7000,        
#                 12000, 4000, 8000, 15000, 3000,         
#                 6500, 10000, 5500, 8500, 13000],      
#     'Quantity': [2, 3, 1, 4, 2,         
#                  5, 1, 3, 4, 1,         
#                  2, 3, 2, 4, 5]
#  }  
# df = pd.DataFrame(data) 
# print(df)

# print(df.head(5))
# print(df.tail(5))
# print(df.describe())
# print(df['Sales'].count())
# print(df['Sales'].mean())
# print(df['Sales'].max())
# print(df['Sales'].min())
# print(df['Profit'].mean())
# print(df['Sales'].median())
# print(df['Sales'].std())
# print(df['Sales'].mode())

# print(df.sort_values(by='Sales'))
# print(df.sort_values(by='Sales',ascending=False))
# print(df.head(5))
# print(df.tail(5))
# print(df.sort_values(by='Profit',ascending=False))
# print(df.sort_values(by=['Sales','Profit'],ascending=[False,True]))
# df['Sales_Rank']=df['Sales'].rank(ascending=False)
# print(df)
# print(df.sort_values(by='Sales_Rank',ascending=False))

# print(df.groupby('Region')['Sales'].sum())
# print(df.groupby('Region')['Sales'].mean())
# print(df.groupby('Region')['Sales'].max())
# print(df.groupby('Region')['Sales'].min())
# print(df.groupby('Region')['Profit'].sum())
# print(df.groupby('Region')['Quantity'].sum())
# print(df.groupby('Product')['Sales'].sum())
# print(df.groupby('Product')['Profit'].mean())
# print(df.groupby('Region').agg({'Sales':'sum','Profit':'mean'}))






