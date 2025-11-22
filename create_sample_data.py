"""
Script to create sample Excel files for demonstration.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create sample input data
np.random.seed(42)

# Sample 1: Sales Data
sales_data = {
    'Date': [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(20)],
    'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B'] * 4,
    'Region': ['North', 'South', 'East', 'West', 'North'] * 4,
    'Sales': np.random.randint(100, 1000, 20),
    'Cost': np.random.randint(50, 500, 20),
    'Quantity': np.random.randint(1, 50, 20),
    'Customer': [f'Customer {i}' for i in range(1, 21)]
}

# Add some duplicates and missing values
sales_df = pd.DataFrame(sales_data)
sales_df.loc[5, 'Sales'] = np.nan
sales_df.loc[10, 'Cost'] = np.nan
sales_df = pd.concat([sales_df, sales_df.iloc[[0, 1, 2]]], ignore_index=True)

# Sample 2: Employee Data
employee_data = {
    'Employee ID': [f'EMP{str(i).zfill(3)}' for i in range(1, 16)],
    'First Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'Diana', 'Eve', 'Frank', 
                   'Grace', 'Henry', 'Ivy', 'Jack', 'Kate', 'Leo', 'Mia'],
    'Last Name': ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 
                  'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 
                  'Gonzalez', 'Wilson'],
    'Department': ['Sales', 'IT', 'HR', 'Sales', 'IT', 'HR', 'Sales', 'IT', 'HR', 
                   'Sales', 'IT', 'HR', 'Sales', 'IT', 'HR'],
    'Salary': np.random.randint(40000, 120000, 15),
    'Hire Date': [(datetime.now() - timedelta(days=np.random.randint(365, 3650))).strftime('%Y-%m-%d') 
                  for _ in range(15)],
    'Performance Score': np.random.randint(1, 6, 15)
}

employee_df = pd.DataFrame(employee_data)

# Create Excel file with multiple sheets
with pd.ExcelWriter('sample_data/sample_input.xlsx', engine='openpyxl') as writer:
    sales_df.to_excel(writer, sheet_name='Sales Data', index=False)
    employee_df.to_excel(writer, sheet_name='Employee Data', index=False)

print("✅ Sample input file created: sample_data/sample_input.xlsx")

# Create a sample output file (with some transformations applied)
sales_output = sales_df.copy()
sales_output = sales_output.drop_duplicates()
sales_output = sales_output.dropna()
sales_output['Profit'] = sales_output['Sales'] - sales_output['Cost']
sales_output['Profit Margin %'] = (sales_output['Profit'] / sales_output['Sales'] * 100).round(2)

employee_output = employee_df.copy()
employee_output['Full Name'] = employee_output['First Name'] + ' ' + employee_output['Last Name']
employee_output['Years of Service'] = ((datetime.now() - pd.to_datetime(employee_output['Hire Date'])).dt.days / 365).round(1)

with pd.ExcelWriter('sample_data/sample_output.xlsx', engine='openpyxl') as writer:
    sales_output.to_excel(writer, sheet_name='Sales Data', index=False)
    employee_output.to_excel(writer, sheet_name='Employee Data', index=False)

print("✅ Sample output file created: sample_data/sample_output.xlsx")
print("\n📊 Sample data summary:")
print(f"Sales Data: {len(sales_df)} rows, {len(sales_df.columns)} columns")
print(f"Employee Data: {len(employee_df)} rows, {len(employee_df.columns)} columns")
