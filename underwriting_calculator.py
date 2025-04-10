import streamlit as st

st.set_page_config(page_title="Commercial Underwriting Calculator", layout="centered")

st.title("🏢 Commercial Underwriting Calculator")

# --- INPUTS ---
st.subheader("Enter Deal Info")

noi = st.number_input("Net Operating Income (NOI) ($)", min_value=0.0, value=100000.0, step=1000.0)
cap_rate = st.number_input("Your Target Cap Rate (%)", min_value=1.0, value=6.0, step=0.1)

lease_term = st.number_input("Remaining Lease Term (Years)", min_value=0.0, value=10.0)
rent_bumps = st.number_input("Annual Rent Bumps (%) [Optional]", min_value=0.0, value=0.0)

tenant_rating = st.selectbox("Tenant Credit Rating", ["AAA", "AA", "A", "BBB", "Sub-Investment", "Unrated"])
property_class = st.selectbox("Property Class / Location Score", ["A", "B", "C"])

# --- BASE CALCULATION ---
base_offer = noi / (cap_rate / 100)
adjusted_offer = base_offer  # start from base

# --- LEASE TERM Adjustment ---
if lease_term < 10:
    adjusted_offer *= 0.95  # -5% discount
elif lease_term > 15:
    adjusted_offer *= 1.02  # +2% premium

# --- RENT BUMPS Adjustment ---
if rent_bumps > 3:
    adjusted_offer *= 1.01  # +1% premium
elif rent_bumps == 0:
    adjusted_offer *= 0.97  # -3% discount

# --- TENANT CREDIT RATING Adjustment ---
credit_adjustments = {
    "AAA": 1.01,
    "AA": 1.00,
    "A": 0.99,
    "BBB": 0.98,
    "Sub-Investment": 0.95,
    "Unrated": 0.95
}
adjusted_offer *= credit_adjustments.get(tenant_rating, 1.00)

# --- PROPERTY CLASS Adjustment ---
location_adjustments = {
    "A": 1.01,
    "B": 0.99,
    "C": 0.97
}
adjusted_offer *= location_adjustments.get(property_class, 1.00)

# --- RESULTS ---
st.divider()
st.subheader("📊 Results")

st.markdown(f"**Base Offer (NOI / Cap Rate):** `${base_offer:,.2f}`")
st.success(f"**Suggested Offer Price:** `${adjusted_offer:,.2f}`")
