import pandas as pd
import streamlit as st
import yfinance as yf

st.write (
    """
    # Stock Price Analyser

    Shown are the stock prices of Apple.
    """
)

ticker_symbol = st.text_input("Enter stock Symbol",
                              "AAPL",
                              key = "placeholder")

#ticker_symbol = 'AAPL'

ticker_data = yf.Ticker(ticker_symbol)

start_date = st.date_input('Input Starting Date')

end_date = st.date_input('Input end date')

ticker_df = ticker_data.history(period = '1d',
                                start = f'{start_date}',
                                end = f'{end_date}')

st.write(f"""
### {ticker_symbol}'s Stock Prices""")

st.dataframe(ticker_df)

st.write(
    """
    ## Daily Closing Price Chart
    """
)

## showcasing the charts
st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)