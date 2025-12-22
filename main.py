import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Load the data you just created
df = pd.read_csv('salary_data.csv')
X = df[['YearsExperience']] 
y = df['Salary']            

# 2. Train the AI Model
model = LinearRegression()
model.fit(X, y)

# 3. Get User Input
print("--- AI Salary Predictor ---")
name = input("Enter Employee Name: ")
exp = float(input("Enter Years of Experience: "))

# 4. Predict
predicted_salary = model.predict([[exp]])[0]

# 5. Print the Salary Slip
print("\n" + "="*40)
print(f"{'OFFICIAL SALARY SLIP':^40}")
print("="*40)
print(f"Employee Name:    {name}")
print(f"Experience:       {exp} Years")
print("-" * 40)
print(f"PREDICTED GROSS:  ${predicted_salary:,.2f}")
print(f"Estimated Tax:    ${(predicted_salary * 0.12):,.2f}")
print("-" * 40)
print(f"NET TAKE-HOME:    ${(predicted_salary * 0.88):,.2f}")
print("="*40)