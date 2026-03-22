import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("churn.csv")

print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())

df['Offer'].fillna('Unknown', inplace=True)
df['Internet Type'].fillna('Unknown', inplace=True)


df['Avg Monthly Long Distance Charges'].fillna(0, inplace=True)


df.drop(['Churn Category', 'Churn Reason'], axis=1, inplace=True)
print(df.isnull().sum())
cols = [
    'Multiple Lines',
    'Avg Monthly GB Download',
    'Online Security',
    'Online Backup',
    'Device Protection Plan',
    'Premium Tech Support',
    'Streaming TV',
    'Streaming Movies',
    'Streaming Music',
    'Unlimited Data'
]

for col in cols:
    df[col].fillna('No Service', inplace=True)
    print(df.isnull().sum())
    


categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    df[col].fillna('No Service', inplace=True)


numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    df[col].fillna(0, inplace=True)


print(df.isnull().sum())
print(df['Customer Status'].value_counts())
print(df.groupby('Contract')['Customer Status'].value_counts())
print(df.groupby('Customer Status')['Monthly Charge'].mean())
print(df.groupby('Customer Status')['Tenure in Months'].mean())


plt.figure(figsize=(6,4))
sns.countplot(x='Customer Status', data=df)
plt.title("Customer Status Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Contract', hue='Customer Status', data=df)
plt.title("Contract vs Customer Status")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Customer Status', y='Monthly Charge', data=df)
plt.title("Monthly Charge vs Customer Status")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Customer Status', y='Tenure in Months', data=df)
plt.title("Tenure vs Customer Status")
plt.show()