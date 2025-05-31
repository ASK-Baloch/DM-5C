# Data-Mining by sir Tajmir
All the Assignments of Datamining By sir Tajmir

## 1. Variable Swap
```python
def swap_variables(a, b):
  """Swaps the values of two variables without using a third variable.
  """
  print(f"Initial values: a = {a}, b = {b}")  # Print initial values

  a = a + b  # Add b to a
  b = a - b  # Subtract b from a (original a is now a+b, so this gives original a)
  a = a - b  # Subtract new b (original a) from a (a+b) to get original b

  print(f"Swapped values: a = {a}, b = {b}")  # Print swapped values
  return a, b


# Example usage:
x = 10
y = 5
x, y = swap_variables(x, y)  # Call the function and unpack the returned tuple

## 2.  Custom Titanic-like Dataset
This assignment focuses on data preprocessing techniques using a custom-generated dataset that mimics the structure of the well-known Titanic passenger data. The steps include:

Handling Missing Values: Filling in NaN entries for 'Embarked', 'Age', and 'Cabin' columns to ensure data completeness.
Binning Numerical Data: Categorizing 'Age' into descriptive groups like 'Child', 'Teen', 'Adult', etc., which can be useful for analysis.
Feature Engineering: Extracting 'Surname' from the 'Name' column to potentially identify family groups.

``` 
python 

import pandas as pd
import numpy as np

# Custom Titanic-like dataset with new values
data = {
    'PassengerId': [101, 102, 103, 104, 105, 106, 107, 108],
    'Survived': [1, 0, 1, 0, 1, 0, 1, 0],
    'Pclass': [1, 3, 2, 1, 3, 2, 1, 3],
    'Name': [
        "Davis, Ms. Sarah",
        "Miller, Mr. Thomas",
        "Wilson, Dr. Emma",
        "Moore, Mrs. Linda",
        "Taylor, Master. George",
        "Anderson, Miss. Sophia",
        "Thomas, Mr. Robert",
        "Jackson, Mrs. Mary"
    ],
    'Sex': ['female', 'male', 'female', 'female', 'male', 'female', 'male', 'female'],
    'Age': [28, np.nan, 55, 30, 8, 22, 65, np.nan],
    'SibSp': [0, 2, 1, 0, 1, 0, 0, 1],
    'Parch': [1, 0, 0, 2, 1, 0, 0, 0],
    'Ticket': ['A101', 'B202', 'C303', 'D404', 'E505', 'F606', 'G707', 'H808'],
    'Fare': [75.50, 12.75, 90.00, 150.00, 25.00, 30.50, 110.00, 9.99],
    'Cabin': ["C50", np.nan, "A10", np.nan, "G10", np.nan, "B80", "Unknown"],
    'Embarked': ['S', 'C', 'Q', 'S', 'C', np.nan, 'S', 'Q']
}

df = pd.DataFrame(data)

# Check for missing values before processing
print("Initial Missing Values:\n", df.isnull().sum(), "\n")

# Step 1: Fill missing values
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Cabin'].fillna("Not Assigned", inplace=True)

# Step 2: Binning Age
def categorize_age(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 35:
        return "Adult"
    elif age <= 60:
        return "Middle-Aged"
    else:
        return "Senior"

df['AgeCategory'] = df['Age'].apply(categorize_age)

# Step 3: Integrate family names
df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])

# Final cleaned data
print("Missing Values After Cleaning:\n", df.isnull().sum(), "\n")
print("Processed Data Sample:\n", df[['PassengerId', 'Survived', 'Age', 'AgeCategory', 'Embarked', 'Cabin', 'Surname']])

