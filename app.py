import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide", page_title="Input Interface")

base_path = Path(__file__).parent
html_content = (base_path / "index.html").read_text()

components.html(html_content, height=1500, scrolling=True)
