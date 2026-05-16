import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression

st.title("Sales Forecasting")

if "data" not in st.session_state:

    st.warning("Please upload dataset from sidebar.")

else:

    df = st.session_state["data"]

    # ---------------- DATA PREPARATION ---------------- #

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    sales_data = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    sales_data = sales_data.sort_values("Order Date")

    # ---------------- LAST MONTH SALES ---------------- #

    st.subheader("Last Month Sales Performance")

    latest_date = sales_data["Order Date"].max()

    last_month_data = sales_data[
        sales_data["Order Date"] >= latest_date - pd.DateOffset(days=30)
    ]

    # ---------------- RED THEME CHART ---------------- #

    fig1, ax1 = plt.subplots(figsize=(12,5))

    ax1.plot(
        last_month_data["Order Date"],
        last_month_data["Sales"],
        color="#ff4b4b",
        linewidth=3
    )

    ax1.set_facecolor("#111111")

    fig1.patch.set_facecolor("#0a0a0a")

    ax1.tick_params(colors="white")

    ax1.spines['bottom'].set_color('white')
    ax1.spines['left'].set_color('white')

    ax1.set_title(
        "Last 30 Days Sales Trend",
        color="white",
        fontsize=18
    )

    ax1.set_xlabel("Date", color="white")

    ax1.set_ylabel("Sales", color="white")

    st.pyplot(fig1)

    # ---------------- FORECASTING ---------------- #

    st.subheader("Future Sales Forecast")

    sales_data["Days"] = np.arange(len(sales_data))

    X = sales_data[["Days"]]

    y = sales_data["Sales"]

    model = LinearRegression()

    model.fit(X, y)

    # ---------------- FUTURE DATES ---------------- #

    future_days = np.arange(
        len(sales_data),
        len(sales_data) + 180
    ).reshape(-1, 1)

    predictions = model.predict(future_days)

    future_dates = pd.date_range(
        start=sales_data["Order Date"].max(),
        periods=180
    )

    # ---------------- FORECAST GRAPH ---------------- #

    fig2, ax2 = plt.subplots(figsize=(14,6))

    ax2.plot(
        sales_data["Order Date"],
        sales_data["Sales"],
        label="Historical Sales",
        color="white",
        linewidth=2
    )

    ax2.plot(
        future_dates,
        predictions,
        label="Forecasted Sales",
        color="#ff4b4b",
        linewidth=3
    )

    ax2.set_facecolor("#111111")

    fig2.patch.set_facecolor("#0a0a0a")

    ax2.tick_params(colors="white")

    ax2.spines['bottom'].set_color('white')
    ax2.spines['left'].set_color('white')

    ax2.set_title(
        "6 Month Sales Forecast",
        color="white",
        fontsize=20
    )

    ax2.set_xlabel("Date", color="white")

    ax2.set_ylabel("Sales", color="white")

    ax2.legend()

    st.pyplot(fig2)

    # ---------------- KPI SECTION ---------------- #

    st.subheader("Forecast Insights")

    expected_growth = (
        predictions[-1] - predictions[0]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Current Avg Sales",
        f"₹ {int(y.mean())}"
    )

    col2.metric(
        "Expected Future Sales",
        f"₹ {int(predictions[-1])}"
    )

    col3.metric(
        "Predicted Growth",
        f"₹ {int(expected_growth)}"
    )

    # ---------------- BUSINESS INSIGHTS ---------------- #

    st.markdown("### AI Style Business Insights")

    if expected_growth > 0:

        st.success(
            "Sales trend indicates expected business growth over the upcoming months."
        )

    else:

        st.error(
            "Sales trend indicates possible decline. Strategic improvements may be needed."
        )

    if predictions[-1] > y.mean():

        st.info(
            "Forecast suggests future sales may outperform historical average performance."
        )

    else:

        st.warning(
            "Forecasted sales are close to current average performance."
        )