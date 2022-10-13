import yfinance as yf 
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

st.write("""


# Shown here are the stock closing price and volume of Google

The text is written in markdown style you can use a cheat sheet
to find all the characters 
The # creates a strong heading

""")

tickerSymbol = 'GOOGL'

tickerData= yf.Ticker(tickerSymbol)

TickerDf = tickerData.history(period = '1d', start ='2010-5-31', end = '2022-5-31')
# yf.Ticker will retrieve data such as Open High Low Close Volume
# Dividends stock splits
st.write("""
This is a line chart for close
""")
st.line_chart(TickerDf.Close)
st.write("""
This is a line chart for Volume
""")
st.line_chart(TickerDf.Volume)

npa2 = np.arange(0,5)
npa2

mat5 = np.random.randint(0,100,50)
mat5
st.write("""
"Mean :" """) 
meanmat = mat5.mean()
meanmat