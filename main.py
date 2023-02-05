import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

#Titles and subtitles
st.title("crypto currency daily prices")
st.header("Main Dashboard")
st.subheader("you can add more crypto in code")

#defining 
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
Bitcoincash = 'BCH-USD'

#Access data
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(Bitcoincash)

#fetch history data from yahoo
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

#fetch crypto for the dataframe 
BTC = yf.download(Bitcoin, start="2023-02-02", end="2023-02-04")
ETH = yf.download(Ethereum, start="2023-02-02", end="2023-02-04")
XRP = yf.download(Ripple, start="2023-02-02", end="2023-02-04")
BCH = yf.download(Bitcoincash, start="2023-02-02", end="2023-02-04")

#Bitcoin
st.write("Bitcoin ($)")
ImageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
#display image
st.image(ImageBTC)
#display Dataframe
st.table(BTC)
#display Dataframe
st.bar_chart(BTCHis.Close)

#Ethereum
st.write("Ethereum ($)")
ImageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
#display image
st.image(ImageETH)
#display Dataframe
st.table(ETH)
#display Dataframe
st.bar_chart(ETHHis.Close)

#Ripple
st.write("Ripple ($)")
ImageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
#display image
st.image(ImageXRP)
#display Dataframe
st.table(XRP)
#display Dataframe
st.bar_chart(XRPHis.Close)

#Bitcoincash
st.write("Bitcoincash ($)")
ImageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
#display image
st.image(ImageBCH)
#display Dataframe
st.table(BCH)
#display Dataframe
st.bar_chart(BCHHis.Close)
