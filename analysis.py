# Import libraries for data analysis and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the dataset
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Drop unnecessary columns and handle missing values
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True)

# Set Seaborn style for all plots
sb.set(style="whitegrid")

# Custom color palette for varied coloring
palette = sb.color_palette("viridis", as_cmap=True)

# 1. Gender Distribution Count Plot
plt.figure(figsize=(8, 6))
ax = sb.countplot(x='Gender', data=df, palette='Set2')
ax.set_title("Gender Distribution")
for container in ax.containers:
    ax.bar_label(container)
plt.show()

# 2. Sales by Gender Bar Plot
plt.figure(figsize=(8, 6))
sales_gen = df.groupby('Gender', as_index=False)['Amount'].sum()
sb.barplot(x='Gender', y='Amount', data=sales_gen, palette='Set3')
plt.title("Total Sales by Gender")
plt.show()

# 3. Age Distribution by Gender Count Plot with Rotated Labels
plt.figure(figsize=(70, 186))
ax = sb.countplot(data=df, x='Age', hue='Gender', palette='Spectral')
ax.set_title("Age Distribution by Gender")
ax.tick_params(axis='x', rotation=45)
plt.show()

# 4. Sales by Age Group Bar Plot with Pie Chart
plt.figure(figsize=(8, 6))
sales_age = df.groupby('Age Group', as_index=False)['Amount'].sum()
sb.barplot(x='Age Group', y='Amount', data=sales_age, palette='coolwarm')
plt.title("Total Sales by Age Group")
plt.xticks(rotation=45)
plt.show()

# Pie Chart for Age Group Sales
plt.figure(figsize=(8, 8))
colors = sb.color_palette("coolwarm", len(sales_age))
plt.pie(sales_age['Amount'], labels=sales_age['Age Group'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Sales Distribution by Age Group")
plt.show()

# 5. Top 10 States by Orders with Rotated Labels
plt.figure(figsize=(12, 6))
sales_state_orders = df.groupby('State', as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sb.barplot(data=sales_state_orders, x='State', y='Orders', palette='icefire')
plt.title("Top 10 States by Orders")
plt.xticks(rotation=45)
plt.show()

# 6. Top 10 States by Sales Amount with Rotated Labels
plt.figure(figsize=(12, 6))
sales_state_amount = df.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sb.barplot(data=sales_state_amount, x='State', y='Amount', palette='magma')
plt.title("Top 10 States by Sales Amount")
plt.xticks(rotation=45)
plt.show()

# 7. Marital Status Distribution Count Plot
plt.figure(figsize=(8, 6))
ax = sb.countplot(data=df, x='Marital_Status', palette='viridis')
plt.title("Marital Status Distribution")
for container in ax.containers:
    ax.bar_label(container)
plt.show()

# 8. Sales by Marital Status and Gender Bar Plot
plt.figure(figsize=(8, 6))
sales_marital_gender = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum()
sb.barplot(data=sales_marital_gender, x='Marital_Status', y='Amount', hue='Gender', palette='husl')
plt.title("Sales by Marital Status and Gender")
plt.show()

# 9. Occupation Distribution Count Plot with Rotated Labels
plt.figure(figsize=(12, 6))
ax = sb.countplot(data=df, x='Occupation', palette='tab20')
plt.title("Occupation Distribution")
plt.xticks(rotation=45)
for container in ax.containers:
    ax.bar_label(container)
plt.show()

# 10. Top 10 Product Categories by Sales Amount with Pie Chart
plt.figure(figsize=(12, 6))
sales_product_category = df.groupby('Product_Category', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sb.barplot(data=sales_product_category, x='Product_Category', y='Amount', palette='cubehelix')
plt.title("Top 10 Product Categories by Sales Amount")
plt.xticks(rotation=45)
plt.show()

# Pie Chart for Product Category Sales
plt.figure(figsize=(8, 8))
colors = sb.color_palette("cubehelix", len(sales_product_category))
plt.pie(sales_product_category['Amount'], labels=sales_product_category['Product_Category'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Sales Distribution by Top Product Categories")
plt.show()
