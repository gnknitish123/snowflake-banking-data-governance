# Banking Data Governance Platform using Snowflake

## Project Overview

The **Banking Data Governance Platform** is a data engineering project built using Snowflake, SQL, Python, and Snowflake Native Streamlit.

The project demonstrates how banking data can be ingested, transformed, organized, secured, and presented through a centralized cloud data warehouse.

It follows the **Medallion Architecture (Bronze, Silver, and Gold)** and implements Slowly Changing Dimensions (SCD Type 1, Type 2, and Type 3), data classification, dynamic data masking, and row-level security.

## Architecture

```text
                 Banking Source Data
                         |
                         v
                  BRONZE LAYER
                    Raw Data
                         |
                         v
                  SILVER LAYER
             Cleaning & Transformations
                         |
             +-----------+-----------+
             |           |           |
           SCD 1       SCD 2       SCD 3
             |           |           |
             +-----------+-----------+
                         |
                         v
                   GOLD LAYER
               Business Analytics
                         |
                         v
              SNOWFLAKE STREAMLIT
                  Dashboard

          DATA GOVERNANCE & SECURITY
          - Classification Tags
          - Dynamic Data Masking
          - Row Access Policies
          - Role-Based Access Control
```

## Technologies Used

- **Cloud Data Warehouse:** Snowflake
- **Programming Language:** Python
- **Query Language:** Snowflake SQL
- **Data Transformation:** Snowflake SQL
- **Architecture:** Medallion Architecture
- **Data Modeling:** SCD Type 1, Type 2, Type 3
- **Data Governance:** Snowflake Tags
- **Data Security:** Dynamic Data Masking Policies
- **Row-Level Security:** Snowflake Row Access Policies
- **Data Visualization:** Snowflake Native Streamlit

## Project Modules

### 1. Bronze Layer – Raw Data

Stores the original banking data.

Tables:
- RAW_CUSTOMERS
- RAW_ACCOUNTS
- RAW_TRANSACTIONS
- RAW_LOANS

### 2. Silver Layer – Data Transformation

Performs data cleaning, transformation, and dimensional modeling.

Tables:
- DIM_CUSTOMER_SCD2
- DIM_ACCOUNT_SCD1
- DIM_LOAN_SCD3
- FACT_TRANSACTIONS

Implemented:
- SCD Type 1 – Overwrites previous values.
- SCD Type 2 – Maintains historical records using surrogate keys, effective dates, and current-record indicators.
- SCD Type 3 – Maintains current and previous values in separate columns.

### 3. Gold Layer – Business Analytics

Contains business-ready analytical tables and views.

Objects:
- CUSTOMER_PORTFOLIO
- BRANCH_PERFORMANCE
- TRANSACTION_ANALYTICS
- LOAN_BOOK_SUMMARY
- V_SUSPICIOUS_ACTIVITY

### 4. Data Governance and Security

Implemented Snowflake governance features to protect sensitive banking information.

**Data Classification Tags**
- RESTRICTED
- CONFIDENTIAL

**Dynamic Data Masking Policies**
- MASK_SSN
- MASK_EMAIL
- MASK_PHONE
- MASK_ACCOUNT_NUMBER
- MASK_AMOUNT

**Row Access Policies**
- BRANCH_ACCESS_POLICY
- TRANSACTION_BRANCH_POLICY

**Role-Based Access Control**

Created separate roles for:
- BANK_COMPLIANCE_ROLE
- BANK_OPERATIONS_ROLE
- BANK_MUMBAI_ROLE
- BANK_DELHI_ROLE
- BANK_BANGALORE_ROLE

Branch-level access is controlled through a role-to-branch mapping table.

### 5. Dashboard

Developed a dashboard using Snowflake Native Streamlit to present business insights.

Dashboard sections:
- Customer Portfolio
- Branch Performance
- Transaction Analytics
- Loan Book Summary
- Suspicious Transaction Analysis

## Key Features

- End-to-end banking data warehouse implementation.
- Medallion Architecture using Bronze, Silver, and Gold layers.
- Historical data tracking using SCD Types 1, 2, and 3.
- Sensitive data classification and protection.
- Dynamic data masking based on user roles.
- Branch-level row access security.
- Business analytics and suspicious transaction reporting.
- Interactive dashboard using Snowflake Native Streamlit.

## Learning Outcomes

Through this project, I gained practical experience in:

- Snowflake database and schema management.
- SQL-based data transformations.
- Dimensional data modeling.
- Slowly Changing Dimensions.
- Snowflake data governance.
- Dynamic data masking.
- Row-level security.
- Role-based access control.
- Snowflake Native Streamlit development.

## How to Run

1. Create the Snowflake database and required schemas.
2. Load the source banking data into the Bronze layer.
3. Execute the Silver layer transformation scripts.
4. Execute the Gold layer analytical queries.
5. Configure governance tags, masking policies, row access policies, and roles.
6. Create and run the Snowflake Native Streamlit dashboard.

Refer to the SQL scripts and application files in this repository for implementation details.

## Disclaimer

This project uses synthetic banking data for educational and demonstration purposes. It does not contain real customer banking information.

## Author

**Nitish Kumar**

GitHub: [Add your GitHub profile URL here]
