import streamlit as st
from modules.econ_event import get_economic_signals
from modules.option_flow import get_option_signals
from modules.cot_fetcher import get_cot_sentiment

st.set_page_config(layout="wide")
st.title("🧠 Live Sentiment Scanner - AI EdgeFinder")

# Fetch live signals
econ_signals = get_economic_signals()
option_signals = get_option_signals()
cot_signals = get_cot_sentiment()

categories = {
    "Economic Signals": econ_signals,
    "Options Flow": option_signals,
    "COT Sentiment": cot_signals
}

for category, signals in categories.items():
    st.subheader(category)
    if signals:
        st.table(signals)
    else:
        st.write("No live signals available.")