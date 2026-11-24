
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Banking Data Governance Platform",
    page_icon="🏦",
    layout="wide"
)

# Get active Snowflake session
session = get_active_session()

DATABASE = "BANKING_GOV"
SCHEMA = "GOLD"

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏦 Banking Data Governance Platform")

st.markdown(
    "Customer Portfolio | Branch Performance | "
    "Transaction Analytics | Loan Summary"
)

st.divider()

# --------------------------------------------------
# FUNCTION TO FETCH DATA FROM SNOWFLAKE
# --------------------------------------------------

def fetch_data(query):
    return session.sql(query).to_pandas()


# --------------------------------------------------
# LOAD GOLD LAYER DATA
# --------------------------------------------------

customer_df = fetch_data("""
    SELECT *
    FROM BANKING_GOV.GOLD.CUSTOMER_PORTFOLIO
""")

branch_df = fetch_data("""
    SELECT *
    FROM BANKING_GOV.GOLD.BRANCH_PERFORMANCE
""")

transaction_df = fetch_data("""
    SELECT *
    FROM BANKING_GOV.GOLD.TRANSACTION_ANALYTICS
""")

loan_df = fetch_data("""
    SELECT *
    FROM BANKING_GOV.GOLD.LOAN_BOOK_SUMMARY
""")

suspicious_df = fetch_data("""
    SELECT *
    FROM BANKING_GOV.GOLD.V_SUSPICIOUS_ACTIVITY
""")

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

total_customers = len(customer_df)

total_accounts = int(
    customer_df["TOTAL_ACCOUNTS"].sum()
)

total_balance = customer_df["TOTAL_BALANCE"].sum()

total_transactions = int(
    transaction_df["TOTAL_TRANSACTIONS"].sum()
)

total_loans = int(
    loan_df["TOTAL_LOANS"].sum()
)

flagged_transactions = int(
    transaction_df["FLAGGED_COUNT"].sum()
)

# --------------------------------------------------
# DISPLAY KPI CARDS
# --------------------------------------------------

st.subheader("📊 Banking Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", total_customers)
col2.metric("Total Accounts", total_accounts)

col3.metric(
    "Total Customer Balance",
    f"₹{total_balance:,.2f}"
)

col4, col5, col6 = st.columns(3)

col4.metric("Total Transactions", total_transactions)
col5.metric("Total Loans", total_loans)
col6.metric("Flagged Transactions", flagged_transactions)

st.divider()

# --------------------------------------------------
# CUSTOMER PORTFOLIO
# --------------------------------------------------

st.subheader("👥 Customer Portfolio")

st.dataframe(
    customer_df,
    use_container_width=True
)

# --------------------------------------------------
# BRANCH PERFORMANCE
# --------------------------------------------------

st.subheader("🏢 Branch Performance")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Deposits by Branch**")

    st.bar_chart(
        branch_df.set_index("BRANCH_CODE")[
            ["TOTAL_DEPOSITS"]
        ]
    )

with col2:
    st.markdown("**Customers by Branch**")

    st.bar_chart(
        branch_df.set_index("BRANCH_CODE")[
            ["TOTAL_CUSTOMERS"]
        ]
    )

st.dataframe(
    branch_df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# TRANSACTION ANALYTICS
# --------------------------------------------------

st.subheader("💳 Transaction Analytics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Transactions by Type**")

    transaction_type_df = (
        transaction_df.groupby("TRANSACTION_TYPE")[
            "TOTAL_TRANSACTIONS"
        ].sum()
    )

    st.bar_chart(transaction_type_df)

with col2:
    st.markdown("**Transaction Amount by Channel**")

    channel_df = (
        transaction_df.groupby("CHANNEL")[
            "TOTAL_AMOUNT"
        ].sum()
    )

    st.bar_chart(channel_df)

st.dataframe(
    transaction_df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# LOAN BOOK SUMMARY
# --------------------------------------------------

st.subheader("🏠 Loan Book Summary")

st.metric(
    "Total Loan Principal",
    f"₹{loan_df['TOTAL_PRINCIPAL'].sum():,.2f}"
)

st.bar_chart(
    loan_df.groupby("LOAN_TYPE")[
        "TOTAL_PRINCIPAL"
    ].sum()
)

st.dataframe(
    loan_df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# SUSPICIOUS TRANSACTION ANALYSIS
# --------------------------------------------------

st.subheader("🚨 Suspicious Transaction Analysis")

st.metric(
    "Suspicious Transactions",
    len(suspicious_df)
)

if not suspicious_df.empty:

    st.warning(
        "Suspicious transactions detected. "
        "Review the following records."
    )

    st.dataframe(
        suspicious_df,
        use_container_width=True
    )

else:
    st.success("No suspicious transactions found.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Banking Data Governance Platform | "
    "Powered by Snowflake and Streamlit"
)
