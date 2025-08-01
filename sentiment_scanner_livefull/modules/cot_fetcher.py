import pandas as pd

def get_cot_sentiment():
    # Simulated live COT sentiment data
    data = [
        {"Asset": "EURUSD", "Sentiment": "Bullish", "Net Positions": 44000},
        {"Asset": "USDJPY", "Sentiment": "Bearish", "Net Positions": -32000},
    ]
    return pd.DataFrame(data)