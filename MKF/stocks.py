import yfincance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple Stock Price App

shown are the stock closing price and volume of Google!

""")

# https:// towardsdatascience.com/how-to-get-stock-data-using-python-c0de1f17e75
#define the ticker symbol
tickerSymbol = 'Workhorse'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High Low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.close)
st.line_chart(ticekrDf.Volume)