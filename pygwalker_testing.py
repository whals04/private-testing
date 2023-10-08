import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Use Pygwalker In Streamlit")
 
# Import your data
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
 
# Paste the copied Pygwalker chart code here
vis_spec = """<PASTE_COPIED_CODE_HERE>"""
 
# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, spec=vis_spec, return_html=True)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
