import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.data_cleaning import clean_data

st.title("Business Analytics Dashboard")

if "data" not in st.session_state:

    st.warning("Please upload dataset from sidebar.")

else:

    df = st.session_state["data"]

    df = clean_data(df)

    # ---------------- DATE ---------------- #

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # ---------------- KPI SECTION ---------------- #

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Order ID"].nunique()

    total_customers = df["Customer Name"].nunique()

    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Sales",
        f"₹ {total_sales:,.0f}"
    )

    col2.metric(
        "Total Profit",
        f"₹ {total_profit:,.0f}"
    )

    col3.metric(
        "Total Orders",
        total_orders
    )

    col4.metric(
        "Customers",
        total_customers
    )

    st.divider()

    # ---------------- SALES TREND ---------------- #

    st.subheader("Sales Trend Analysis")

    monthly_sales = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    fig1 = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales",
        title="Sales Trend Over Time",
        template="plotly_dark",
        color_discrete_sequence=["red"]
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ---------------- CATEGORY WISE SALES ---------------- #

    colA, colB = st.columns(2)

    with colA:

        category_sales = (
            df.groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            category_sales,
            values="Sales",
            names="Category",
            hole=0.5,
            title="Category Wise Sales",
            template="plotly_dark",
            color_discrete_sequence=[
                "#ff4b4b",
                "#ff7b7b",
                "#ff9999"
            ]
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ---------------- REGION WISE SALES ---------------- #

    with colB:

        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig3 = px.bar(
            region_sales,
            x="Region",
            y="Sales",
            title="Region Wise Revenue",
            template="plotly_dark",
            color="Sales",
            color_continuous_scale="Reds"
        )

        st.plotly_chart(fig3, use_container_width=True)

    # ---------------- PROFIT BY CATEGORY ---------------- #

    st.subheader("Profit Analysis")

    profit_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )

    fig4 = px.bar(
        profit_category,
        x="Category",
        y="Profit",
        title="Profit By Category",
        template="plotly_dark",
        color="Profit",
        color_continuous_scale="reds"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # ---------------- TOP PRODUCTS ---------------- #

    st.subheader("Top Performing Products")

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig5 = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products",
        template="plotly_dark",
        color="Sales",
        color_continuous_scale="Reds"
    )

    st.plotly_chart(fig5, use_container_width=True)

    # ---------------- SUB CATEGORY ---------------- #

    st.subheader("Sub-Category Analysis")

    sub_category = (
        df.groupby("Sub-Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig6 = px.area(
        sub_category,
        x="Sub-Category",
        y="Sales",
        title="Sub Category Sales",
        template="plotly_dark",
        color_discrete_sequence=["#ff4b4b"]
    )

    st.plotly_chart(fig6, use_container_width=True)

    # ---------------- DISCOUNT ANALYSIS ---------------- #

    if "Discount" in df.columns:

        st.subheader("Discount Impact")

        fig7 = px.scatter(
            df,
            x="Discount",
            y="Profit",
            color="Category",
            title="Discount vs Profit",
            template="plotly_dark"
        )

        st.plotly_chart(fig7, use_container_width=True)

    # ---------------- DATA PREVIEW ---------------- #

    with st.expander("View Dataset"):

        st.dataframe(df.head(20))