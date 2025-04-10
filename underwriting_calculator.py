import streamlit as st

st.set_page_config(page_title="Commercial Underwriting Calculator", layout="centered")

st.title("🏢 Commercial Underwriting Calculator")

# --- INPUTS ---
st.subheader("Enter Deal Info")

noi = st.number_input("Net Operating Income (NOI) ($)", min_value=0.0, value=100000.0, step=1000.0)
cap_rate = st.number_input("Your Target Cap Rate (%)", min_value=1.0, value=6.0, step=0.1)

lease_term = st.number_input("Remaining Lease Term (Years)", min_value=0.0, value=10.0)
rent_bumps = st.number_input("Annual Rent Bumps (%) [Optional]", min_value=0.0, value=0.0)

tenant_rating = st.selectbox("Tenant Credit Rating", ["AAA", "A", "BBB", "Unrated"])
property_class = st.selectbox("Property Class / Location Score", ["A", "B", "C"])

# --- CALCULATION ---
base_offer = noi / (cap_rate / 100)

# Risk-based adjustment
discount = 0
if tenant_rating == "BBB":
    discount += 0.03
elif tenant_rating == "Unrated":
    discount += 0.05

if property_class == "B":
    discount += 0.02
elif property_class == "C":
    discount += 0.04

adjusted_offer = base_offer * (1 - discount)

# --- RESULTS ---
st.divider()
st.subheader("📊 Results")

st.markdown(f"**Base Offer (NOI / Cap Rate):** `${base_offer:,.2f}`")

if discount > 0:
    st.markdown(f"**Risk Adjusted Discount:** `{discount * 100:.1f}%`")
    st.success(f"**Final Suggested Offer Price:** `${adjusted_offer:,.2f}`")
else:
    st.success(f"**Suggested Offer Price:** `${base_offer:,.2f}`")
