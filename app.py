import streamlit as st

# Page configuration for a professional browser tab look
st.set_page_config(page_title="Justin Currency Converter", page_icon="💱", layout="centered")

# Custom styling to make the app pop
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title & Description
st.title("💱 Justin Currency Converter")
st.markdown("Convert currencies from around the world with ease. Enter the amount, select the source and target currencies, and get the converted value instantly.")

# Create a list of available currencies
currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "INR", "BRL", "ZAR", "MXN", "SGD", "HKD", "KRW", "TRY", "RUB", "SAR", "AED", "THB", "MYR", "IDR", "PHP", "VND", "PLN", "HUF", "CZK", "DKK", "NOK", "ILS", "CLP", "COP", "PEN", "ARS", "EGP", "KWD", "QAR", "BHD", "OMR", "JOD", "LKR", "PKR", "BDT", "NPR", "MMK", "KHR", "LAK", "MNT", "UZS", "TWD", "KZT", "AZN", "GEL", "BYN", "UAH", "MDL", "BGN", "RON", "HRK", "ISK", "MKD", "ALB", "BIH", "SRD", "GYD", "TTD", "BBD", "JMD", "BZD", "HTG", "XCD", "XOF", "XAF", "XPF", "ZMW", "MZN", "MWK", "LSL", "SZL", "BWP", "NAD", "MUR", "SCR", "FJD", "PGK", "SBD", "VUV", "TOP", "WST", "KPW", "TJS", "TMT", "AFN", "BTN", "BND", "MVR", "UYU", "PYG", "BOB", "VEF"]

# Remove any accidental duplicates while keeping order
currencies = list(dict.fromkeys(currencies))

# Create dropdown menus for "From" and "To" currencies inside a clean layout
col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("📤 From Currency", currencies)
with col2:
    to_currency = st.selectbox("📥 To Currency", currencies, index=1)

# Input box for the amount
amount = st.number_input("💵 Enter Amount", min_value=0.0, value=100.0, step=10.0)

# Exchange rates dictionary
rates = {
    "USD": 1.0, "EUR": 0.85, "GBP": 0.75, "JPY": 110.0, "AUD": 1.35,
    "CAD": 1.25, "CHF": 0.92, "CNY": 6.45, "SEK": 8.6, "NZD": 1.65,
    "INR": 74.0, "BRL": 5.2, "ZAR": 14.5, "MXN": 20.0, "SGD": 1.35,
    "HKD": 7.8, "KRW": 1150.0, "TRY": 8.5, "RUB": 73.0, "SAR": 3.75,
    "AED": 3.67, "THB": 32.0, "MYR": 4.15, "IDR": 14200.0, "PHP": 50.0,
    "VND": 23000.0, "PLN": 3.8, "HUF": 300.0, "CZK": 21.0, "DKK": 6.3,
    "NOK": 8.5, "ILS": 3.2, "CLP": 750.0, "COP": 3800.0, "PEN": 3.8,
    "ARS": 95.0, "EGP": 15.7, "KWD": 0.3, "QAR": 3.64, "BHD": 0.38,
    "OMR": 0.38, "JOD": 0.71, "LKR": 200.0, "PKR": 160.0, "BDT": 85.0,
    "NPR": 120.0, "MMK": 1700.0, "KHR": 4000.0, "LAK": 9500.0, "MNT": 2850.0,
    "UZS": 10500.0, "TWD": 28.0, "KZT": 425.0, "AZN": 1.7, "GEL": 3.1,
    "BYN": 2.5, "UAH": 27.0, "MDL": 17.0, "BGN": 1.65, "RON": 4.1,
    "HRK": 6.3, "ISK": 130.0, "MKD": 52.0, "ALB": 105.0, "BIH": 1.7,
    "SRD": 14.0, "GYD": 210.0, "TTD": 6.8, "BBD": 2.0, "JMD": 150.0,
    "BZD": 2.0, "HTG": 90.0, "XCD": 2.7, "XOF": 550.0, "XAF": 550.0,
    "XPF": 100.0, "ZMW": 22.0, "MZN": 63.0, "MWK": 800.0, "LSL": 15.0,
    "SZL": 15.0, "BWP": 11.0, "NAD": 15.0, "MUR": 40.0, "SCR": 15.0,
    "FJD": 2.0, "PGK": 3.5, "SBD": 8.0, "VUV": 115.0, "TOP": 2.3,
    "WST": 2.5, "KPW": 900.0, "TJS": 11.0, "TMT": 3.5, "AFN": 77.0,
    "BTN": 75.0, "BND": 1.35, "MVR": 15.0, "VEF": 248000.0, "UYU": 43.0,
    "PYG": 6900.0, "BOB": 6.9
}

# Conversion execution
if st.button("✨ Convert Now"):
    # Convert input to USD first, then to target currency
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    
    st.markdown("---")
    # Modern visual metric output card
    st.metric(
        label=f"Converted Value ({to_currency})", 
        value=f"{converted_amount:,.2f} {to_currency}", 
        delta=f"From {amount:,.2f} {from_currency}"
    )
    st.balloons() # Fun celebration effect!