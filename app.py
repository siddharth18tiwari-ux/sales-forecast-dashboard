import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Forecast Dashboard",
    layout="wide"
)

# ---------------- UI ---------------- #

st.markdown("""
<style>

.stApp{
    background-color:#0a0a0a;
    color:white;
}

section[data-testid="stSidebar"]{
    background-color:#111111;
}

h1,h2,h3,h4,h5,p{
    color:white;
}

div[data-testid="metric-container"]{
    background-color:#151515;
    border:1px solid #222;
    padding:15px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.title("Sales Forecasting & Business Insights Dashboard")

st.write("Upload dataset once and analyze everything.")
  
st.markdown("""
<div style="margin-top:30px;
padding:25px;
background:#111111;
border-radius:20px;
border:1px solid #222;">

<h1 style="font-size:55px;
color:white;
margin-bottom:10px;">
Siddharth Analytics
</h1>

<p style="font-size:20px;
color:#aaaaaa;">
 Sales Forecasting & Business Intelligence Dashboard
</p>

<hr style="border:1px solid #222; margin-top:25px; margin-bottom:25px;">

<div style="display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;">

<div>

<h3 style="color:white;">
Made By Siddharth Tiwari
</h3>

<p style="color:#999999;">
Python • SQL • Streamlit • Data Analytics
</p>

</div>

<div>

<h3 style="color:white;">
Contact Us
</h3>

<p style="color:#ff4b4b;">
siddharth57tiwari@gmail.com
</p>

</div>

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# ---------------- SAVE DATA ---------------- #

if uploaded_file:

    df = pd.read_csv(
        uploaded_file,
        encoding='latin1'
    )

    st.session_state["data"] = df

    st.success("Dataset Uploaded Successfully")