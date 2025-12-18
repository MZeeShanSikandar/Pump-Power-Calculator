import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Advanced Pump Power Calculator",
    page_icon="⚙️",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align: center;'>⚙️ Advanced Pump Power Calculator</h1>
    <p style='text-align: center; font-size: 16px;'>
    Engineering tool for pump and motor power estimation
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Options")

include_motor = st.sidebar.checkbox("Include Motor Power", value=True)
include_losses = st.sidebar.checkbox("Include Head Losses", value=True)
efficiency_format = st.sidebar.radio("Efficiency Format", ["Decimal", "Percentage"])

st.sidebar.divider()
st.sidebar.info("Mechanical Engineering Utility")

# ---------------- INPUT SECTION ----------------
st.subheader("📥 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    Q = st.number_input(
        "Flow Rate (Q)",
        min_value=0.0,
        step=0.001
    )

    Q_unit = st.selectbox(
        "Flow Rate Unit",
        ["m³/s", "m³/hr", "L/s"]
    )

    rho = st.number_input(
        "Fluid Density ρ (kg/m³)",
        value=1000.0,
        step=10.0
    )

with col2:
    H = st.number_input(
        "Static Head H (m)",
        min_value=0.0,
        step=0.1
    )

    if include_losses:
        losses = st.number_input(
            "Head Losses (m)",
            min_value=0.0,
            step=0.1
        )
    else:
        losses = 0.0

    if efficiency_format == "Percentage":
        eta = st.number_input(
            "Pump Efficiency (%)",
            min_value=1.0,
            max_value=100.0,
            value=70.0
        ) / 100
    else:
        eta = st.number_input(
            "Pump Efficiency (0–1)",
            min_value=0.01,
            max_value=1.0,
            value=0.7
        )

st.divider()

# ---------------- UNIT CONVERSION ----------------
if Q_unit == "m³/hr":
    Q = Q / 3600
elif Q_unit == "L/s":
    Q = Q / 1000

H_total = H + losses
g = 9.81

# ---------------- CALCULATION ----------------
if st.button("🧮 Calculate Power", use_container_width=True):

    hydraulic_power = (rho * g * Q * H_total) / 1000
    pump_power = hydraulic_power / eta

    st.subheader("📊 Results")

    st.metric("Hydraulic Power", f"{hydraulic_power:.3f} kW")
    st.metric("Pump Shaft Power", f"{pump_power:.3f} kW")

    if include_motor:
        motor_eff = st.slider(
            "Motor Efficiency (%)",
            min_value=70,
            max_value=98,
            value=90
        )
        motor_power = pump_power / (motor_eff / 100)
        st.metric("Required Motor Power", f"{motor_power:.3f} kW")

    st.success("Calculation completed successfully ✔️")

    st.caption(
        "Formula: P = (ρ × g × Q × H) / η"
    )

# ---------------- FOOTER ----------------
st.divider()
st.markdown(
    "<p style='text-align: center; font-size: 13px;'>"
    "Pump & Fluid Machinery • Mechanical Engineering Tool"
    "</p>",
    unsafe_allow_html=True
)
