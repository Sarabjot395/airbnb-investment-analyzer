import streamlit as st
import pandas as pd

st.set_page_config(page_title="Airbnb Investment Analyzer", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("Data/Processed/AB_US_2020_cleaned.csv")
    return df

df = load_data()

st.title("🏠 Airbnb Investment Analyzer")
st.markdown("Find the best Airbnb investment opportunities based on your budget and preferences.")

# --- Sidebar: User Inputs ---
st.sidebar.header("Your Investment Criteria")

city = st.sidebar.selectbox(
    "City",
    options=["All"] + sorted(df["city"].unique().tolist())
)

budget = st.sidebar.slider(
    "Max Nightly Price Budget ($)",
    min_value=int(df["price"].min()),
    max_value=int(df["price"].quantile(0.95)),  # cap at 95th percentile so the slider stays usable
    value=200,
    step=10
)

room_type = st.sidebar.multiselect(
    "Property Type",
    options=df["room_type"].unique().tolist(),
    default=df["room_type"].unique().tolist()
)

min_occupancy = st.sidebar.slider(
    "Minimum Occupancy Proxy (reviews/month)",
    min_value=0.0,
    max_value=float(df["reviews_per_month"].quantile(0.95)),
    value=0.5,
    step=0.1
)

# --- Filter Data Based on Inputs ---
filtered = df.copy()

if city != "All":
    filtered = filtered[filtered["city"] == city]

filtered = filtered[
    (filtered["price"] <= budget) &
    (filtered["room_type"].isin(room_type)) &
    (filtered["reviews_per_month"] >= min_occupancy)
]

# --- Calculate Estimated Revenue ---
filtered["est_annual_revenue"] = filtered["price"] * filtered["reviews_per_month"] * 12

# --- Main Panel: Results ---
st.subheader(f"Matching Listings: {len(filtered):,}")

if len(filtered) == 0:
    st.warning("No listings match your criteria. Try adjusting your budget or occupancy threshold.")
else:
    # Top-level metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Price", f"${filtered['price'].mean():.0f}")
    col2.metric("Avg Occupancy Proxy", f"{filtered['reviews_per_month'].mean():.2f}")
    col3.metric("Avg Est. Annual Revenue", f"${filtered['est_annual_revenue'].mean():,.0f}")

    st.markdown("### Best Neighborhoods for These Criteria")
    neighborhood_summary = (
        filtered.groupby(["city", "neighbourhood"])
        .agg(
            avg_price=("price", "mean"),
            avg_occupancy=("reviews_per_month", "mean"),
            avg_est_revenue=("est_annual_revenue", "mean"),
            listing_count=("id", "count")
        )
        .query("listing_count >= 5")  # avoid tiny, unreliable samples
        .sort_values("avg_est_revenue", ascending=False)
        .head(10)
        .round(2)
    )
    st.dataframe(neighborhood_summary, use_container_width=True)

    st.markdown("### Top Individual Listings")
    top_listings = (
        filtered[["name", "city", "neighbourhood", "room_type", "price", "reviews_per_month", "est_annual_revenue"]]
        .sort_values("est_annual_revenue", ascending=False)
        .head(20)
        .round(2)
    )
    st.dataframe(top_listings, use_container_width=True)

st.markdown("---")
st.caption(
    "Estimated annual revenue = price × reviews_per_month (occupancy proxy) × 12. "
    "This is a directional estimate, not a financial guarantee. "
    "Data source: US Airbnb Open Data (Inside Airbnb, via Kaggle)."
)