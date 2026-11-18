# ======== Retail Sales Data Analysis =======

import pandas as pd

df=pd.read_csv("retail sales.csv")
print(df)

# ==== PART 1 – Understand the dataset ====

# print("First 10 Records",df.head(10))
# print("Last 5 Recorde",df.tail(5))
# print("Number of rows:",df.shape[0])
# print("Number of columns:",df.shape[1])
# print("Display column name:",df.columns)
# print("Data Types:",df.dtypes)
# print(df.isnull())
# print("Total sales:",df['Sales'].sum())
# print("Total Profit:",df['Profit'].sum())
# print("Average sales:",df['Sales'].mean())
# print("Highest sales:",df['Sales'].max())
# print("Lowest sales:",df["Sales"].min())

df['Date']=pd.to_datetime(df['Order Date'],format='%d-%m-%Y')
df['Month_Name']=df['Date'].dt.month_name()

# print(df['Month_Name'])

# ==== Part 2 – Matplotlib practical tasks ==== 

import matplotlib.pyplot as plt

#==== Task 1 Line Plot – Monthly Sales Trend ====

# Monthly_sales=df.groupby('Month_Name')['Sales'].sum()
# print(Monthly_sales)

# plt.plot(Monthly_sales.index,Monthly_sales.values,marker='o')
# plt.title('Monthly Sales Analysis')
# plt.xlabel('Month_Name')
# plt.ylabel('Total sales')
# plt.grid(True)
# plt.show()

# highest_month=Monthly_sales.idxmax()
# highest_sales=Monthly_sales.max()
# print("Highest  month:",highest_month)
# print("Total Sales:",highest_sales)

# ==== Task 2: Scatter Plot – Sales vs Profit ====

# plt.scatter(df['Sales'],df['Profit'],s=100,marker='o')
# plt.title('Sales VS Profit')
# plt.xlabel('Sales')
# plt.ylabel('Profit')
# plt.show()

# Yes. The scatter trend showing upper trend.
# NO. Higher sales do not always mean higher profit because expenses, discounts, and operating costs can reduce profit.

# ==== Task 3: Bar Chart – Region-wise Sales ====

# region_sales=df.groupby('Region')['Sales'].sum()
# print(region_sales)

# plt.bar(region_sales.index,region_sales.values)
# plt.title('Total sales by region')
# plt.xlabel('Region')
# plt.ylabel('Total sales')
# plt.show()

# plt.barh(region_sales.index,region_sales.values)
# plt.title('Total sales by region')
# plt.xlabel('Total Sales')
# plt.ylabel('Region')
# plt.show()

# ==== Task 4: Pie Chart – Product Sales Contribution ====

# product_sale=df.groupby('Product')['Sales'].sum()
# print(product_sale) 

# explode=[0]*len(product_sale)
# explode[product_sale.values.argmax()]=0.1
# plt.pie(product_sale.values,labels=product_sale.index,autopct='%1.1f%%',explode=explode,startangle=90)
# plt.title('Product Sales Contibution')
# plt.show()

# ==== Task 5: Histogram – Customer Age Distribution ====

# plt.hist(df['Customer Age'],bins=5)
# plt.title("Customer Age Distribution")
# plt.xlabel=('Customer Age')
# plt.ylabel=('Number of customer')
# plt.show()

# plt.hist(df['Customer Age'],bins=10)
# plt.title("Customer Age Distribution")
# plt.xlabel=('Customer Age')
# plt.ylabel=('Number of customer')
# plt.show()

# ==== Task 6: Box Plot – Profit Distribution ====

# plt.boxplot(df['Profit'])
# plt.title("Profit Distribution")
# plt.ylabel('Profit')
# plt.show()

# ==== Part 3 – Additional analytical challenges ====

# Task 1: Compare Total Sales and Profit by Region

# region_data=df.groupby('Region')[['Sales','Profit']].sum()
# print(region_data)

# region_data.plot(kind='bar')
# plt.title('Sales and Profit by Region')
# plt.xlabel('Region')
# plt.ylabel('Amount')
# plt.show()

# Task 2: Find the Most Profitable Product

# profit_product=df.groupby('Product')['Profit'].sum()
# print(profit_product)
# print("Most Profitable Product:",profit_product.idxmax())
# print("Highest Profit:",profit_product.max())

# Task 3: Compare Electronics and Accessories Sales Using a Bar Chart

# data=df[df['Category'].isin(['Electronics','Accessories'])]
# category_sales = df.groupby('Category')['Sales'].sum()

# data.plot(kind='bar')

# plt.title('Electronics vs Accessories Sales')
# plt.xlabel('Category')
# plt.ylabel('Total Sales')
# plt.show()

# Task 4: Create a Histogram for Customer Ratings

# plt.hist(df['Customer Rating'],bins=10)
# plt.title('Customer Rating Distribution')
# plt.xlabel('Customer Rating')
# plt.ylabel('Frequency')
# plt.show()

# Task 5: Compare Profit Distribution Across Different Regions Using Box Plots

# df.boxplot(column='Profit',by='Region')
# plt.title('Profit Distribution by Region')
# plt.xlabel('Region')
# plt.ylabel('Profit')
# plt.show()

# Task 6: Find the Relationship Between Quantity and Profit Using a Scatter Plot

# plt.scatter(df['Quantity'],df['Profit'])
# plt.title('Relationship between Quantity and Profit')
# plt.xlabel('Quanity')
# plt.ylabel('Profit')
# plt.show()

