import pandas as pd
import numpy as np

# Custom Titanic-like dataset with new values
data = {
    'PassengerId': [101, 102, 103, 104, 105, 106, 107, 108],
    'Survived': [1, 0, 1, 0, 1, 0, 1, 0],
    'Pclass': [1, 3, 2, 1, 3, 2, 1, 3],
    'Name': [
        "Ahmed, Mrs. Fatima",
        "shah, Mr. Ali",
        "qaim, Miss. Noor",
        "hamza, ahmed",
        "ali, Mr. Bilal",
        "jahaz, Miss. Sara",
        "peterthegreat, Mr. Robert",
        "notty, Miss. Ayesha"
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