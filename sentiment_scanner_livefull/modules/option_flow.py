import pandas as pd

def get_option_signals():
    # Simulated live options flow results
    data = [
        {"Ticker": "AAPL", "Flow": "Bullish", "Volume": 12000, "OI": 54000, "Expiry": "2025-08-02"},
        {"Ticker": "TSLA", "Flow": "Bearish", "Volume": 8900, "OI": 30000, "Expiry": "2025-08-02"},
    ]
    return pd.DataFrame(data)