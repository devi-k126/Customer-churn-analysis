# Customer churn analysis
Customer Churn Analysis using Python
1. Introduction

Customer churn refers to the situation where customers stop doing business with a company. Understanding why customers leave is very important for improving customer retention and business growth.

In this project, we analyze a telecom dataset to identify patterns and factors that influence customer churn using data analysis techniques.

2. Dataset Description

The dataset contains customer-related information such as:

Customer ID
Gender, Age, Marital Status
Tenure (how long the customer stayed)
Contract type
Monthly charges and total charges
Internet services and additional features
Customer Status (Stayed, Churned, Joined)

The dataset helps in understanding customer behavior and identifying churn patterns.

3. Methodology

The project was completed in the following steps:

Data Collection
Imported dataset using Pandas
Data Cleaning
Handled missing values
Filled categorical values with "No Service"
Filled numerical values with 0
Removed unnecessary columns
Data Exploration
Checked dataset structure using .info() and .describe()
Identified missing values using .isnull().sum()
Data Analysis
Used grouping and aggregation
Compared churn across different features
Visualization
Created graphs using Seaborn and Matplotlib

4. Analysis

The following analyses were performed:

Customer churn distribution
Churn based on contract type
Churn vs monthly charges
Churn vs tenure

Using groupby operations and visualizations, relationships between variables were identified.

5. Results

The analysis revealed clear differences between churned and retained customers:

Higher churn observed in certain contract types
Customers with higher monthly charges tend to leave
Customers with shorter tenure show higher churn

6. Insights
Customers with month-to-month contracts churn more
Customers with higher monthly charges are more likely to leave
Customers with low tenure (new customers) churn more
Customers with long-term contracts are more loyal

7. Tools and Technologies
Python
Pandas
Seaborn
Matplotlib
Visual Studio Code
GitHub

8. Project Structure
churn_project/
 churn.csv
 analysis.py
 README.md

9. Conclusion

This project successfully analyzed customer churn data and identified key factors influencing customer behavior. The findings can help businesses take proactive steps to reduce churn and improve customer retention.

10. Author

Devi K


