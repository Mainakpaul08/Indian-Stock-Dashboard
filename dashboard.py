from nselib import capital_market
from nselib import  derivatives
import streamlit as st

st.header('Indian Stock Dashboard')


istrument = st.sidebar.selectbox('Instruement Type',options=('NSE Equity Market','NSE Derivatives Market'))

data_info = st.sidebar.selectbox(
    "Data to extract",
    options=(
        "bhav_copy_equities",
        "bhav_copy_with_delivery",
        "equity_list",
        "fno_equity_list",
        "market_watch_all_indices",
        "nifty50_equity_list",
        "block_deals_data",
        "bulk_deal_data",
        "india_vix_data",
        "short_selling_data",
        "deliverable_position_data",
        "index_data",
        "price_volume_and_deliverable_position_data",
        "price_volume_data"
    )
)
# no date

if data_info in (
    "equity_list",
    "fno_equity_list",
    "market_watch_all_indices",
    "nifty50_equity_list"
):
    data = getattr(capital_market, data_info)()

#  one date

if data_info in (
    "bhav_copy_equities",
    "bhav_copy_with_delivery"
):
    date = st.sidebar.text_input("Date", "22-12-2023")
    data = getattr(capital_market, data_info)(date)

# Functions that also require a date

if data_info in (
    "block_deals_data",
    "bulk_deal_data",
    "india_vix_data",
    "short_selling_data"
):
    Period_= st.sidebar.text_input("Period", "1M")
    data = getattr(capital_market, data_info)(period = Period_)


st.write(data)