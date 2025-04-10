
import streamlit as st

# Title
st.title("Apartment Underwriting Calculator")

# Input sliders and fields
num_units = st.number_input("Number of Units", min_value=1, value=40)
market_rent = st.number_input("Market Rent ($/month)", min_value=0.0, value=2000.0)
other_income_pct = st.number_input("Other Income (%)", min_value=0.0, value=3.25)
occupancy_pct = st.slider("Occupancy (%)", min_value=0, max_value=100, value=93)
expense_pct = st.slider("Expenses (% of EGI)", min_value=0, max_value=100, value=40)
cap_rate_pct = st.slider("Cap Rate (%)", min_value=1, max_value=15, value=6)

# Calculation function
def calculate_underwriting(num_units, market_rent, other_income_pct, occupancy_pct, expense_pct, cap_rate_pct):
    gross_rent = num_units * market_rent * 12
    other_income = gross_rent * (other_income_pct / 100)
    effective_income = (gross_rent + other_income) * (occupancy_pct / 100)
    expenses = effective_income * (expense_pct / 100)
    noi = effective_income - expenses
    cap_rate = cap_rate_pct / 100
    offer_price = noi / cap_rate if cap_rate > 0 else 0
    return gross_rent, other_income, effective_income, expenses, noi, offer_price

# Run calculation
gross_rent, other_income, effective_income, expenses, noi, offer_price = calculate_underwriting(
    num_units, market_rent, other_income_pct, occupancy_pct, expense_pct, cap_rate_pct
)

# Display results
st.subheader("Results")
st.write(f"**Gross Potential Rent:** ${gross_rent:,.2f}")
st.write(f"**Other Income:** ${other_income:,.2f}")
st.write(f"**Effective Gross Income:** ${effective_income:,.2f}")
st.write(f"**Expenses:** ${expenses:,.2f}")
st.write(f"**Net Operating Income (NOI):** ${noi:,.2f}")
st.success(f"**Suggested Offer Price:** ${offer_price:,.2f}")
