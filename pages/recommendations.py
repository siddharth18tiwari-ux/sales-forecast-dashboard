import streamlit as st
import pandas as pd

st.title("Business Recommendations")

if "data" not in st.session_state:

    st.warning("Please upload dataset from sidebar.")

else:

    df = st.session_state["data"]

    # ---------------- TOP PRODUCT ---------------- #

    top_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .idxmax()
    )

    st.success(
        f"Focus more marketing on '{top_product}' because it has the highest sales."
    )

    # ---------------- LOW PRODUCT ---------------- #

    low_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .idxmin()
    )

    st.warning(
        f"'{low_product}' has very low sales. Consider reducing inventory or improving marketing."
    )

    # ---------------- BEST CATEGORY ---------------- #

    best_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .idxmax()
    )

    st.info(
        f"'{best_category}' category is generating the highest profit. Expanding this category may increase revenue."
    )

    # ---------------- LOWEST REGION ---------------- #

    low_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmin()
    )

    st.error(
        f"Sales are lowest in '{low_region}' region. Consider running regional promotions there."
    )

    # ---------------- MOST PROFITABLE SUBCATEGORY ---------------- #

    best_subcategory = (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .idxmax()
    )

    st.success(
        f"'{best_subcategory}' sub-category is highly profitable and should be prioritized."
    )

    # ---------------- SALES TREND ---------------- #

    average_sales = df["Sales"].mean()

    if average_sales > 200:

        st.info(
            "Average sales value is healthy. Business performance is stable."
        )

    else:

        st.warning(
            "Average sales value is relatively low. Focus on increasing customer engagement."
        )

    # ---------------- DISCOUNT IMPACT ---------------- #

    if "Discount" in df.columns:

        avg_discount = df["Discount"].mean()

        if avg_discount > 0.3:

            st.warning(
                "High average discount detected. Excessive discounts may reduce profitability."
            )

        else:

            st.success(
                "Discount strategy looks balanced and sustainable."
            )