# APPLE iPhone Sales Interactive Dashboard (Apple-Style UI)
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Apple iPhone Sales Dashboard", layout="wide")

# ---------------------- Custom Apple-like Styling ----------------------
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
        color: white;
    }
    .main {
        background-color: #0f0f0f;
    }
    .block-container {
        padding-top: 1.5rem;
    }
    h1, h2, h3 {
        color: white;
        font-weight: 600;
    }
    .stMetric {
        background-color: #1c1c1e;
        padding: 15px;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Header with White Apple Logo ----------------------
col_logo, col_title = st.columns([1, 6])

with col_logo:
    st.image(
        "D:\ADITI RAJESH NAIR\DATA SCIENCE\APPLE DATA ANALYSIS/apple logo.jpg",
        width=200
    )

with col_title:
    st.title("Apple iPhone Sales Dashboard")
    st.caption("Interactive Data Analysis | Apple Inspired UI")

st.divider()

# ---------------------- Load Data ----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("apple_products.csv")

    # Robust conversion for Discount Percentage
    df["Discount Percentage"] = (
        pd.to_numeric(
            df["Discount Percentage"].astype(str).str.replace("%", ""),
            errors="coerce"
        )
    )

    return df


data = load_data()

# ---------------------- Sidebar Filters ----------------------
st.sidebar.header("Filters")

min_price = int(data["Sale Price"].min())
max_price = int(data["Sale Price"].max())

price_range = st.sidebar.slider(
    "Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

filtered_data = data[(data["Sale Price"] >= price_range[0]) &
                     (data["Sale Price"] <= price_range[1])]

# ---------------------- iPhone Images Section ----------------------
st.subheader("Featured iPhone Models")
img1, img2, img3 = st.columns(3)

with img1:
    st.image(
        r"D:\ADITI RAJESH NAIR\DATA SCIENCE\APPLE DATA ANALYSIS\apple 1.jpg",
        width=250
    )

with img2:
    st.image(
        r"D:\ADITI RAJESH NAIR\DATA SCIENCE\APPLE DATA ANALYSIS\apple 2.jpg",
        width=250
    )

with img3:
    st.image(
        r"D:\ADITI RAJESH NAIR\DATA SCIENCE\APPLE DATA ANALYSIS\apple 3.jpg",
        width=250
    )

st.divider()

# ---------------------- KPI Metrics ----------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Products", len(filtered_data))
col2.metric("Average Sale Price", f"₹{int(filtered_data['Sale Price'].mean())}")
col3.metric("Average Rating", round(filtered_data['Star Rating'].mean(), 2))

st.divider()

# ---------------------- Bar Chart ----------------------
st.subheader("Top 10 Highest Rated iPhones vs Number of Ratings")

highest_rated = filtered_data.sort_values(by="Star Rating", ascending=False).head(10)

bar_fig = px.bar(
    highest_rated,
    x="Product Name",
    y="Number Of Ratings",
    color="Star Rating",
    text="Number Of Ratings"
)

bar_fig.update_layout(
    xaxis_tickangle=-45,
    yaxis=dict(tickmode='linear', dtick=500, tickformat=","),
    plot_bgcolor="#0f0f0f",
    paper_bgcolor="#0f0f0f",
    font_color="white"
)

st.plotly_chart(bar_fig, use_container_width=True)

# ---------------------- Scatter Plot ----------------------
st.subheader("Relationship between Sale Price and Number of Ratings")

scatter_fig = px.scatter(
    filtered_data,
    x="Number Of Ratings",
    y="Sale Price",
    size="Discount Percentage",
    color="Star Rating",
    trendline="ols",
    title="Sale Price vs Number of Ratings"
)

scatter_fig.update_layout(
    plot_bgcolor="#0f0f0f",
    paper_bgcolor="#0f0f0f",
    font_color="white"
)

st.plotly_chart(scatter_fig, use_container_width=True)

# ---------------------- Rating Distribution ----------------------
st.subheader("Rating Distribution")

hist_fig = px.histogram(
    filtered_data,
    x="Star Rating",
    nbins=10
)

hist_fig.update_layout(
    plot_bgcolor="#0f0f0f",
    paper_bgcolor="#0f0f0f",
    font_color="white"
)

st.plotly_chart(hist_fig, use_container_width=True)

# ---------------------- Raw Data ----------------------
st.subheader("Explore Raw Data")
st.dataframe(filtered_data, use_container_width=True)

st.markdown("---")
st.caption("Built with Streamlit & Plotly | Apple iPhone Sales Analysis Project")
