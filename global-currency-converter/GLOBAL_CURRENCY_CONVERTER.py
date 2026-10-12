import requests
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Justin's Global Currency Converter",
    layout="centered",
)

# App header
st.title("🍎Justin's Global Currency Converter🍎")
st.markdown("🍎Convert currencies from around the world! (yes there's an apple emoji)🍎")
st.divider()

# Comprehensive currency name mapping dictionary
CURRENCY_NAMES = {
    "AED": "United Arab Emirates Dirham",
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
    "AMD": "Armenian Dram",
    "ANG": "Netherlands Antillean Guilder",
    "AOA": "Angolan Kwanza",
    "ARS": "Argentine Peso",
    "AUD": "Australian Dollar",
    "AWG": "Aruban Florin",
    "AZN": "Azerbaijani Manat",
    "BAM": "Bosnia-Herzegovina Convertible Mark",
    "BBD": "Barbadian Dollar",
    "BDT": "Bangladeshi Taka",
    "BGN": "Bulgarian Lev",
    "BHD": "Bahraini Dinar",
    "BIF": "Burundian Franc",
    "BMD": "Bermudan Dollar",
    "BND": "Brunei Dollar",
    "BOB": "Bolivian Boliviano",
    "BRL": "Brazilian Real",
    "BSD": "Bahamian Dollar",
    "BTN": "Bhutanese Ngultrum",
    "BWP": "Botswanan Pula",
    "BYN": "Belarusian Ruble",
    "BZD": "Belize Dollar",
    "CAD": "Canadian Dollar",
    "CDF": "Congolese Franc",
    "CHF": "Swiss Franc",
    "CLP": "Chilean Peso",
    "CNY": "Chinese Yuan",
    "COP": "Colombian Peso",
    "CRC": "Costa Rican Colón",
    "CUP": "Cuban Peso",
    "CVE": "Cape Verdean Escudo",
    "CZK": "Czech Republic Koruna",
    "DJF": "Djiboutian Franc",
    "DKK": "Danish Krone",
    "DOP": "Dominican Peso",
    "DZD": "Algerian Dinar",
    "EGP": "Egyptian Pound",
    "ERN": "Eritrean Nakfa",
    "ETB": "Ethiopian Birr",
    "EUR": "Euro",
    "FJD": "Fijian Dollar",
    "FKP": "Falkland Islands Pound",
    "GBP": "British Pound Sterling",
    "GEL": "Georgian Lari",
    "GHS": "Ghanaian Cedi",
    "GIP": "Gibraltar Pound",
    "GMD": "Gambian Dalasi",
    "GNF": "Guinean Franc",
    "GTQ": "Guatemalan Quetzal",
    "GYD": "Guyanese Dollar",
    "HKD": "Hong Kong Dollar",
    "HNL": "Honduran Lempira",
    "HRK": "Croatian Kuna",
    "HTG": "Haitian Gourde",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "IQD": "Iraqi Dinar",
    "IRR": "Iranian Rial",
    "ISK": "Icelandic Króna",
    "JMD": "Jamaican Dollar",
    "JOD": "Jordanian Dinar",
    "JPY": "Japanese Yen",
    "KES": "Kenyan Shilling",
    "KGS": "Kyrgystani Som",
    "KHR": "Cambodian Riel",
    "KMF": "Comorian Franc",
    "KRW": "South Korean Won",
    "KWD": "Kuwaiti Dinar",
    "KYD": "Cayman Islands Dollar",
    "KZT": "Kazakhstani Tenge",
    "LAK": "Laotian Kip",
    "LBP": "Lebanese Pound",
    "LKR": "Sri Lankan Rupee",
    "LRD": "Liberian Dollar",
    "LSL": "Lesotho Loti",
    "LYD": "Libyan Dinar",
    "MAD": "Moroccan Dirham",
    "MDL": "Moldovan Leu",
    "MGA": "Malagasy Ariary",
    "MKD": "Macedonian Denar",
    "MMK": "Myanma Kyat",
    "MNT": "Mongolian Tugrik",
    "MOP": "Macanese Pataca",
    "MRU": "Mauritanian Ouguiya",
    "MUR": "Mauritian Rupee",
    "MVR": "Maldivian Rufiyaa",
    "MWK": "Malawian Kwacha",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "MZN": "Mozambican Metical",
    "NAD": "Namibian Dollar",
    "NGN": "Nigerian Naira",
    "NIO": "Nicaraguan Córdoba",
    "NOK": "Norwegian Krone",
    "NPR": "Nepalese Rupee",
    "NZD": "New Zealand Dollar",
    "OMR": "Omani Rial",
    "PAB": "Panamanian Balboa",
    "PEN": "Peruvian Nuevo Sol",
    "PGK": "Papua New Guinean Kina",
    "PHP": "Philippine Peso",
    "PKR": "Pakistani Rupee",
    "PLN": "Polish Zloty",
    "PYG": "Paraguayan Guarani",
    "QAR": "Qatari Rial",
    "RON": "Romanian Leu",
    "RSD": "Serbian Dinar",
    "RUB": "Russian Ruble",
    "RWF": "Rwandan Franc",
    "SAR": "Saudi Riyal",
    "SBD": "Solomon Islands Dollar",
    "SCR": "Seychellois Rupee",
    "SDG": "Sudanese Pound",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "SHP": "Saint Helena Pound",
    "SLL": "Sierra Leonean Leone",
    "SOS": "Somali Shilling",
    "SRD": "Surinamese Dollar",
    "SSP": "South Sudanese Pound",
    "STN": "São Tomé and Príncipe Dobra",
    "SYP": "Syrian Pound",
    "SZL": "Swazi Lilangeni",
    "THB": "Thai Baht",
    "TJS": "Tajikistani Somoni",
    "TMT": "Turkmenistani Manat",
    "TND": "Tunisian Dinar",
    "TOP": "Tongan Paʻanga",
    "TRY": "Turkish Lira",
    "TTD": "Trinidad and Tobago Dollar",
    "TWD": "New Taiwan Dollar",
    "TZS": "Tanzanian Shilling",
    "UAH": "Ukrainian Hryvnia",
    "UGX": "Ugandan Shilling",
    "USD": "United States Dollar",
    "UYU": "Uruguayan Peso",
    "UZS": "Uzbekistan Som",
    "VES": "Sovereign Bolivar",
    "VND": "Vietnamese Dong",
    "VUV": "Vanuatu Vatu",
    "WST": "Samoan Tala",
    "XAF": "CFA Franc BEAC",
    "XCD": "East Caribbean Dollar",
    "XOF": "CFA Franc BCEAO",
    "XPF": "CFP Franc",
    "YER": "Yemeni Rial",
    "ZAR": "South African Rand",
    "ZMW": "Zambian Kwacha",
    "ZWL": "Zimbabwean Dollar",
}


