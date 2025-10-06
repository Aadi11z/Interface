import streamlit as st
from pathlib import Path

# Force layout for stability
st.set_page_config(layout="wide", page_title="Input Interface")

# Load HTML template
html_content = Path("index.html").read_text()
st.components.v1.html(html_content, height=1500, scrolling=True)