# Task 7: Create a Pie Chart Showing Category-wise Sales Contribution

# category_sale=df.groupby('Category')['Sales'].sum()
# plt.pie(category_sale,labels=category_sale.index,autopct='%1.1f%%',startangle=90)
# plt.title('Category wise sales Contribution')
# plt.show()

# Task 8: Create a Monthly Sales Chart with Title, Legend, Markers and Grid

# monthly_sales=df.groupby('Month_Name')['Sales'].sum()
# plt.plot(monthly_sales.index,monthly_sales.values,marker='o')
# plt.title('Monthly sales')
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.grid=True
# plt.show()

# ==== Part 4 – Final mini project ====

# Task 1 What is the total revenue? 
# print("Total Revenue:",df['Sales'].sum())

# Task 2 What is the total profit? 
# print("Total Profit:",df['Profit'].sum())

# Task 3 Which region performs best? 

# region_sales=df.groupby('Region')['Sales'].sum()
# print(region_sales)

# plt.bar(region_sales.index,region_sales.values)
# plt.title('Total sales by region')
# plt.xlabel('Region')
# plt.ylabel('Total sales')
# plt.show()

# Task 4 Which product sells the most? 

# product_sale=df.groupby('Product')['Sales'].sum()
# print(product_sale) 

# explode=[0]*len(product_sale)
# explode[product_sale.values.argmax()]=0.1
# plt.pie(product_sale.values,labels=product_sale.index,autopct='%1.1f%%',explode=explode,startangle=90)
# plt.title('Product Sales Contibution')
# plt.show()

# Task 5 Which category contributes the highest revenue? 

# sales_category=df.groupby('Category')['Sales'].sum()
# print(sales_category)
# print("Most Profitable category:",sales_category.idxmax())
# print("Highest Profit:",sales_category.max())

# Task 6 How do monthly sales change? 

# Monthly_sales=df.groupby('Month_Name')['Sales'].sum()
# print(Monthly_sales)

# plt.plot(Monthly_sales.index,Monthly_sales.values,marker='o')
# plt.title('Monthly Sales Analysis')
# plt.xlabel('Month_Name')
# plt.ylabel('Total sales')
# plt.grid(True)
# plt.show()

# highest_month=Monthly_sales.idxmax()
# highest_sales=Monthly_sales.max()
# print("Highest  month:",highest_month)
# print("Total Sales:",highest_sales)

# Task 7 Is there a relationship between sales and profit? 

# plt.scatter(df['Sales'],df['Profit'],s=100,marker='o')
# plt.title('Sales VS Profit')
# plt.xlabel('Sales')
# plt.ylabel('Profit')
# plt.show()

# Task 8 Are there any unusual profit values? 

# plt.boxplot(df['Profit'])
# plt.title("Profit Distribution")
# plt.ylabel('Profit')
# plt.show()

# Task 9 What is the customer age distribution? 

# plt.hist(df['Customer Age'],bins=5)
# plt.title("Customer Age Distribution")
# plt.xlabel=('Customer Age')
# plt.ylabel=('Number of customer')
# plt.show()



import seaborn as sns

# ==== Part 1 Count plot ====

# ---- Q1. Regional Order Analysis ----

# sns.countplot(x=df['Region'])
# plt.title('Regional Order Analysis')
# plt.show()

# ---- Q2. Product Category Distribution ----

# sns.countplot(x=df['Category'])
# plt.title('Product Category Distribution')
# plt.show()

# ==== Part 2 – Bar Plot ====

# ---- Q3. Regional Sales Performance ----

# sns.barplot(x=df['Region'],y=df['Sales'])
# plt.title('Regional Sales Performance')
# plt.show()

# ---- Q4. Product Profitability Analysis ----

# sns.barplot(x=df['Profit'],y=df['Product'])
# plt.title('Product Profitability Analysis')
# plt.show()

# ==== Part 3 – Line Plot ====

# ---- Q5. Monthly Revenue Analysis ----

# sns.lineplot(x=df['Sales'],y=df['Month_Name'])
# plt.title('Monthly Revenue Analysis')
# plt.show()

# ---- Q6. Monthly Profit Analysis ----

# sns.lineplot(x=df['Month_Name'],y=df['Profit'])
# plt.title('Monthly Profit Analysis')
# plt.show()

# ==== Part 4 – Correlation and Heatmap ====

# ---- Q7. Business Correlation Analysis ----

# corr = df.corr(numeric_only=True)
# sns.heatmap(corr,annot=True,cmap='coolwarm')
# plt.title('Business Correlation Analysis')
# plt.show()

# ==== Part 5 – Pairplot ====

# ---- Q8. Sales and Profit Relationship Analysis ----

# sns.pairplot(df[['Sales','Profit','Quantity','Unit Price']])
# plt.title('Sales and Profit Relationship Analysis')
# plt.show()

# ==== Part 6 – Hue Parameter ====

# ---- Q9. Regional Category Performance ----

# sns.countplot(x=df['Region'],hue=df['Category'])
# plt.title('Regional Category Analysis')
# plt.xlabel('Region')
# plt.ylabel('Count of product')
# plt.show()

# ---- Q10. Regional Profit Comparison ----

# sns.barplot(x=df['Region'],y=df['Profit'],hue=df['Category'])
# plt.title('Regional profit Comparison')
# plt.xlabel('Region')
# plt.ylabel('Average of profit')
# plt.show()