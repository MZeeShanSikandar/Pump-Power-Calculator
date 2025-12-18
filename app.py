import streamlit as st

st.set_page_config(page_title="Pump Power Calculator", layout="centered")

st.title("💧 Pump Power Calculator")
st.write("Calculate the required pump power based on flow rate, head, efficiency, and fluid density.")

st.divider()

# Input fields
Q = st.number_input(
    "Flow Rate, Q (m³/s)",
    min_value=0.0,
    step=0.001,
    help="Volume flow rate of the fluid"
)

H = st.number_input(
    "Pump Head, H (m)",
    min_value=0.0,
    step=0.1,
    help="Total head developed by the pump"
)

eta = st.number_input(
    "Pump Efficiency, η (0–1)",
    min_value=0.01,
    max_value=1.0,
    value=0.7,
    step=0.01,
    help="Overall pump efficiency"
)

rho = st.number_input(
    "Fluid Density, ρ (kg/m³)",
    min_value=1.0,
    value=1000.0,
    step=10.0,
    help="Density of the pumped fluid (water ≈ 1000 kg/m³)"
)

st.divider()

# Calculation
if st.button("🔢 Calculate Pump Power"):
    g = 9.81  # gravitational acceleration (m/s²)
    
    power_kw = (rho * g * Q * H) / (eta * 1000)

    st.success(f"### Required Pump Power = **{power_kw:.3f} kW**")

    st.caption(
        "Formula used:  P = (ρ × g × Q × H) / η"
    )
