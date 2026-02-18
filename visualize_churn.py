import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visualizations directory
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Load dataset
df = pd.read_csv('churn_data.csv')

# Set aesthetic style
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# 1. Churn Distribution (Pie Chart)
churn_counts = df['Churn'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99'])
plt.title('Overall Churn Distribution')
plt.savefig('visualizations/churn_distribution.png')
plt.close()

# 2. Churn by Contract Type
plt.figure(figsize=(10, 6))
sns.countplot(x='Contract', hue='Churn', data=df, palette='viridis')
plt.title('Customer Churn by Contract Type')
plt.xlabel('Contract Type')
plt.ylabel('Count')
plt.savefig('visualizations/churn_by_contract.png')
plt.close()

# 3. Churn by Payment Method
plt.figure(figsize=(12, 6))
sns.countplot(x='PaymentMethod', hue='Churn', data=df, palette='viridis')
plt.title('Customer Churn by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/churn_by_payment_method.png')
plt.close()

# 4. Monthly Charges Distribution
plt.figure(figsize=(10, 6))
sns.kdeplot(df[df['Churn'] == 'Yes']['MonthlyCharges'], color='red', fill=True, label='Churn: Yes')
sns.kdeplot(df[df['Churn'] == 'No']['MonthlyCharges'], color='blue', fill=True, label='Churn: No')
plt.title('Distribution of Monthly Charges by Churn Status')
plt.xlabel('Monthly Charges')
plt.ylabel('Density')
plt.legend()
plt.savefig('visualizations/monthly_charges_distribution.png')
plt.close()

print("Visualizations generated successfully in 'visualizations/' folder.")
