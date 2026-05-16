import streamlit as st
import pandas as pd
import sqlite3

st.title("SQL Analysis")

if "data" not in st.session_state:

    st.warning("Please upload dataset from sidebar.")

else:

    df = st.session_state["data"]

    # Database connection
    conn = sqlite3.connect(":memory:")

    # Save dataframe into SQL table
    df.to_sql(
        "sales",
        conn,
        index=False,
        if_exists="replace"
    )

    st.subheader("SQL Based Business Insights")

    # ---------------- QUERY 1 ---------------- #

    st.markdown("## Top 5 Products By Sales")

    query1 = """
    SELECT 
        "Product Name",
        ROUND(SUM(Sales),2) as TotalSales
    FROM sales
    GROUP BY "Product Name"
    ORDER BY TotalSales DESC
    LIMIT 5
    """

    result1 = pd.read_sql_query(query1, conn)

    st.dataframe(result1)

    # ---------------- QUERY 2 ---------------- #

    st.markdown("## Sales By Region")

    query2 = """
    SELECT 
        Region,
        ROUND(SUM(Sales),2) as Revenue
    FROM sales
    GROUP BY Region
    ORDER BY Revenue DESC
    """

    result2 = pd.read_sql_query(query2, conn)

    st.dataframe(result2)

    # ---------------- QUERY 3 ---------------- #

    st.markdown("## Profit By Category")

    query3 = """
    SELECT 
        Category,
        ROUND(SUM(Profit),2) as TotalProfit
    FROM sales
    GROUP BY Category
    ORDER BY TotalProfit DESC
    """

    result3 = pd.read_sql_query(query3, conn)

    st.dataframe(result3)

    # ---------------- QUERY 4 ---------------- #

    st.markdown("## Top 10 Customers")

    query4 = """
    SELECT 
        "Customer Name",
        ROUND(SUM(Sales),2) as TotalPurchase
    FROM sales
    GROUP BY "Customer Name"
    ORDER BY TotalPurchase DESC
    LIMIT 10
    """

    result4 = pd.read_sql_query(query4, conn)

    st.dataframe(result4)

    # ---------------- QUERY 5 ---------------- #

    st.markdown("## Average Sales Per Category")

    query5 = """
    SELECT 
        Category,
        ROUND(AVG(Sales),2) as AverageSales
    FROM sales
    GROUP BY Category
    ORDER BY AverageSales DESC
    """

    result5 = pd.read_sql_query(query5, conn)

    st.dataframe(result5)

    # ---------------- QUERY 6 ---------------- #

    st.markdown("## Highest Selling Sub-Categories")

    query6 = """
    SELECT 
        "Sub-Category",
        ROUND(SUM(Sales),2) as Sales
    FROM sales
    GROUP BY "Sub-Category"
    ORDER BY Sales DESC
    LIMIT 10
    """

    result6 = pd.read_sql_query(query6, conn)

    st.dataframe(result6)