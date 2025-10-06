import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Stable layout
st.set_page_config(layout="wide", page_title="Input Interface")

# Get current directory
base_path = Path(__file__).parent

# Load HTML and CSS
html_path = base_path / "index.html"
css_path = base_path / "styles.css"

html_content = html_path.read_text(encoding="utf-8")
css_content = css_path.read_text(encoding="utf-8")

# Combine HTML and CSS
final_html = f"""
    <style>
    {css_content}
    </style>
    {html_content}
"""

# Render inside Streamlit
components.html(final_html, height=1500, scrolling=True)
