import streamlit as st
from detectorPhishing import is_phishing

st.set_page_config(page_title="PhishGuard-AI", page_icon="🛡️")
st.title("🛡️ PhishGuard-AI")
st.write("Enter any URL and check if it's phishing or safe.")

url = st.text_input("Enter URL:")

if st.button("Check"):
    if url:
        score, reasons = is_phishing(url)
        if score >= 2:
            st.error(f"⚠️ Phishing Detected! Risk Score: {score}")
            st.write(reasons)
        else:
            st.success(f"✅ Safe URL! Risk Score: {score}")
    else:
        st.warning("Please enter a URL")
import re

x