@st.cache_data(ttl=3600)
def get_exchange_rates(base_currency):
  url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
  response = requests.get(url)

  if response.status_code == 200:
    return response.json().get("rates", {})

  st.error("Failed to fetch exchange rates. Please try again later.")
  return {}


rates = get_exchange_rates("USD")
if rates:
  raw_currencies = list(rates.keys())

  # Format currency option labels to include full names (e.g., "USD - United States Dollar")
  currency_options = [
      f"{code} - {CURRENCY_NAMES.get(code, 'Unknown Currency')}"
      for code in raw_currencies
  ]


  def get_code_from_selection(selection):
    return selection.split(" - ")[0]


  col1, col2 = st.columns(2)
  with col1:
    default_from = next(
        (opt for opt in currency_options if opt.startswith("USD")),
        currency_options[0],
    )
    from_selection = st.selectbox(
        "From Currency",
        options=currency_options,
        index=currency_options.index(default_from),
    )
    from_currency = get_code_from_selection(from_selection)

  with col2:
    default_to = next(
        (opt for opt in currency_options if opt.startswith("EUR")),
        currency_options[1] if len(currency_options) > 1 else currency_options[0],
    )
    to_selection = st.selectbox(
        "To Currency",
        options=currency_options,
        index=currency_options.index(default_to),
    )
    to_currency = get_code_from_selection(to_selection)

  amount = st.number_input(
      "Enter Amount to Convert",
      min_value=0.0,
      value=100.0,
      step=1.0,
  )

  if st.button("Convert", type="primary", use_container_width=True):
    with st.spinner("Fetching latest exchange rates..."):
      current_rates = get_exchange_rates(from_currency)

    if current_rates and to_currency in current_rates:
      rate = current_rates[to_currency]
      converted_amount = amount * rate
      st.success("Conversion Successful")
      st.metric(
          label=f"{amount:,.2f} {from_currency} equals",
          value=f"{converted_amount:,.2f} {to_currency}",
          delta=f"Rate: 1 {from_currency} = {rate:,.4f} {to_currency}",
      )
    else:
      st.warning("Selected currency is unavailable.")
else:
  st.warning("Unable to load exchange rates. Please try again later.")

# Footer info
st.markdown("---")
st.caption("Powered by Streamlit and Open Exchange Rates API. (and me)")
