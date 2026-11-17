# ======= Mini Project: Customer Churn Analysis Using Pandas =======

# import pandas as pd

# ==== 1.Import Pandas and load dataset ====

# df=pd.read_csv("Customer churn prediction.csv")
# print(df)

# ==== 2.Display dataset ====

# print(df.head(5))
# print(df.tail(5))

# ==== 3.Dataset Informations ====

# print("Rows and Columns:",df.shape)
# print("Column Name:",df.columns)
# print("Data Types:",df.dtypes)
# df.info()

# ==== 4.Check missing values and duplicates ====

# print(df.isnull().sum())
# print("Duplicate records:",df.duplicated().sum())

# ==== 5.Data Cleaning ====

# df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
# df['TotalCharges']=df['TotalCharges'].fillna(df['TotalCharges'].median())
# print(df.isnull().sum())

# ==== 6.Descriptive statistics ====

# print(df.describe())
# print("Mean:",df['MonthlyCharges'].mean())
# print("Median:",df['MonthlyCharges'].median())
# print("Mode:",df['MonthlyCharges'].mode())
# print("Maximum:",df['MonthlyCharges'].max())
# print("Minimum:",df['MonthlyCharges'].min())
# print("Standard Deviation:",df['MonthlyCharges'].std())
# print("Variance:",df['MonthlyCharges'].var())
# print("Total:",df['MonthlyCharges'].sum())
# print("Count:",df['MonthlyCharges'].count())
# print("Q1:",df['MonthlyCharges'].quantile(0.25))
# print("Q3:",df['MonthlyCharges'].quantile(0.75))

# ==== 7.Customer churn count ====

# print(df['Churn'].value_counts())

# ==== 8.Sorting Operations ====

# print(df.sort_values(by='MonthlyCharges',ascending=False))
# print(df.sort_values(by='MonthlyCharges',ascending=True))

# ==== 9.Ranking ====

# df['Charges_Rank'] = df['MonthlyCharges'].rank(ascending=False)
# print(df[['MonthlyCharges', 'Charges_Rank']])
# print(df.nlargest(10, 'MonthlyCharges'))
# print(df.nsmallest(10, 'MonthlyCharges'))

# ==== 10.GroupBy operations ====

# print("Customer count by gender:",df.groupby('gender')['customerID'].count())
# print("Customer count by contract:",df.groupby('Contract')['customerID'].count())
# print("Churn count by contract:",df.groupby('Contract')['Churn'].value_counts())
# print("Average monthly charges by contract:",df.groupby('Contract')['MonthlyCharges'].mean())
# print("Average tenure by churn status:",df.groupby('Churn')['tenure'].mean())
# print("Total monthly charges by internet service:",df.groupby('InternetService')['MonthlyCharges'].sum())

# ==== 11. Correlation analysis ====

# df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
# correlation = df.corr(numeric_only=True)
# print(df["MonthlyCharges"].corr(df["TotalCharges"]))
# print(correlation)




