📊 E-Commerce Analytics: Customer Cohort Retention & Data Integrity
Data Analyst Portfolio Project | Dataset: Olist Brazilian E-Commerce

🎯 Project Overview
This project focuses on analyzing customer behavior and business health for a large-scale Brazilian marketplace. Leveraging SQL (BigQuery) for heavy data lifting and Python for advanced visualization, I transformed raw transactional data into actionable business insights.

The core of the project is a Cohort Analysis designed to measure customer loyalty and retention patterns over a 12-month lifecycle.

🛠️ Tech Stack & Skills
Cloud Data Warehouse: Google BigQuery

Languages: SQL (Standard SQL), Python 3.9

Python Libraries: Pandas, Seaborn, Matplotlib

SQL Techniques: CTEs (Common Table Expressions), Window Functions (FIRST_VALUE, OVER), Date Transformations, and Joins.

IDE: PyCharm

📈 Key Analysis: Monthly Cohort Retention
I developed a robust SQL pipeline to group customers into cohorts based on their first purchase month. The analysis tracks how many unique customers return to the platform in subsequent months.

🔍 Business Insights
Low Retention Floor: The heatmap reveals a retention rate below 5% starting from Month 1, indicating a "One-Time Buyer" dominant model.

Acquisition vs. Retention: The data suggests that while the platform is excellent at acquiring new users, there is a significant opportunity to implement CRM strategies to reduce churn.

🛡️ Data Quality & Engineering Approach
With 5 years of experience in data, I know that insights are only as good as the underlying data. This repository includes scripts to identify:

Logical Anomalies: Orders delivered before the approval date.

Missing Values: Handling nulls in review comments and delivery timestamps.

Data Consistency: Ensuring customer_unique_id is used instead of session-based IDs for accurate tracking.

📂 Repository Structure
sql_queries/: Advanced SQL scripts for retention and data cleaning.

python_scripts/: Python code for data visualization (Heatmaps).

requirements.txt: Project dependencies for easy environment setup.

results/: Exported visualizations and summary reports.

🚀 How to use this project
Clone the repository.

Install dependencies: pip install -r requirements.txt.

Run visualize_retention.py to generate the heatmap from the provided sample data.